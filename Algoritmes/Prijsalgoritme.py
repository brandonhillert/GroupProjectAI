import psycopg2
import random

"""
Gemaakt door: Wijnand van Dijk en Richard Jansen.
Wijnand van Dijk: Core code
Richard Jansen: Overzetten naar SQL tabel
Brandon Hillert: Functionele decompositie
"""

con = psycopg2.connect("dbname=voordeelshoponescript user=postgres password=admin")
cur = con.cursor()

"""
Globale variabelen voor een snellere werking van het programma
"""

cur.execute("SELECT id, selling_price FROM product WHERE selling_price < 101")
very_cheap = cur.fetchall()

cur.execute("SELECT id, selling_price FROM product WHERE selling_price > 100 and selling_price < 251")
cheap = cur.fetchall()

cur.execute("SELECT id, selling_price FROM product WHERE selling_price > 250 and selling_price < 501")
middle = cur.fetchall()

cur.execute("SELECT id, selling_price FROM product WHERE selling_price > 500 and selling_price < 751")
expensive = cur.fetchall()

cur.execute("SELECT id, selling_price FROM product WHERE selling_price > 750")
more_expensive = cur.fetchall()

"""
Functie voor het aanmaken Postgres DB tabel
"""


def create_prijs_aanbevelingen():
    cur.execute('DROP TABLE IF EXISTS Prijs_aanbevelingen;')
    cur.execute('CREATE TABLE Prijs_aanbevelingen (id varchar PRIMARY KEY,'
                'PRODUCT1 varchar,'
                'PRODUCT2 varchar,'
                'PRODUCT3 varchar,'
                'PRODUCT4 varchar,'
                'PRODUCT5 varchar);')
    con.commit()


"""" 
In deze functie wordt bepaald in welke prijsklasse het product hoor,
en keert daarna 5 random waardes terug ui die prijsklasse
"""


def prijs(id, prijs_prod):
    if prijs_prod < 101:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(very_cheap)[0],
                                                                                           random.choice(very_cheap)[0],
                                                                                           random.choice(very_cheap)[0],
                                                                                           random.choice(very_cheap)[0],
                                                                                           random.choice(very_cheap)[0]))
        """
        return [id, random.choice(very_cheap)[0], random.choice(very_cheap)[0], random.choice(very_cheap)[0],
                random.choice(very_cheap)[0], random.choice(very_cheap)[0]]
    elif 100 < prijs_prod < 251:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(cheap)[0],
                                                                                           random.choice(cheap)[0],
                                                                                           random.choice(cheap)[0],
                                                                                           random.choice(cheap)[0],
                                                                                           random.choice(cheap)[0]))
        """
        return [id, random.choice(cheap)[0], random.choice(cheap)[0], random.choice(cheap)[0], random.choice(cheap)[0],
                random.choice(cheap)[0]]
    elif 250 < prijs_prod < 501:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(middle)[0],
                                                                                           random.choice(middle)[0],
                                                                                           random.choice(middle)[0],
                                                                                           random.choice(middle)[0],
                                                                                           random.choice(middle)[0]))
        """
        return [id, random.choice(middle)[0], random.choice(middle)[0], random.choice(middle)[0],
                random.choice(middle)[0], random.choice(middle)[0]]
    elif 500 < prijs_prod < 751:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(expensive)[0],
                                                                                           random.choice(expensive)[0],
                                                                                           random.choice(expensive)[0],
                                                                                           random.choice(expensive)[0],
                                                                                           random.choice(expensive)[0]))
        """
        return [id, random.choice(expensive)[0], random.choice(expensive)[0], random.choice(expensive)[0],
                random.choice(expensive)[0], random.choice(expensive)[0]]
    elif prijs_prod > 750:
        """
        print("Uw aanbevolen producten inclusief de prijzen zijn {} {} {} {} en {}".format(random.choice(more_expensive)[0],
                                                                                           random.choice(more_expensive)[0],
                                                                                           random.choice(more_expensive)[0],
                                                                                           random.choice(more_expensive)[0],
                                                                                           random.choice(more_expensive)[0]))
        """
        return [id, random.choice(more_expensive)[0], random.choice(more_expensive)[0],
                random.choice(more_expensive)[0], random.choice(more_expensive)[0], random.choice(more_expensive)[0]]


"""
Deze tabel zorgt ervoor dat alle waardes worden ingeladen
Maakt gebruikt van prijs() om te bepalen wat er in komt
"""


def fill_table():
    create_prijs_aanbevelingen()

    cur.execute("select id,selling_price from product")
    id_price = cur.fetchall()

    counter = 0

    for id in id_price:
        recids = prijs(id[0], id[1])

        try:
            cur.execute(
                "INSERT INTO Prijs_aanbevelingen (id, PRODUCT1, PRODUCT2, PRODUCT3, PRODUCT4, PRODUCT5) VALUES ( %s, %s, %s, %s,%s,%s)",
                (recids[0], recids[1], recids[2], recids[3], recids[4], recids[5]))
        except:
            print("error", recids)

        counter += 1
        if counter % 1000 == 0:
            print(counter, "/34000 producten zijn ingeladen")

    print("Table filled")

    con.commit()


def main_loop():
    create_prijs_aanbevelingen()
    fill_table()
    cur.close()


main_loop()
