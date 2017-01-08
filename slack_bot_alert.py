#!/bin/python
import os
from slackclient import SlackClient

def get_slack_token():
   tkn_file_h = open('slack_token.txt','r')
   tkn= tkn_file_h.readline().rstrip()
   return tkn



def send_alert_to_slack():
    token = get_slack_token()
       

    #slack_token = os.environ["xoxb-121355730919-9IEodFmVZVwsgOV4GP7yh4F7"]
    sc = SlackClient(token)
    # attachments_var = [{
    #             "text": "Choose a game to play",
    #             "fallback": "You are unable to choose a game",
    #             "callback_id": "wopr_game",
    #             "color": "#3AA3E3",
    #             "attachment_type": "default",
    #             "actions": [
    #                 {
    #                     "name": "chess",
    #                     "text": "Chess",
    #                     "type": "button",
    #                     "value": "chess"
    #                 },
    #                 {
    #                     "name": "maze",
    #                     "text": "Falken's Maze",
    #                     "type": "button",
    #                     "value": "maze"
    #                 },
    #                 {
    #                     "name": "war",
    #                     "text": "Thermonuclear War",
    #                     "style": "danger",
    #                     "type": "button",
    #                     "value": "war",
    #                     "confirm": {
    #                         "title": "Are you sure?",
    #                         "text": "Wouldn't you prefer a good game of chess?",
    #                         "ok_text": "Yes",
    #                         "dismiss_text": "No"
    #                     }
    #                 }
    #             ]
    #         }]
    attachments_var =     [{
 
                "title": "Values of on file httpd.conf have changed on al1_prod_hadoop1",
                "text": "Values changed are ",
                "fields": [
                    {
                        "title": "Priority",
                        "value": "High",
                        "short": "false"
                    }
                ],
                "image_url": "http://my-website.com/path/to/image.jpg",
                "thumb_url": "http://example.com/path/to/thumb.png",
                "footer": "Powering Scientific Discovery Since 1974",
                "footer_icon": "http://www.nersc.gov/assets/Logos/_resampled/CroppedResize130130-NERSClogoslatepmssolid-sm.png",
                "ts": 123456789
            }]

    response = sc.api_call(
      "chat.postMessage",
      channel="#oncall_alerts",
      #text="Hello from Python! :tada:"
      text = "File monitoring alert, ticket INC230134 is created",
      attachments = attachments_var,
      username = 'ops_bot',
      as_user = "true"
    )

    print response['ok']
    message_delivered = response['ok']

    if message_delivered == True:
      print "message delivered"

    print response
