#!/bin/python
import os
from slackclient import SlackClient

#slack_token = os.environ["xoxb-121355730919-9IEodFmVZVwsgOV4GP7yh4F7"]
sc = SlackClient("xoxb-121355730919-8oFqlfd751dfxhK0j9Q9Rax8")
attachments_var = [{
            "text": "Choose a game to play",
            "fallback": "You are unable to choose a game",
            "callback_id": "wopr_game",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "chess",
                    "text": "Chess",
                    "type": "button",
                    "value": "chess"
                },
                {
                    "name": "maze",
                    "text": "Falken's Maze",
                    "type": "button",
                    "value": "maze"
                },
                {
                    "name": "war",
                    "text": "Thermonuclear War",
                    "style": "danger",
                    "type": "button",
                    "value": "war",
                    "confirm": {
                        "title": "Are you sure?",
                        "text": "Wouldn't you prefer a good game of chess?",
                        "ok_text": "Yes",
                        "dismiss_text": "No"
                    }
                }
            ]
        }]

response = sc.api_call(
  "chat.postMessage",
  channel="#oncall_alerts",
  #text="Hello from Python! :tada:"
  text = "This is my perfect message",
  attachments = attachments_var,
  username = 'ops_bot',
  as_user = "true"
)

print response['ok']
message_delivered = response['ok']

if message_delivered == True:
  print "message delivered"

print response
