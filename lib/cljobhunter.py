def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
load_src("settings", "settings.py")
from craigslist import CraigslistJobs
from slackclient import SlackClient
import time
import settings
from dateutil.parser import parse
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy import Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    sc = SlackClient(settings.SLACK_TOKEN)
except AttributeError:
    sc = None

engine = create_engine('sqlite:///listings.db', echo=True)
Base = declarative_base()

class Listings(Base):
    __tablename__= 'joblistings'
    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    geotag = Column(String)
    name = Column(String)
    price = Column(String)
    location = Column(String)
    cl_id = Column(Integer, unique=True)
    area = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def create_list(area, result):
    listing = Listings(
            cl_id = result["id"],
            link = result["url"],
            created = parse(result["datetime"]),
            name = result["name"],
            price = result["price"],
            location = result["where"],
            )
    return listing

def save_to_db(listing):
    session.add(listing)
    session.commit()

def area_in_bounds(coords, box = settings.AREAS_OF_INTEREST):
    if coords is not None and len(coords) == 2 and \
        box[0][0] < coords[0] < box[1][0] and \
        box[0][1] < coords[1] < box[1][1]:
        return True
    return False


def in_area_of_interest(geotag):
    area = None 
    area_found = False
    if geotag is not None and len(geotag) == 2:
        for a, coords in settings.JOB_AREAS_OF_INTEREST.items():
            if area_in_bounds(geotag, coords):
                area = a
                area_found = True
    return (area_found, area);


def not_in_undesired_areas(location):
    for hood in settings.JOB_LOCATIONS_UNWANTED:
        if location is None or hood.lower() in location.lower():
            return False
    return True 


def cl_info_parser(area, result):
    desc = None
    if area is None and result["where"] is None:
        area = "N/A"
    elif area is not None:
        location = area
    else:
        location = result["where"]
    try:
        desc = "{0} | {1} | <{2}>".format(\
            result["name"], location, result["url"])
    except UnicodeEncodeError:
        print "UnicodeEncodeError for url:{}".format(result["url"])
    except TypeError:
        print "Method argument error."
    return desc


def post_to_slack(description):
    if description is not None and sc is not None:
        sc.api_call( "chat.postMessage", channel=settings.SLACK_CHANNEL_JOBS, 
                text=description, username='Hal-2000')
    elif sc is None:
        print description
    else:
        print("Error. Nothing to post.")


def scrape_cl(cl_jobs):
    for result in cl_jobs.get_results(sort_by='newest', geotagged=True):
        geotag = result["geotag"]
        aoi_tuple = in_area_of_interest(geotag) 
        aoi_found = aoi_tuple[0]
        if aoi_found is not True:
            location = result["where"]
            aoi_found = not_in_undesired_areas(location)
        if aoi_found is True:
            area = aoi_tuple[1]
            description = cl_info_parser(area, result)
            listing = create_list(area, result)
            save_to_db(listing)
            post_to_slack(description)


def start_cl_job_hunt():
    if sc is None:
        print "\nSlack Token is missing. Displaying results in command-line:\n"
    for keyword in settings.JOB_SEARCHWORD:
        cl_jobs = CraigslistJobs(
                                        site=settings.SITE,
                                        category=settings.JOB_CATEGORY, 
                                        filters={'query': keyword }
                )
        scrape_cl(cl_jobs)
