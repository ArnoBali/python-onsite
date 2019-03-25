'''
Create a slack API token for the codingnomads workspace.

Using the slackclient package, fetch all comments that include links
from the python-resources channel.

Store the links in a JSON file that has the following form:
[
    {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
    # next link item
]

We will continue to work with this data throughout the week, so make sure to complete it!
https://slack.dev/python-slackclient/
'''

from secrets import tokens

import pprint
import time

from slackclient import SlackClient

slack_token = tokens["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_token)

python_resources = sc.api_call("conversations.history", channel="CGUDWETHR")

messages = python_resources['messages']

# pprint.pprint(messages[1]['attachments'])

# for m in range(len(messages)):
#
#     try:
#         msg = messages[m]['attachments'][0]['from_url']
#         print(msg)
#
#     except Exception as error:
#         pass
#         # print('Caught this error: ' + repr(error))


#-----------------------------------------------------------------------------------------------------
# 1. Create list
# 2. Create dict
# 3. Map messages' attributes to dict
# 4. Write list with attributes as dictionaries into Json file
#

msg_list = []

for m in range(len(messages)):

    msg_dict = {}

    try:
        msg_dict["link"] = messages[m]['attachments'][0]['from_url']
    except Exception as error:
        # msg_dict["link"] = None
        continue

    try:
        msg_dict["description"] = messages[m]['attachments'][0]['title']
    except Exception as error:
        msg_dict["description"] = None
        pass

    try:
        msg_dict["date_added"] = time.ctime(int(float(messages[m]['ts'])))
    except Exception as error:
        msg_dict["date_added"] = None
        pass

        msg_dict["read"] = False # defaults to False, change to True if you read it
        msg_dict["rating"] = 0   # on a scale from 1-10, initially 0

    try:
        msg_dict["comments"] = messages[m]['attachments'][0]['text']
    except Exception as error:
        msg_dict["comments"] = None
        pass
        msg_dict["starred"] = False # defaults to False, change to True if you think it's great

    msg_list.append(msg_dict)

print(msg_list)

import json
with open('data.json', 'w') as outfile:
    json.dump(msg_list, outfile, sort_keys=True, indent=4, separators=(',', ':'))


# msg_list = []
#
# for m in range(len(messages)):
#
#     try:
#         msg_list.append({
#             "link": messages[m]['attachments'][0]['from_url'],
#             "description": messages[m]['attachments'][0]['title'],
#             "date_added": time.ctime(int(float(messages[m]['ts']))),
#             "read": False,  # defaults to False, change to True if you read it
#             "rating": 0,  # on a scale from 1-10, initially 0
#             "comments": [messages[m]['attachments'][0]['text']],
#             "starred": False # defaults to False, change to True if you think it's great
#         })
#
#     except Exception as error:
#         pass
#
# pprint.pprint(msg_list)
#
# import json
# with open('data.json', 'w') as outfile:
#     json.dump(msg_list, outfile)