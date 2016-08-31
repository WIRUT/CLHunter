def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
load_src("settings", "settings.py")
from craigslist import CraigslistHousing
from slackclient import SlackClient
import time
import settings

try:
    sc = SlackClient(settings.SLACK_TOKEN)
except AttributeError:
    sc = None

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
        for a, coords in settings.AREAS_OF_INTEREST.items():
            if area_in_bounds(geotag, coords):
                area = a
                area_found = True
    return (area_found, area);


def in_neighborhood(location):
    area = None
    area_found = False
    for hood in settings.NEIGHBORHOODS:
        if location is not None and hood in location.lower():
            area_found = True
            area = hood
    return (area_found, area);


def cl_info_parser(area, result):
    desc = None
    try:
        desc = "{0} | {1} | {2} | <{3}>".format(result["price"], \
            result["name"], area, result["url"])
    except UnicodeEncodeError:
        print "UnicodeEncodeError for url:{}".format(result["url"])
    return desc


def post_to_slack(description):
    if description is not None and sc is not None:
        sc.api_call( "chat.postMessage", channel=settings.SLACK_CHANNEL, 
                text=description, username='Hal-2000')
    elif sc is None:
        print description
    else:
        print("Error. Nothing to post.")


def cl_hunt_result(cl_housing):
    for result in cl_housing.get_results(sort_by='newest', geotagged=True):
        geotag = result["geotag"]
        aoi_tuple = in_area_of_interest(geotag) 
        aoi_found = aoi_tuple[0]
        if aoi_found is False:
            location = result["where"]
            aoi_found = in_neighborhood(location)
        if aoi_found is True:
            area = aoi_tuple[1]
            description = cl_info_parser(area, result)
            post_to_slack(description)


def start_cl_house_hunt():
    cl_housing = CraigslistHousing(
                                    site=settings.SITE,
                                    area=settings.AREA,
                                    category=settings.CATEGORY, 
                                    filters={'min_price': settings.MIN_PRICE, 
                                             'max_price': settings.MAX_PRICE}
            )
    if sc is None:
        print "\nSlack Token is missing. Displaying results in command-line:\n"
    result = cl_hunt_result(cl_housing)
