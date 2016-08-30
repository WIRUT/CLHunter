class ErrorMsg:
    def importErrorMsg(self):
        msg = \
        "\nOops! You don't have the module 'privateslackdetail.py' that " \
        "Craigslist Hunter requres.\nPlease visit: "\
        "'https://get.slack.help/hc/en-us/articles/215770388'\n" \
        "on how to issue a new API Token from Slack.\n"                     
        return msg

    def missingFileErrorMsg(self):
        msg = "\nMissing file containg Slack API Token\n"
        return msg
