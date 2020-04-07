import psycopg2

conn = psycopg2.connect("user=postgres password=pgadminJTgeest dbname=voordeelshopgpx")
cur = conn.cursor()
print("postgres connected")

c.execute("DROP TABLE IF EXISTS brandrecommendations CASCADE")
c.execute("CREATE TABLE brandrecommendations (id VARCHAR PRIMARY KEY, "
          "product1 VARCHAR, product2 VARCHAR, product3 VARCHAR, product4 VARCHAR, product5 VARCHAR);")

c.execute("select id, brand_idbrand from product")
ids = c.fetchall()
