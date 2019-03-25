'''

All of the following exercises should be done using sqlalchemy.

Using the dvdrental schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy as sqa
from pprint import pprint

DATABASE_URI = f'postgres+psycopg2://ak@localhost:5432/dvdrental'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

actor = sqa.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)
category = sqa.Table('category', metadata, autoload=True, autoload_with=engine)

#query = sqa.select([actor])
query1 = sqa.select([film, category])
query2 = sqa.select([film])

result_proxy1 = connection.execute(query1)
result_set1 = result_proxy1.fetchall()
result_proxy2 = connection.execute(query2)
result_set2 = result_proxy2.fetchall()
# result_set = result_proxy.fetchmany(10)

pprint(result_set1)
pprint(result_set2)

