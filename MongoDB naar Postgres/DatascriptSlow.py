#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html
import psycopg2
from pymongo import MongoClient

def dataimportmgdb():
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
                "discount varchar,"
                "brand varchar);")

    cur.execute("CREATE TABLE all_se (_ID varchar PRIMARY KEY, "
                "buid varchar, has_sale varchar, segment varchar, preferences varchar, itorder varchar);")

    cur.execute("CREATE TABLE all_pro (_ID varchar PRIMARY KEY, "
                "buids varchar,"
                "recommendations varchar);")
    col = db.products
    products = col.find()
    count = 0
    for i in products:

        try:
            preferenceval = {}

            try:
                preference = i['preferences']['brand']
                newlist = list()
                for j in preference.keys():
                    newlist.append(j)
                    break

                preferenceval = newlist[0]

                preferenceval = str(preferenceval)
                cur.execute("select idbrand from brand where brandnaam = '{}' ".format(preferenceval))
                info = cur.fetchall()

                brandnaam = info[0][0]
                cur.execute(
                    "SELECT id FROM product where brand_idbrand = {} ORDER BY RANDOM() LIMIT 1;".format(brandnaam))
                proid = cur.fetchall()
                # print(proid[0][0])
                preferenceval = "{" + proid[0][0] + "}"

                '''
                preference = i['preferences']['brand']
                {k: v for k, v in sorted(preference.items(), key=lambda item: item[1])}
                print(preference.keys())
                preferenceval = newlist
                print(preferenceval)
                '''
            except:
                preferenceval = "{}"

            orderstring = "{"
            try:
                for j in range(len(i['order']['products'])):
                    # print(i['order']['products'][j].get('id'),end= " ")
                    orderstring += i['order']['products'][j].get('id') + ","
                orderstring = orderstring[:-1]
                orderstring += "}"
            except:
                orderstring = "{}"

            cur.execute(
                "INSERT INTO all_se (_ID, buid, has_sale, preferences,itorder,segment) VALUES (%s, %s,%s,%s,%s,%s)",
                (str(i['_id']),
                 str(i['buid']) if 'buid' in i else None,
                 str(i['has_sale']) if 'has_sale' in i else None,
                 preferenceval,
                 # str(i['preferences']['brand']) if 'preferences' in i else None,
                 # str(i['order']['products'][0]) if 'products' in i else None,
                 orderstring,
                 str(i['segment']) if 'segment' in i else None))

            '''
            cur.execute("INSERT INTO all_se (_ID, buid, has_sale, preferences,itorder,segment) VALUES ('{}', '{}','{}','{}','{}','{}')".format(str(i["_id"]), i["buid"] if "buid" in i else None, str(i["has_sale"]) if "has_sale" in i else None, preferenceval,orderstring, str(i["segment"]) if "segment" in i else None))
            '''

        except:

            try:
                orderstring = "{"
                try:
                    for j in range(len(i['order']['products'])):
                        # print(i['order']['products'][j].get('id'),end= " ")
                        orderstring += i['order']['products'][j].get('id') + ","
                    orderstring = orderstring[:-1]
                    orderstring += "}"
                except:
                    orderstring = "{}"

                cur.execute(
                    "INSERT INTO all_se (_ID, buid, has_sale, preferences,itorder,segment) VALUES (%s, %s,%s,%s,%s,%s)",
                    (str(i['_id']),
                     str(i['buid']) if 'buid' in i else None,
                     str(i['has_sale']) if 'has_sale' in i else None,
                     str(i['preferences']['brand']) if 'preferences' in i else None,
                     # str(i['order']['products'][0]) if 'products' in i else None,
                     orderstring,
                     str(i['segment']) if 'segment' in i else None))
            except:
                if count % 1000 == 0:
                    print(count, "Sessions")
                    print("error")
                    conn.commit()

            if count % 1000 == 0:
                print(count, "Sessions")
                print("error")
                conn.commit()

        count += 1

        if count % 1000 == 0:
            print(count, "Sessions")
            conn.commit()
    print("done with sessions")
    conn.commit()


