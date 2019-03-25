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


DATABASE_URI = f'postgres+psycopg2://ak@localhost:5432/slack_db'

engine = db.create_engine(DATABASE_URI, echo=True)
connection = engine.connect()
metadata = db.MetaData()


test = Table('test', metadata,
            Column('id', Integer(), autoincrement=True, primary_key=True),
            Column('quote', String(255), nullable=False),
            Column('year', Integer()),
            Column('greatness', SmallInteger())
            )

t2 = Table('t2', metadata,
            Column('id', Integer(), autoincrement=True, primary_key=True),
            Column('quote', String(255), nullable=False),
            Column('year', Integer()),
            Column('greatness', SmallInteger())
            )


metadata.create_all(engine)

