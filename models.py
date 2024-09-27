from database import Base, engine
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


def create_tables():
    Base.metadata.create_all(engine)


class PokemonData(Base):
    __tablename__ = "pokemon_data"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(40))
    type_1 = Column(String(40))
    type_2 = Column(String(40))
    total = Column(Integer)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    sp_atk = Column(Integer)
    sp_def = Column(Integer)
    speed = Column(Integer)
    generation = Column(Integer)
    legendary = Column(Boolean())


# import requests
# import psycopg2
#
# url = "https://coralvanda.github.io/pokemon_data.json"
# response = requests.get(url)
# data = response.json()
#
# conn = psycopg2.connect(
#     dbname="pokemon_data",
#     user="vishal.chaurasiya",
#     password="Password",
#     host="localhost",
#     port="5432"
# )
# cursor = conn.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS pokemon (
#     id SERIAL PRIMARY KEY,
#     number INT UNIQUE,  -- Add UNIQUE constraint on 'number'
#     name TEXT NOT NULL,
#     type1 TEXT,
#     type2 TEXT,
#     total INT,
#     hp INT,
#     attack INT,
#     defense INT,
#     sp_atk INT,
#     sp_def INT,
#     speed INT,
#     generation INT,
#     legendary BOOLEAN
# )
# """)
# conn.commit()
#
# for pokemon in data:
#     try:
#         cursor.execute("""
#         INSERT INTO pokemon (
#             number, name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """, (
#             pokemon['#'],
#             pokemon['Name'],
#             pokemon['Type 1'],
#             pokemon.get('Type 2'),
#             pokemon['Total'],
#             pokemon['HP'],
#             pokemon['Attack'],
#             pokemon['Defense'],
#             pokemon['Sp. Atk'],
#             pokemon['Sp. Def'],
#             pokemon['Speed'],
#             pokemon['Generation'],
#             pokemon['Legendary']
#
#         ))
#         conn.commit()  # Commit after each successful insert
#         print(f"Inserted Pokémon #{pokemon['#']}")
#     except psycopg2.errors.UniqueViolation as e:
#         print(f"Duplicate Pokémon #{pokemon['#']} detected, skipping insertion.")
#
# cursor.close()
# conn.close()
#
# print("Data insertion completed (including handling of duplicates).")

