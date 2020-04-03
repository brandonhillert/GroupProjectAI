import psycopg2
from pymongo import MongoClient
import random

"""
Opdracht: AI Group project Categorie-Algoritme
Author: Brandon Hillert
"""

client = MongoClient('localhost', 27017)

db = client.huwebshop
conn = psycopg2.connect("dbname=voordeelshoponescript user=postgres password=admin")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS categorie_algoritme;")

cur.execute("CREATE TABLE categorie_algoritme( id serial NOT NULL,"
            "id_product varchar(45),"
            "id_categorie varchar(45),"
            "id_product_1 varchar(45),"
            "id_product_2 varchar(45),"
            "id_product_3 varchar(45),"
            "CONSTRAINT categorie_algoritme_pk PRIMARY KEY (id)"
            "  ) WITH ("
            "   OIDS=FALSE"
            ");")

cur.execute("INSERT INTO categorie_algoritme(id_product, id_categorie)"
            "SELECT id, catergory_idcatergory FROM product"
            " ORDER BY id")

cur.execute("SELECT id_product,id_categorie FROM categorie_algoritme")
lijst_producten = cur.fetchall()

"""
Vanaf hieronder heb ik gister avond gemaakt
Moet eigenlijk wel efficienter
"""

count = 0

# Loopt door alle waardes die er zijn
for product in lijst_producten:
    product = list(product)

    if product[0] == "38647-It'sglowtime":
        product[0] = "38647-It''sglowtime"


    # selecteerd per product alle items waar de idcategorie gelijk aan is, maar het id wel verschillend
    cur.execute(
        "SELECT id_product,id_categorie FROM categorie_algoritme"
        " WHERE id_categorie = '{}' AND id_product != '{}' ".format(product[1], product[0])
    )
    lijst = cur.fetchall()

    try:
        # kiest een random waarde uit die lijst
        random_waarde = random.randint(0, (len(lijst) - 1))
        random_product = lijst[random_waarde]

        # Resultaat is het random gekozen product
        cur.execute(
            "UPDATE categorie_algoritme SET id_product_1 = '{}' WHERE id = '{}';".format(random_product[0], product[1]))

    except:
        print("Error")

    count += 1
    if count % 1000 == 0:
        print(count, "producten")

print("done with producten")
conn.commit()