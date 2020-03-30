import psycopg2
from pymongo import MongoClient
client = MongoClient('localhost', 27017)    #MongodB connectie

db = client.huwebshop
conn = psycopg2.connect("dbname=voordeelshopgp user=postgres password=kip")       #edit dit voor je eigen database
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS all_p;")
cur.execute("DROP TABLE IF EXISTS all_se;")
cur.execute("DROP TABLE IF EXISTS all_pro;")

cur.execute("CREATE TABLE all_p (_ID varchar PRIMARY KEY, "
            "data varchar, "
            "price integer, "
            "category varchar,"
            "sub_category varchar, "
            "sub_sub_category varchar, "
            "gender varchar, "
            "color varchar, "
            "herhaalaankoop varchar,"
            "brand varchar);")

cur.execute("CREATE TABLE all_se (_ID varchar PRIMARY KEY, "
            "buid varchar, has_sale varchar, segment varchar, preferences varchar, itorder varchar);")

cur.execute("CREATE TABLE all_pro (_ID varchar PRIMARY KEY, "
            "buids varchar,"
            "recommendations varchar);")


col = db.products
products = col.find()
count =0
for i in products:
    cur.execute("INSERT INTO all_p (_ID, data, price,category ,sub_category, sub_sub_category, gender, color, herhaalaankoop, brand) VALUES (%s, %s, %s,%s, %s, %s,%s, %s,%s,%s)",
                (i['_id'],
                 i['name'] if 'name' in i else None,
                 i['price']['selling_price'] if 'price' in i else None,
                 i['category'] if 'category' in i else None,
                 i['sub_category'] if 'sub_category' in i else None,
                 i['sub_sub_category'] if 'sub_sub_category' in i else None,
                 i['gender'] if 'gender' in i else None,
                 i['color'] if 'color' in i else None,
                 i['herhaalaankoop'] if 'herhaalaankoop' in i else None,
                 i['brand'] if 'brand' in i else None))
    count +=1
    if count % 1000 == 0:
        print(count,"Products")
print("done with products")

col = db.profiles
profiles = col.find()
count =0
for i in profiles:
    cur.execute("INSERT INTO all_pro (_ID, buids, recommendations) VALUES (%s, %s, %s)",
                (str(i['_id']),
                 i['buids'] if 'buids' in i else None,
                 i['recommendations']['viewed_before'] if 'recommendations' in i else None))
    count +=1
    if count % 1000 == 0:
        print(count,"Profiles")
print("done with profiles")

col = db.sessions
sessions = col.find()

count =0
for i in sessions:
    cur.execute("INSERT INTO all_se (_ID, buid, has_sale, preferences,itorder,segment) VALUES (%s, %s,%s,%s,%s,%s)",
                (str(i['_id']),
                 str(i['buid']) if 'buid' in i else None,
                 str(i['has_sale']) if 'has_sale' in i else None,
                 str(i['preferences']) if 'preferences' in i else None,
                 str(i['order']) if 'order' in i else None,
                 str(i['segment']) if 'segment' in i else None))
    count +=1
    if count % 1000 == 0:
        print(count,"Sessions")
print("done with sessions")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()