from clhunter import start_cl_hunt 
import time
import os


if __name__== '__main__':
    print("{}: Starting Craigslist Scrap".format(time.ctime()))
    try:
        start_cl_hunt()
    except KeyboardInterrupt:
        print("\nExiting...")
    else:
        print("{}: Scraping complete".format(time.ctime()))
    