def createrecomendeditemsrecords():
    categorydict = {}
    subcategorydict = {}
    subsubcategorydict = {}
    branddict = {}
    genderdict = {}
    # met deze execute haal ik alle producten op die zowiezo een deal hebben en daarna haal ik ze gesoorteerd binnen
    cur.execute("select all_p._id, all_p.category, all_p.sub_category, all_p.gender, all_p.sub_sub_category, all_p.brand,all_p.price, all_p.discount from all_p WHERE all_p.discount IS NOT NULL and all_p.category is not null order by category, sub_category, gender,discount asc")
    rows = cur.fetchall()

    for row in rows:
        # een stukje code om alle categories uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[1][0]], str) == True:
            if row[1] in categorydict:
                categorydict[row[1]] += 1
            else:
                categorydict[row[1]] = 1
        if row[1] in categorydict:
            categorydict[row[1]] += 1
        else:
            categorydict[row[1]] = 1

        # een stukje code om alle subcategories uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[2][0]], str) == True:
            if row[2] in subcategorydict:
                subcategorydict[row[2]] += 1
            else:
                subcategorydict[row[2]] = 1
        if row[2] in subcategorydict:
            subcategorydict[row[2]] += 1
        else:
            subcategorydict[row[2]] = 1

        # een stukje code om alle genders/targetaudience uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[3][0]], str) == True:
            if row[3] in genderdict:
                genderdict[row[3]] += 1
            else:
                genderdict[row[3]] = 1
        if row[3] in genderdict:
            genderdict[row[3]] += 1
        else:
            genderdict[row[3]] = 1

        # een stukje code om alle subsubsubcategories uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[4][0]], str) == True:
            if row[4] in subsubcategorydict:
                subsubcategorydict[row[4]] += 1
            else:
                subsubcategorydict[row[4]] = 1
        if row[4] in subsubcategorydict:
            subsubcategorydict[row[4]] += 1
        else:
            subsubcategorydict[row[4]] = 1

        # een stukje code om alle brands uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[5][0]], str) == True:
            if row[5] in branddict:
                branddict[row[5]] += 1
            else:
                branddict[row[5]] = 1
        if row[5] in branddict:
            branddict[row[5]] += 1
        else:
            branddict[row[5]] = 1

    #een stukje code om de keys van alles dicts om te zetten naar een list omdat ik dat makelijker werken vindt
    categorylst = []
    subcategorylst = []
    subsubcategorylst = []
    brandlst = []
    genderlst = []
    for keys in categorydict.keys():
        categorylst.append(keys)
    for keys in subcategorydict.keys():
        subcategorylst.append(keys)
    for keys in genderdict.keys():
        genderlst.append(keys)
    for keys in subsubcategorydict.keys():
        subsubcategorylst.append(keys)
    for keys in branddict.keys():
        brandlst.append(keys)

    #return alle list zodat ik ze ergens anders kan gebruiken in anderen stukken code voor flexibiliteit
    return categorylst,subcategorylst,genderlst,subsubcategorylst,brandlst

def getitemrecords(id):
    #het ophalen van de prodcuct gegevens met een query
    #filter voor een specifieke record
    if id == "38647-It'sglowtime":
        id = "38647-It\''sglowtime"
    #edited last 2
    cur.execute("select all_p._id, all_p.category, all_p.sub_category, all_p.gender,all_p.brand, all_p.sub_sub_category, all_p.price, all_p.discount from all_p where _id = '{}'".format(id))
    info = cur.fetchall()
    return info

def clearerd():
    cur.execute("DROP TABLE IF EXISTS category CASCADE;")
    cur.execute("DROP TABLE IF EXISTS gender CASCADE;")
    cur.execute("DROP TABLE IF EXISTS brand CASCADE;")
    cur.execute("DROP TABLE IF EXISTS product CASCADE")
    cur.execute("DROP TABLE IF EXISTS profile CASCADE")
    cur.execute("DROP TABLE IF EXISTS session CASCADE")
    cur.execute("DROP TABLE IF EXISTS preference_session CASCADE")
    cur.execute("DROP TABLE IF EXISTS order_session CASCADE")

    cur.execute("CREATE TABLE brand (idBrand serial NOT NULL,brandnaam varchar(45),CONSTRAINT brand_pk PRIMARY KEY (idBrand)) WITH (OIDS=FALSE);")
    cur.execute(
        "CREATE TABLE category (idcategory serial NOT NULL,category varchar(45),sub_category varchar(45),sub_sub_category varchar(45),CONSTRAINT category_pk PRIMARY KEY (idcategory)) WITH (OIDS=FALSE);")
    cur.execute("CREATE TABLE gender (idgender serial NOT NULL,gendernaam varchar(45),CONSTRAINT gender_pk PRIMARY KEY (idgender)) WITH (OIDS=FALSE);")
    cur.execute("CREATE TABLE product (id varchar(45) NOT NULL,selling_price integer,brand_idBrand integer,gender_idgender integer,discount varchar(45),category_idcategory integer,CONSTRAINT product_pk PRIMARY KEY (id)) WITH (OIDS=FALSE);")
    cur.execute("CREATE TABLE profile (id varchar(255) NOT NULL,recommendation_segment varchar(45),recommendations varchar,buids varchar,CONSTRAINT profile_pk PRIMARY KEY (id)) WITH (OIDS=FALSE);")
    cur.execute("CREATE TABLE session (id varchar(255) NOT NULL,has_sale varchar(45),prefences varchar,profile_id varchar(255),buid varchar,segment varchar(255),itorder varchar,CONSTRAINT session_pk PRIMARY KEY (id)) WITH (OIDS=FALSE);")
    cur.execute("CREATE TABLE preference_session (id serial NOT NULL,session_id varchar(255) NOT NULL, category_idcategory integer NOT NULL, CONSTRAINT preference_session_pk PRIMARY KEY (id)) WITH (OIDS=FALSE);")
    cur.execute("CREATE TABLE order_session (id serial NOT NULL,session_id varchar(255) NOT NULL,product_id varchar(45) NOT NULL,CONSTRAINT order_session_pk PRIMARY KEY (id)) WITH (OIDS=FALSE);")
    return

