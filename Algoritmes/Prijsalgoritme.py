import psycopg2
import random

"""
Gemaakt door: Wijnand van Dijk en Richard Jansen.
Wijnand van Dijk: Core code
Richard Jansen: Overzetten naar SQL tabel
"""


def prijs(id,prijs_prod):
    if prijs_prod < 101:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(very_cheap)[0],
                                                                                           random.choice(very_cheap)[0],
                                                                                           random.choice(very_cheap)[0],
                                                                                           random.choice(very_cheap)[0],
                                                                                           random.choice(very_cheap)[0]))
        """
        return [id,random.choice(very_cheap)[0],random.choice(very_cheap)[0], random.choice(very_cheap)[0],random.choice(very_cheap)[0],random.choice(very_cheap)[0]]
    elif 100 < prijs_prod < 251:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(cheap)[0],
                                                                                           random.choice(cheap)[0],
                                                                                           random.choice(cheap)[0],
                                                                                           random.choice(cheap)[0],
                                                                                           random.choice(cheap)[0]))
        """
        return [id,random.choice(cheap)[0], random.choice(cheap)[0], random.choice(cheap)[0], random.choice(cheap)[0], random.choice(cheap)[0]]
    elif 250 < prijs_prod < 501:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(middle)[0],
                                                                                           random.choice(middle)[0],
                                                                                           random.choice(middle)[0],
                                                                                           random.choice(middle)[0],
                                                                                           random.choice(middle)[0]))
        """
        return [id,random.choice(middle)[0], random.choice(middle)[0], random.choice(middle)[0], random.choice(middle)[0], random.choice(middle)[0]]
    elif 500 < prijs_prod < 751:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(expensive)[0],
                                                                                           random.choice(expensive)[0],
                                                                                           random.choice(expensive)[0],
                                                                                           random.choice(expensive)[0],
                                                                                           random.choice(expensive)[0]))
        """
        return [id,random.choice(expensive)[0], random.choice(expensive)[0], random.choice(expensive)[0], random.choice(expensive)[0], random.choice(expensive)[0]]
    elif prijs_prod > 750:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(more_expensive)[0],
                                                                                           random.choice(more_expensive)[0],
                                                                                           random.choice(more_expensive)[0],
                                                                                           random.choice(more_expensive)[0],
                                                                                           random.choice(more_expensive)[0]))
        """
        return [id,random.choice(more_expensive)[0], random.choice(more_expensive)[0], random.choice(more_expensive)[0], random.choice(more_expensive)[0], random.choice(more_expensive)[0]]


def create_prijs_aanbevelingen():
    cur.execute('DROP TABLE IF EXISTS Prijs_aanbevelingen;')

    cur.execute('CREATE TABLE Prijs_aanbevelingen (id varchar PRIMARY KEY,'
                'PRODUCT1 varchar,'
                'PRODUCT2 varchar,'
                'PRODUCT3 varchar,'
                'PRODUCT4 varchar,'
                'PRODUCT5 varchar);')
    con.commit()


con = psycopg2.connect("user=postgres password=pgadminJTgeest dbname=voordeelshopgpx")
cur = con.cursor()

cur.execute("select id, selling_price from product where selling_price < 101")
very_cheap = cur.fetchall()

cur.execute("select id, selling_price from product where selling_price > 100 and selling_price < 251")
cheap = cur.fetchall()

cur.execute("select id, selling_price from product where selling_price > 250 and selling_price < 501")
middle = cur.fetchall()

cur.execute("select id, selling_price from product where selling_price > 500 and selling_price < 751")
expensive = cur.fetchall()

cur.execute("select id, selling_price from product where selling_price > 750")
more_expensive = cur.fetchall()

create_prijs_aanbevelingen()

cur.execute("select id,selling_price from product")
id_price = cur.fetchall()

for id in id_price:
    recids = prijs(id[0],id[1])
    print(recids[0])
    try:
        cur.execute("INSERT INTO Prijs_aanbevelingen (id, PRODUCT1, PRODUCT2, PRODUCT3, PRODUCT4, PRODUCT5) VALUES ( %s, %s, %s, %s,%s,%s)",(recids[0], recids[1], recids[2], recids[3], recids[4],recids[5]))
    except:
        print("error", recids)

con.commit()
