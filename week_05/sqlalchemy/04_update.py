'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''


import sqlalchemy as sqa

DATABASE_URI = f'postgres+psycopg2://ak@localhost:5432/dvdrental'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqa.update(film).values(rental_duration=10).where(film.columns.length > 150)
# query = query.where(film.columns.Id == 1)
results = connection.execute(query)

result = connection.execute(query)