def filldata():
    cur.execute("INSERT INTO category(category,sub_category,sub_sub_category) SELECT DISTINCT category, sub_category,sub_sub_category from all_p order by category asc;")
    cur.execute("INSERT INTO profile(id, recommendations,buids) SELECT _id,recommendations, buids from all_pro;")
    cur.execute("INSERT INTO session(id, has_sale, prefences,buid,segment,itorder) SELECT all_se._id,all_se.has_sale,all_se.preferences,all_se.buid,all_se.segment,all_se.itorder from all_se;")

    for item in searchitems[2]:
        # print(item)
        cur.execute("INSERT INTO gender(gendernaam) VALUES ('{}')".format(item))

    for item in searchitems[4]:
        # print(item)
        if item == "M&M's":
            item = "M&M\''s"
        if item == "Grab 'n Go":
            item = "Grab \''n Go"
        if item == "Lucy's Home":
            item = "Lucy\''s Home"
        if item == "L'alerteur":
            item = "L\''alerteur"
        if item == "Dr. Tom's":
            item = "Dr. Tom\''s"
        if item == "Lay's":
            item = "Lay\''s"
        if item == "Tesori d'Oriente":
            item = "Tesori d\''Oriente"
        if item == "Pet's Unlimited":
            item = "Pet\''s Unlimited"
        cur.execute("INSERT INTO brand(brandnaam) VALUES ('{}')".format(item))
    return

def queuedata():
    cur.execute("select all_p._id from all_p")
    ids = cur.fetchall()
    count =0
    for id in ids:
        itemrecords = getitemrecords(id[0])

        cur.execute("select idgender from gender where gendernaam = '{}';".format(itemrecords[0][3]))
        genderid = cur.fetchall()[0][0]

        item = itemrecords[0][4]
        if item == "M&M's":
            item = "M&M\''s"
        if item == "Grab 'n Go":
            item = "Grab \''n Go"
        if item == "Lucy's Home":
            item = "Lucy\''s Home"
        if item == "L'alerteur":
            item = "L\''alerteur"
        if item == "Dr. Tom's":
            item = "Dr. Tom\''s"
        if item == "Lay's":
            item = "Lay\''s"
        if item == "Tesori d'Oriente":
            item = "Tesori d\''Oriente"
        if item == "Pet's Unlimited":
            item = "Pet\''s Unlimited"

        cur.execute("select idbrand from brand where brandnaam = '{}';".format(item))
        try:
            brandid = cur.fetchall()[0][0]
        except:
            #dit is het merk None, eigenmerk.. wordt maar op 2 records toegepast
            brandid = 2


        category = itemrecords[0][1]
        subcategory = itemrecords[0][2]
        subsubcategory = itemrecords[0][5]
        if subcategory == "Baby's en kinderen":
            subcategory = "Baby\''s en kinderen"
        if category == "['Make-up & geuren', 'Make-up', 'Nagellak']":
            category = "[\''Make-up & geuren\'', \''Make-up\'', \''Nagellak\'']"
        if subsubcategory =="Vibrators en dildo's":
            subsubcategory = "Vibrators en dildo\''s"

        cur.execute("select * from category where category = '{}' and sub_category = '{}' and sub_sub_category = '{}';".format(category,subcategory,subsubcategory))
        try:
            catid = cur.fetchall()[0][0]
        except:
            catid = 238


        itemid = itemrecords[0][0]
        if itemid == "38647-It'sglowtime":
            itemid = "38647-It\''sglowtime"

        selling_price = itemrecords[0][6]
        if selling_price == "None":
            selling_price = 0
        if selling_price == "none":
            selling_price = 0
        if selling_price == "":
            selling_price = 0
        if selling_price == "null":
            selling_price = 0
        if selling_price == "Null":
            selling_price = 0
        if selling_price == subsubcategory:
            selling_price= 0

        productrecord = [itemid,selling_price,genderid,brandid,itemrecords[0][7],catid]

        try:
            cur.execute("INSERT INTO product(id,selling_price,brand_idbrand,gender_idgender,discount,category_idcategory) VALUES ('{}','{}','{}','{}','{}','{}')".format(productrecord[0],productrecord[1],productrecord[3],productrecord[2],productrecord[4],productrecord[5]))
        except:
            print((productrecord[1]))
            productrecord(type(productrecord[1]))
        count += 1
        if count % 1000 == 0:
            print(count, "products")
    print("done with products")

