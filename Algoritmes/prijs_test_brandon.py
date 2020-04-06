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


        print(product, prod1, prod2, prod3, prod4, prod5)



def fill_prod_id():
    cur.execute('SELECT id,catergory_idcatergory FROM product')
    lijst_producten = cur.fetchall()

    for ids in lijst_producten:
        product = list(ids)

        if product[0] == "38647-It'sglowtime":
            product[0] = "38647-It''sglowtime"

        categorie_algoritme(product[0], product[1])

        # Hier komt een insert statement met categorie als format [product, prod1, prod2, prod3, prod4, prod5]

fill_prod_id()
