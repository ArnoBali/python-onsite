import sqlalchemy as sqa
# from secrets import username, password
from pprint import pprint

DATABASE_URI = f'postgres+psycopg2://ak@localhost:5432/dvdrental'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

actor = sqa.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqa.Table('film_actor', metadata, autoload=True, autoload_with=engine)

#query = sqa.select([actor])
query = sqa.select([actor]).where(actor.columns.first_name == 'Penelope')
print(query)
print(type(query))


result_proxy = connection.execute(query)
#result_set = result_proxy.fetchall()
result_set = result_proxy.fetchmany(10)

#print(actor.columns.keys())
pprint(result_set)

    # SELECT a.first_name, a.last_name, f.title
    # FROM actor as a
    # JOIN film_actor as fa
    # ON a.actor_id = fa.actor_id
    # JOIN film as f
    # ON f.film_id = fa.film_id;

print(actor.columns.keys())
pprint(repr(metadata.tables['actor']))
