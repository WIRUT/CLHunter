def load_src(name,fpath):
    import os, imp
    try:
        return imp.load_source(name, 
                os.path.join(os.path.dirname(__file__), fpath))
    except IOError:
        print "Filename: '{}' is missing.".format(fpath)
        return None
try:
    load_src("slackapitoken", "slackapitokens.py")
    import slackapitoken
    SLACK_TOKEN = slackapitoken.SLACK_TOKEN
except ImportError:
    print "Missing SLACK_TOKEN. Displaying results in command-line."
    SLACK_TOKEN = None 



###############################################################################
#                           Modifiable Variables                              #
###############################################################################

HUNT_JOB = False
HUNT_APT = True


########################## Housing Configurations #############################
SLACK_CHANNEL = "#general"
MIN_PRICE = 500
MAX_PRICE = 1500
AREA = 'cal'
SITE = 'calgary'
CATEGORY = 'apa'


# Coordinates from BoundingBox(http://boundingbox.klokantech.com/)
AREAS_OF_INTEREST = {
        "False_Creek": [
            [49.2652, -123.137984],
            [49.279425, -123.097472],
            ],
        "New Westminster": [
            [49.1996605132, -122.9202532768],
            [49.2080022935, -122.8999114037],
            ],
        "Brentwood": [
            [49.2593048154, -123.0172204971],
            [49.2681825938, -122.9988956451],
            ],
#         "All of Vancouver" : [
#             [49.263268,-123.149872],
#             [49.293281,-123.09906]
#             ],
}

NEIGHBORHOODS = ["False Creek", "Downtown", "Kitsilano", "Mount Pleasant"]
