import sqlalchemy as sqa
# from secrets import username, password
from pprint import pprint

DATABASE_URI = f'postgres+psycopg2://ak@localhost:5432/dvdrental' #Always create db in pgAdmin

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

test = sqa.Table('test', metadata,
                 sqa.Column('id', sqa.Integer(), autoincrement=True, primary_key=True),
                 sqa.Column('year', sqa.Integer()),
                 sqa.Column('quote', sqa.String(144),nullable=False),
                )

metadata.create_all(engine)

query = sqa.insert(test).value(

)