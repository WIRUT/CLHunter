from craigslist import CraigslistHousing
from slackclient import SlackClient
import time

SLACK_TOKEN = "xoxp-20539905617-20540944710-73838868212-1c49726c56"
SLACK_CHANNEL = "#general"

sc = SlackClient(SLACK_TOKEN)

AREAS_OF_INTEREST = {
        "False_Creek": [
            [-123.137984,49.2652],
            [-123.097472,49.279425],
            # [-123.14558,49.263607],
            # [-123.095831,49.280292],
            ],
        "New Westminster": [
            [-122.9202532768,49.1996605132],
            [-122.8999114037,49.2080022935],
            ],
}

NEIGHBORHOODS = ["False Creek", "Downtown", "Kitsilano", "Mount Pleasant"]
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

    location = result["where"]
    for hood in NEIGHBORHOODS:
        if location is not None and hood in location.lower():
                area_found = True
                area = hood
    
    try:
        desc = "{0} | {1} | {2} | <{3}>".format(result["price"], \
            result["name"], area, result["url"])
    except UnicodeEncodeError:
        print result["url"]

    if area_found:
        print "Found one! \n" + desc
        sc.api_call( "chat.postMessage", channel=SLACK_CHANNEL, text=desc,
                username='Hal-2000')