def fkmaker():
    cur.execute("ALTER TABLE product ADD CONSTRAINT product_fk0 FOREIGN KEY (brand_idBrand) REFERENCES brand(idBrand);")
    cur.execute("ALTER TABLE product ADD CONSTRAINT product_fk1 FOREIGN KEY (gender_idgender) REFERENCES gender(idgender);")
    cur.execute("ALTER TABLE product ADD CONSTRAINT product_fk2 FOREIGN KEY (category_idcategory) REFERENCES category(idcategory);")
    cur.execute("ALTER TABLE session ADD CONSTRAINT session_fk0 FOREIGN KEY (profile_id) REFERENCES profile(id);")

def sessiontoprofile():
    #cur.execute("select buid,id from session where prefences != 'null'")
    cur.execute("select buid,prefences,itorder,id from session where prefences != '{}' or itorder !='{}' order by prefences desc")
    buids = cur.fetchall()
    count = 0
    print(len(buids))
    cur.execute("SELECT id, buids FROM profile")
    #cur.execute("SELECT id FROM profile")
    proinfo = cur.fetchall()
    matching = [s for s in proinfo if '{r390PNmqPdqIs9xNH9aBQT2yktexrUycgjFuLWpDwHpkxpepow65ja7XFwlchYcB7hbI}' in s]
    print(matching)

    #print(proinfo.index('5c485b2677267e00010652e0'))
    for buid in buids[:2800]:
        try:
            convbuid = "{" + str(buid[0][2:-2]) + "}"
            matching = [s for s in proinfo if convbuid in s]
            #print((matching[0][0], buid[3]))
            #print(buid[0][2:-2])
            if len(buids[0][1]) > 3:
                recommendation = buids[0][1]
            else:
                recommendation = buids[0][2]
            cur.execute("UPDATE session SET profile_id = '{}' WHERE id = '{}';".format(matching[0][0], buid[3]))
            cur.execute("UPDATE profile SET recommendations = '{}' WHERE id = '{}'; ".format(recommendation, matching[0][0]))
        except:
            print("error")
        count += 1
        if count % 50 == 0:
            print(count, "profiles linked")

    '''
    for buid in buids[:3000]:
        try:
            #print(buid[0][2:-2])
            cur.execute("SELECT id FROM profile WHERE buids LIKE '%{}%'".format(buid[0][2:-2]))
            if len(buids[0][1]) > 3:
                recommendation = buids[0][1]
            else:
                recommendation = buids[0][2]
            profid = cur.fetchall()[0][0]
            sesid = buid[3]
            cur.execute("UPDATE session SET profile_id = '{}' WHERE id = '{}';".format(profid,sesid))
            #cur.execute("UPDATE profile SET recommendations = '{}' WHERE id = '{}'; ".format(recommendation,profid))
        except:
            print("Error","profid",profid,"id",sesid)
            #print("id",sesid)
        count += 1
        if count % 50 == 0:
            print(count, "profiles linked")
    '''
    print("done with profile-link")


client = MongoClient('localhost', 27017)    #MongodB connectie
db = client.huwebshop

conn = psycopg2.connect("dbname=voordeelschoptest user=postgres password=kip")
cur = conn.cursor()

#~~~~~~~~~~~~~~~~~~~~~~~~ code voor product koppeling

dataimportmgdb()

searchitems = createrecomendeditemsrecords()

clearerd()
filldata()
queuedata()

sessiontoprofile()

fkmaker()

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
