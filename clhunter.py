from craigslist import CraigslistHousing
from slackclient import SlackClient
import time
import settings

class CLHunter:
    sc = SlackClient(settings.SLACK_TOKEN)

  cl_housing = CraigslistHousing(site='vancouver', area='van', category='apa', 
          filters={'max_price': 4200})


    def in_aoi(coords, box):
        if coords is not None and \
            box[0][0] < coords[0] < box[1][0] and \
            box[1][1] < coords[1] < box[0][1]:
            return True
        return False

    for result in cl_housing.get_results(sort_by='newest', geotagged=True):
        geotag = result["geotag"]
        area_found = False
        area = ""
        for a, coords in AREAS_OF_INTEREST.items():
            if in_aoi(geotag, coords):
                area = a
                area_found = True

        # location = result["where"]
        # for hood in NEIGHBORHOODS:
        #     if location is not None and hood in location.lower():
        #             area_found = True
        #             area = hood
        
        try:
            desc = "{0} | {1} | {2} | <{3}>".format(result["price"], \
                result["name"], area, result["url"])
        except UnicodeEncodeError:
            print result["url"]

        if area_found:
            print "Found one! \n" + desc
            sc.api_call( "chat.postMessage", channel=SLACK_CHANNEL, text=desc,
                    username='Hal-2000')
