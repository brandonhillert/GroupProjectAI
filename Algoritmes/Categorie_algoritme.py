import psycopg2
from pymongo import MongoClient
import random

"""
Opdracht: AI Group project Categorie-Algoritme 2
Author: Brandon Hillert
Definitieve versie Categorie Algoritme
"""

client = MongoClient('localhost', 27017)

db = client.huwebshop
conn = psycopg2.connect("user=postgres password=pgadminJTgeest dbname=voordeelshopgpx")
cur = conn.cursor()


def create_table():
    cur.execute("DROP TABLE IF EXISTS categorie_algoritme;")
    cur.execute('CREATE TABLE categorie_algoritme ('
                'id varchar PRIMARY KEY,'
                'product1 varchar,'
                'product2 varchar,'
                'product3 varchar,'
                'product4 varchar,'
                'product5 varchar);')
    conn.commit()


def categorie_algoritme(product, categorie):
    #Query die alle ids ophaalt waar die id != product en category_idcatergory = categorie
    cur.execute("SELECT id FROM product"
                " WHERE category_idcategory = {} AND id != '{}'".format(categorie, product)
                )
    lijst = cur.fetchall()

    #Stopt alle id's in een lijst, en haalt daar 5 willekeurige waardes uit
    lijst_producten = []
    for i in lijst:
        list(i)
        lijst_producten.append(i[0])

    if len(lijst_producten) < 5:
        return [product, product, product, product, product, product]
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

        return [product, prod1, prod2, prod3, prod4, prod5]


def fill_table():
    cur.execute('SELECT id, category_idcategory FROM product')
    lijst_producten = cur.fetchall()

    count = 0

    for ids in lijst_producten:
        product = list(ids)

        if product[0] == "38647-It'sglowtime":
            product[0] = "38647-It''sglowtime"

        lijst_prods = categorie_algoritme(product[0], product[1])

        try:
            cur.execute("INSERT INTO categorie_algoritme(id, product1, product2, product3, product4, product5)"
                        "VALUES ('{}','{}','{}','{}','{}','{}')".format(lijst_prods[0], lijst_prods[1], lijst_prods[2],
                                                                        lijst_prods[3], lijst_prods[4], lijst_prods[5]))
        except:
            print(product[0], product[1])
        conn.commit()

        count += 1
        if count % 1000 == 0:
            print(count, "producten")

    print("Producten zijn ingeladen")


create_table()
fill_table()
