from err.errormsg import * 
try:
    import slackapitoken
    # SLACK_TOKEN = slackapitoken.SLACK_TOKEN
except ImportError:
    print ErrorMsg().importErrorMsg() 
    SLACK_TOKEN = None 


# Modify the variables below:
SLACK_CHANNEL = "#general"
MIN_PRICE = 500
MAX_PRICE = 1500
AREA = 'van'
SITE = 'vancouver'
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
