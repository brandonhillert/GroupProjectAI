import psycopg2

def brandrecommendation(prodid):
    prodid = str(prodid)
    reclist = []
    prodidbrand = ""

    for item in ids:
        if item[0] == prodid:
            prodidbrand = item[1]
            break
        else:
            continue

    for item in ids:
        if item[0] == prodid:
            continue
        elif item[1] == prodidbrand:
            reclist.append(item[0])
    try:
        if len(reclist) >= 5:
            c.execute("INSERT INTO brandrecommendations (id, product1, product2, product3, product4, product5) VALUES (%s, %s, %s, %s, %s, %s)",
                        (prodid, reclist[0], reclist[1], reclist[2], reclist[3], reclist[4]))
        elif len(reclist) == 4:
            c.execute("INSERT INTO brandrecommendations (id, product1, product2, product3, product4) VALUES ( %s, %s, %s, %s,%s)",
                        (prodid, reclist[0], reclist[1], reclist[2], reclist[3]))
        elif len(reclist) == 3:
            c.execute("INSERT INTO brandrecommendations (id, product1, product2, product3) VALUES ( %s, %s, %s, %s)",
                        (prodid, reclist[0], reclist[1], reclist[2]))
        elif len(reclist) == 2:
            c.execute("INSERT INTO brandrecommendations (id, product1, product2) VALUES ( %s, %s, %s)",
                        (prodid, reclist[0], reclist[1]))
        elif len(reclist) == 1:
            c.execute("INSERT INTO brandrecommendations (id, product1) VALUES ( %s, %s)", (prodid, reclist[0]))
        elif len(reclist) == 0:
            c.execute("INSERT INTO brandrecommendations (id) VALUES ( %s)", (prodid))
    except:
        pass
    return

connect = psycopg2.connect("dbname=voordeelshopgpx user=postgres password=pgadminJTgeest")
c = connect.cursor()
print("postgres connected")

#c.execute("DROP TABLE IF EXISTS brandrecommendations CASCADE")
#c.execute("CREATE TABLE brandrecommendations (id VARCHAR PRIMARY KEY, "
#          "product1 VARCHAR, product2 VARCHAR, product3 VARCHAR, product4 VARCHAR, product5 VARCHAR);")

c.execute("select id, brand_idbrand from product")
ids = c.fetchall()

counter = 0

for id in ids:
    brandrecommendation(id[0])
    counter += 1
    if counter % 1000 == 0:
        print(counter)

print("Table filled")

connect.commit()
c.close()
