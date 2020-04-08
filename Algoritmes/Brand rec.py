import psycopg2

"""
Opdracht: AI Group project brand-Algoritme
Author: Julian van der Geest
Definitieve versie Brand Algoritme
Functionele decompositie: Brandon Hillert
"""
connect = psycopg2.connect("user=postgres password=pgadminJTgeest dbname=voordeelshopgpx")
c = connect.cursor()
print("postgres connected")

"""
Functie voor het aanmaken Postgres DB tabel
"""
def create_table():
    c.execute("DROP TABLE IF EXISTS brandalgoritme CASCADE")
    c.execute("CREATE TABLE brandalgoritme (id VARCHAR PRIMARY KEY, "
              "product1 VARCHAR, "
              "product2 VARCHAR, "
              "product3 VARCHAR, "
              "product4 VARCHAR, "
              "product5 VARCHAR);")



""""
Functie die een lijst met alle mogelijke producten ophaalt die dezelfde brand hebben
Vervolgens kiest de functie 5 waardes uit
Met een insert into statement wordt de data ingeladen
"""
def brand_recommendation(productid, brandid):
    c.execute("SELECT id FROM product"
              " WHERE brand_idbrand = {} AND id != '{}'".format(brandid, productid)
              )
    lijst_mogelijkheden = c.fetchall()

    lijst_producten = []
    for i in lijst_mogelijkheden:
        list(i)
        lijst_producten.append(i[0])

    if len(lijst_producten) >= 5:
        c.execute(
            "INSERT INTO brandalgoritme (id, product1, product2, product3, product4, product5) VALUES (%s, %s, %s, %s, %s, %s)",
            (productid, lijst_producten[0], lijst_producten[1], lijst_producten[2], lijst_producten[3],
             lijst_producten[4]))
        connect.commit()

    elif len(lijst_producten) == 4:
        c.execute(
            "INSERT INTO brandalgoritme (id, product1, product2, product3, product4) VALUES ( %s, %s, %s, %s,%s)",
            (productid, lijst_producten[0], lijst_producten[1], lijst_producten[2], lijst_producten[3]))
        connect.commit()

    elif len(lijst_producten) == 3:
        c.execute("INSERT INTO brandalgoritme (id, product1, product2, product3) VALUES ( %s, %s, %s, %s)",
                  (productid, lijst_producten[0], lijst_producten[1], lijst_producten[2]))
        connect.commit()

    elif len(lijst_producten) == 2:
        c.execute("INSERT INTO brandalgoritme (id, product1, product2) VALUES ( %s, %s, %s)",
                  (productid, lijst_producten[0], lijst_producten[1]))
        connect.commit()

    elif len(lijst_producten) == 1:
        c.execute("INSERT INTO brandalgoritme (id, product1) VALUES ( %s, %s)", (productid, lijst_producten[0]))
        connect.commit()

    elif len(lijst_producten) == 0:
        c.execute("INSERT INTO brandalgoritme (id) VALUES ('{}')".format(productid))
        connect.commit()
    return


"""
Deze tabel zorgt ervoor dat alle waardes worden ingeladen
Maakt gebruikt van prijs() om te bepalen wat er in komt
"""
def fill_table():
    c.execute("select id, brand_idbrand from product")
    producten_lijst = c.fetchall()

    counter = 0

    for product in producten_lijst:

        product_id = product[0]
        brand_id = product[1]

        if product_id == "38647-It'sglowtime":
            product_id = "38647-It''sglowtime"

        # Voert for iedere product in productenlijst de functie brand_recommendation uit
        brand_recommendation(product_id, brand_id)

        counter += 1
        if counter % 1000 == 0:
            print(counter, "/ 34000 producten zijn ingeladen")

    print("Table filled")

def main():
    create_table()
    fill_table()
    c.close()

main()