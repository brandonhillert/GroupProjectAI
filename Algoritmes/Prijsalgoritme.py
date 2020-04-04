import psycopg2
import random


def prijs(id,prijs_prod):
    #prijs_prod = int(input("Geef de prijs van het product: "))
    #prijs_prod = 100
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

    cur.execute('CREATE TABLE Prijs_aanbevelingen (Prod_id varchar PRIMARY KEY,'
                'PROD1 varchar,'
                'PROD2 varchar,'
                'PROD3 varchar,'
                'PROD4 varchar,'
                'PROD5 varchar);')
    con.commit()

con = psycopg2.connect("dbname=voordeelshoponescript user=postgres password=kip")
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
        cur.execute("INSERT INTO Prijs_aanbevelingen (Prod_id, PROD1, PROD2, PROD3, PROD4,PROD5) VALUES ( %s, %s, %s, %s,%s,%s)",(recids[0], recids[1], recids[2], recids[3], recids[4],recids[5]))
    except:
        print("error", recids)

con.commit()
