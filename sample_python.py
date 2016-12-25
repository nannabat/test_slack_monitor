#!/bin/python
import os
from slackclient import SlackClient

#slack_token = os.environ["xoxb-121355730919-9IEodFmVZVwsgOV4GP7yh4F7"]
sc = SlackClient("xoxb-121355730919-9IEodFmVZVwsgOV4GP7yh4F7")

response = sc.api_call(
  "chat.postMessage",
  channel="#oncall_alerts",
  #text="Hello from Python! :tada:"
  text = "This is my perfect message",
  username = 'ops_bot',
  as_user = "true"
)

print response['ok']
message_delivered = response['ok']

if message_delivered == True:
  print "message delivered"

print response
