'''

Building on the example more_APIs/00_slack, make a new database with two tables to model this object:

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
}

Think about what tables are required to model this object. Do you need two tables? Three?

Now, instead of saving the list of these objects to a JSON file, persist the data
to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Table, DateTime, ForeignKey, Text, Boolean
import json
import pprint


DATABASE_URI = f'postgres+psycopg2://ak@localhost:5432/slack_db'

engine = db.create_engine(DATABASE_URI, echo=True)
connection = engine.connect()
metadata = db.MetaData()


# test = Table('post', metadata,
#             Column('id', Integer(), autoincrement=True, primary_key=True),
#             Column('description', String(255), nullable=False),
#             Column('link', String(255), nullable=False),
#             Column('date_added', DateTime),
#             )
#
# t2 = Table('post_read', metadata,
#             Column('id', Integer(), autoincrement=True, primary_key=True),
#             Column('read', Boolean(), default=False),
#             Column('rating', Integer(), default=0),
#             Column('comments', Text()),
#             Column('starred', Boolean(), default=False),
#             Column('id_post', Integer(), ForeignKey("post.id"))
#             )
#
# metadata.create_all(engine)

with open('data.json', 'r') as f:
    slack_posts = json.load(f)

# pprint.pprint(slack_posts)

post = Table('post', metadata, autoload=True, autoload_with=engine)
post_read = Table('post_read', metadata, autoload=True, autoload_with=engine)

# query1 = db.insert(post)
# new_records = slack_posts
# result_proxy1 = connection.execute(query1, new_records)
#
# query2 = db.insert(post_read)
# new_records = slack_posts
# result_proxy2 = connection.execute(query2, new_records)



for p in slack_posts:
    query_post = db.insert(post).values(description=p['description'],
                                        link=p['link'],
                                        date_added=p['date_added']
                                        )

    query_post_read = db.insert(post_read).values(read=p['read'],
                                                  rating=p['rating'],
                                                  comments=p['comments'],
                                                  starred=p['starred']
                                                  )

    result_proxy = connection.execute(query_post)
    result_proxy2 = connection.execute(query_post_read)


