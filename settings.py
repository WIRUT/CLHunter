from err.errormsg import * 
try:
    import slackapitokens
    SLACK_TOKEN = slackapitoken.SLACK_TOKEN
except ImportError:
    print ErrorMsg().importErrorMsg() 
    SLACK_TOKEN = None 


# Modify the variables below:
SLACK_CHANNEL = "#general"
MIN_PRICE = 0
MAX_PRICE = 1500
AREA = 'van'
SITE = 'vancouver'
CATEGORY = 'apa'


AREAS_OF_INTEREST = {
        "False_Creek": [
            [-123.137984,49.2652],
            [-123.097472,49.279425],
            ],
        "New Westminster": [
            [-122.9202532768,49.1996605132],
            [-122.8999114037,49.2080022935],
            ],
}

NEIGHBORHOODS = ["False Creek", "Downtown", "Kitsilano", "Mount Pleasant"]
