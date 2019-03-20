my_list = []

my_list.append({'hello': 3})

# print(my_list)
# print(my_list[0])
# print(my_list[0]['hello'])


from secrets import tokens

import pprint
import time


from slackclient import SlackClient

slack_token = tokens["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_token)

python_resources = sc.api_call("conversations.history", channel="CGUDWETHR")

messages = python_resources['messages']

# pprint.pprint(python_resources)
# pprint.pprint(messages)
ts = time.ctime(int(float(messages[5]['ts'])))

print(ts)


# pprint.pprint(messages[5]['attachments'][0]['title'])
# print(type(messages[5]['attachments'][0]['text']))

