CLHunter is a app that scrapes Craigslist and posts results onto your Slack.
Without the API Token, it'll post there results in your CLI.

You can get your slack api token at:
https://get.slack.help/hc/en-us/articles/215770388

App created by Ross Kwong (rosskwong@gmail.com)


To get the application started
1. run `install.sh` to install the necessary python packages. 
2. Activate your python virtua env with command: 'source venv/bin/activate'
3. Run the command: 'python main.py'

You can configure the settings.py in the lib folder to fit your criteria. You'll
also need a Slack API token if you want it to post notifications into your slack
channel. 

To do this, you will need to create a file called 'slackapitoken.py'
and set a variable called 'SLACK_API_TOKEN=(YourAPITokenHere)'
