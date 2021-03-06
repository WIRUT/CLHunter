from clhousehunter import start_cl_house_hunt
from cljobhunter import start_cl_job_hunt
import settings
import time
import traceback
import sys
import os


if __name__== '__main__':
    while True:
        print("{}: Starting Craigslist Scrap".format(time.ctime()))
        try:
            if settings.HUNT_APT:
                start_cl_house_hunt()
            if settings.HUNT_JOB:
                start_cl_job_hunt()
        except KeyboardInterrupt:
            print("\nExiting...")
        except Exception as exc:
            print ("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Scraping complete".format(time.ctime()))
        time.sleep(settings.SLEEP_INTERVAL) 
