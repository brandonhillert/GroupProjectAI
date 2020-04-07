import psycopg2
import re

def insert_into_table(newrecs):
    try:
        if len(newrecs) >= 6:
            c.execute("INSERT INTO categoryrecommendations (id, prod1, prod2, prod3, prod4, prod5) VALUES (%s, %s, %s, %s, %s, %s)",
                        (newrecs[0], newrecs[1], newrecs[2], newrecs[3], newrecs[4], newrecs[5]))
        elif len(newrecs) == 5:
            c.execute("INSERT INTO categoryrecommendations (id, prod1, prod2, prod3, prod4) VALUES ( %s, %s, %s, %s,%s)",
                        (newrecs[0], newrecs[1], newrecs[2], newrecs[3]))
        elif len(newrecs) == 4:
            c.execute("INSERT INTO categoryrecommendations (id, prod1, prod2, prod3) VALUES ( %s, %s, %s, %s)",
                        (newrecs[0], newrecs[1], newrecs[2]))
        elif len(newrecs) == 3:
            c.execute("INSERT INTO categoryrecommendations (id, prod1, prod2) VALUES ( %s, %s, %s)",
                        (newrecs[0], newrecs[1]))
        elif len(newrecs) == 2:
            c.execute("INSERT INTO categoryrecommendations (id, prod1) VALUES ( %s, %s)", (newrecs[0], newrecs[1]))
        elif len(newrecs) == 1:
            c.execute("INSERT INTO categoryrecommendations (id) VALUES ( %s)", (newrecs[0]))
    except:
        pass

def only_numerics(seq):             #Behoud alleen nummer van string
    seq_type = type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

def formatting_item(product):
    product = product[1:-1]
    product = product.split(",")
    product = product[0]
    product = only_numerics(product)
    if product != '':
        product = int(product)
    return product

connect = psycopg2.connect("user=postgres password=pgadminJTgeest dbname=voordeelshopgpx")
c = connect.cursor()

c.execute("DROP TABLE IF EXISTS categoryrecommendations CASCADE")
c.execute("CREATE TABLE categoryrecommendations (id VARCHAR PRIMARY KEY, "
          "prod1 VARCHAR, prod2 VARCHAR, prod3 VARCHAR, prod4 VARCHAR, prod5 VARCHAR);")

c.execute("select id, recommendations from profile where recommendations != '{}'")
idprevrec = c.fetchall()
counter = 0

for item in idprevrec:
    product = item[1]
    product = formatting_item(product)

    try:
        c.execute("select id, product1, product2, product3, product4, product5 from categorie_algoritme "
                  "where id = '{}';".format(product))
        newrecs = c.fetchall()

        if newrecs != []:
            newrecs = newrecs[0]
            newrecs = list(newrecs)
            if len(newrecs) > 6:
                newrecs = newrecs[0:6]
            newrecs.remove(newrecs[0])
            copy = newrecs.copy()
            for rec in copy:
                if rec == None:
                    newrecs.remove(rec)
            newrecs.insert(0, item[0])

        else:
            continue
        insert_into_table(newrecs)
    except:
        print("foutmelding")

    counter += 1
    if counter % 10000 == 0:
        print(counter)

connect.commit()
c.close()
