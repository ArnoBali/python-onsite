'''
Insert a new record in the film table.

'''

import sqlalchemy as sqa
from pprint import pprint

DATABASE_URI = f'postgres+psycopg2://ak@localhost:5432/dvdrental'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

actor = sqa.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqa.insert(film).values(title='het zakmes', description="Het Zakmes is een Nederlandse kinderfilm uit 1992, geregisseerd door Ben Sombogaart. Het is gebaseerd op het boek van Sjoerd Kuyper. De hoofdrollen zijn voor Olivier Tuinier, Verno Romney, Genio de Groot en Adelheid Roosen. In 2018 is de film helemaal opnieuw ingekleurd en komt deze opnieuw in de bioscoop.", language_id=1,release_year=1992, length=90)
result_proxy = connection.execute(query)