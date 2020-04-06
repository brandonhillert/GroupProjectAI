import psycopg2
from pymongo import MongoClient
import random

"""
Opdracht: AI Group project Categorie-Algoritme 2
Author: Brandon Hillert
"""

client = MongoClient('localhost', 27017)

db = client.huwebshop
conn = psycopg2.connect("dbname=voordeelshoponescript user=postgres password=admin")
cur = conn.cursor()


def create_table():
    cur.execute("DROP TABLE IF EXISTS categorie_algoritme;")

    cur.execute('CREATE TABLE categorie_algoritme ('
                'prod_id varchar PRIMARY KEY,'
                'prod1 varchar,'
                'prod2 varchar,'
                'prod3 varchar,'
                'prod4 varchar,'
                'prod5 varchar);')
    conn.commit()


def categorie_algoritme(product, categorie):
    # def fill_table():

    cur.execute("SELECT id FROM product"
                " WHERE catergory_idcatergory = {} AND id != '{}'".format(categorie, product)
                )
    lijst = cur.fetchall()

    lijst_producten = []
    for i in lijst:
        list(i)
        lijst_producten.append(i[0])


    """" 
    Even kijken wat ik kan doen om een lijst met 0 product bijvoorbeeld te vullen
    """
    if len(lijst_producten) < 10:
        print(len(lijst_producten))
    else:
        random_waarde = random.randint(0, (len(lijst_producten) - 1))
        prod1 = lijst_producten[random_waarde]

        random_waarde = random.randint(0, (len(lijst_producten) - 1))
        prod2 = lijst_producten[random_waarde]

        random_waarde = random.randint(0, (len(lijst_producten) - 1))
        prod3 = lijst_producten[random_waarde]

        random_waarde = random.randint(0, (len(lijst_producten) - 1))
        prod4 = lijst_producten[random_waarde]

        random_waarde = random.randint(0, (len(lijst_producten) - 1))
        prod5 = lijst_producten[random_waarde]

        return print(product, prod1, prod2, prod3, prod4, prod5)


def fill_prod_id():
    cur.execute('SELECT id,catergory_idcatergory FROM product')
    lijst_producten = cur.fetchall()

    for ids in lijst_producten:
        product = list(ids)

        if product[0] == "38647-It'sglowtime":
            product[0] = "38647-It''sglowtime"

        # categorie_algoritme(product[0], product[1])

        categorie_algoritme(product[0], product[1])

        try:
            """
            hier moet een insert statement komen die de waardes uit categorie algoritme in 1x de db in pompt
            
            """
            cur.execute('INSERT INTO categorie_algoritme(prod_id)'
                        'VALUES ({})'.format(product[0]))
        except:
            print(print("error"), product[0])
        conn.commit()


create_table()
fill_prod_id()
