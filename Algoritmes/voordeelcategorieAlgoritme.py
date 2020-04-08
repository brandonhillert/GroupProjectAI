# https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
# https://api.mongodb.com/python/current/tutorial.html
# https://www.psycopg.org/docs/usage.html
import psycopg2

"""" 
Author: Richard Jansen
Dit bestand genereert het voordeelcategorie tabel
"""

conn = psycopg2.connect("dbname=voordeelshoponescript user=postgres password=admin")
cur = conn.cursor()


def recomendeditems(category, subcategory, targetaudience):
    """
    Hier maak ik gebruik van een SQL statement die in mijn Recomended items
    table alleen maar de producten hallen die overeen komen de gegeven category,
    subcategory en target audience(kunnen maximaal 5 items zijn*)
    Ik moest verschillenden entries aanpassen omdat ze niet 1 op 1 in sql konden,
    hier onder worden de strings aangepast zodat ze werken in SQL
    """
    if targetaudience == "Baby's":
        targetaudience = "Baby\''s"
    if subcategory == "Baby's en kinderen":
        subcategory = "Baby\''s en kinderen"
    if category == "['Make-up & geuren', 'Make-up', 'Nagellak']":
        category = "[\''Make-up & geuren\'', \''Make-up\'', \''Nagellak\'']"

    cur.execute("SELECT recomendedpro._id, recomendedpro.category,"
                " recomendedpro.sub_category, recomendedpro.targetaudience "
                "FROM recomendedpro  "
                "WHERE category = '{}'AND sub_category = '{}' "
                "AND targetaudience = '{}'".format(category, subcategory, targetaudience))
    info = cur.fetchall()

    return info


"""
Deze functie maak een table aan voor mijn producten die ik wil laten zien
"""


def createrecomendeditemstable():
    cur.execute("DROP TABLE IF EXISTS recomendedpro;")
    cur.execute("CREATE TABLE recomendedpro (id serial  PRIMARY KEY, "
                "_ID varchar , "
                "category varchar, "
                "sub_category varchar, "
                "targetaudience varchar, "
                "sellingprice varchar, "
                "deal varchar);")


def createrecomendeditemsrecords():
    categorydict = {}
    subcategorydict = {}
    subsubcategorydict = {}
    branddict = {}
    genderdict = {}
    # Deze execute haalt alle producten op die zowiezo een deal hebben, en daarna haal ik ze gesorteerd binnen
    cur.execute("SELECT all_p._id, all_p.category, all_p.sub_category, "
                "all_p.gender, all_p.sub_sub_category, all_p.brand,all_p.price, all_p.discount "
                "FROM all_p "
                "WHERE all_p.discount IS NOT NULL "
                "AND all_p.category IS NOT NULL "
                "ORDER BY category, sub_category, gender,discount "
                "ASC")
    rows = cur.fetchall()

    for row in rows:
        # Code om alle categories uit de query te hallen en dit naar een dict te zetten
        if isinstance(row[[1][0]], str) == True:
            if row[1] in categorydict:
                categorydict[row[1]] += 1
            else:
                categorydict[row[1]] = 1
        if row[1] in categorydict:
            categorydict[row[1]] += 1
        else:
            categorydict[row[1]] = 1

        # Code om alle subcategories uit de query te hallen en dit naar een dict te zetten
        if isinstance(row[[2][0]], str) == True:
            if row[2] in subcategorydict:
                subcategorydict[row[2]] += 1
            else:
                subcategorydict[row[2]] = 1
        if row[2] in subcategorydict:
            subcategorydict[row[2]] += 1
        else:
            subcategorydict[row[2]] = 1

        # Code om alle genders/targetaudience uit de query te hallen en dit naar een dict te zetten
        if isinstance(row[[3][0]], str) == True:
            if row[3] in genderdict:
                genderdict[row[3]] += 1
            else:
                genderdict[row[3]] = 1
        if row[3] in genderdict:
            genderdict[row[3]] += 1
        else:
            genderdict[row[3]] = 1

        # Code om alle subsubsubcategories uit de query te hallen en dit naar een dict te zetten
        if isinstance(row[[4][0]], str) == True:
            if row[4] in subsubcategorydict:
                subsubcategorydict[row[4]] += 1
            else:
                subsubcategorydict[row[4]] = 1
        if row[4] in subsubcategorydict:
            subsubcategorydict[row[4]] += 1
        else:
            subsubcategorydict[row[4]] = 1

        # Code om alle brands uit de query te hallen en dit naar een dict te zetten
        if isinstance(row[[5][0]], str) == True:
            if row[5] in branddict:
                branddict[row[5]] += 1
            else:
                branddict[row[5]] = 1
        if row[5] in branddict:
            branddict[row[5]] += 1
        else:
            branddict[row[5]] = 1

    # Code om de keys van alle dicts om te zetten naar een List
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

    # Returned alle list voor voorkomen van redudantie
    return categorylst, subcategorylst, genderlst, subsubcategorylst, brandlst


def fillrecomendeditems(categorylst, subcategorylst, genderlst):
    cur.execute("SELECT all_p._id, all_p.category, all_p.sub_category,"
                " all_p.gender, all_p.price, all_p.discount "
                "FROM all_p "
                "WHERE all_p.discount IS NOT NULL "
                "AND all_p.category IS NOT NULL "
                "ORDER BY category, sub_category, gender,discount ASC")
    rows = cur.fetchall()
    # Per subcategory een selectie van 5 items per target/gender naar Database
    for j in range(0, len(subcategorylst)):
        for k in range(0, len(genderlst)):
            # Counter voor het maximale aantal elementen per subcategory en target/gender
            count = 0
            for row in rows:
                # i bevat de category waarmee er wordt gesorteerd
                if count == 5:
                    break
                if (subcategorylst[j] in row and genderlst[k] in row):
                    count += 1
                    cur.execute(
                        "INSERT INTO recomendedpro (_ID, category,"
                        " sub_category, targetaudience, sellingprice, deal) "
                        "VALUES ( %s, %s, %s, %s, %s, %s)",
                        (row[0], row[1], row[2], row[3], row[4], row[5]))

    for i in range(0, len(categorylst)):
        # Per category een selectie van 5 items per target/gender  naar de database
        for k in range(0, len(genderlst)):
            # Counter voor het maximale aantal elementen per category en target/gender
            count = 0
            for row in rows:
                # i bevat category waarmee er wordt gesorteerd
                if count == 5:
                    break
                if (subcategorylst[i] in row and genderlst[k] in row):
                    # print(row)
                    count += 1
                    cur.execute(
                        "INSERT INTO recomendedpro (_ID, category, sub_category,"
                        " targetaudience, sellingprice, deal) "
                        "VALUES ( %s, %s, %s, %s, %s, %s)",
                        (row[0], row[1], row[2], row[3], row[4], row[5]))

    cur.execute("SELECT DISTINCT recomendedpro._id, recomendedpro.category,"
                " recomendedpro.sub_category, recomendedpro.targetaudience "
                "FROM recomendedpro "
                "ORDER BY recomendedpro._id ASC")
    prorows = cur.fetchall()

    cur.execute("DROP TABLE IF EXISTS recomendedpro;")
    cur.execute("CREATE TABLE recomendedpro (_ID varchar  PRIMARY KEY, "
                "category varchar, "
                "sub_category varchar, "
                "targetaudience varchar);")

    for prorow in prorows:
        cur.execute("INSERT INTO recomendedpro (_ID, category, sub_category, targetaudience) "
                    "VALUES ( %s, %s, %s, %s)",
                    (prorow[0], prorow[1], prorow[2], prorow[3]))
    return


"""
Het ophalen van de product gegevens met een query
Filter voor een specifieke record
"""


def getitemrecords(id):
    #
    if id == "38647-It'sglowtime":
        id = "38647-It\''sglowtime"

    cur.execute("SELECT all_p._id, all_p.category, all_p.sub_category,"
                " all_p.gender,all_p.brand, all_p.sub_sub_category,"
                " all_p.price, all_p.discount "
                "FROM all_p "
                "WHERE _id = '{}'".format(id))
    info = cur.fetchall()
    return info


"""
Functie om tabel voordeelcatalgoritme aan temaken
"""


def createidlink():
    #
    cur.execute("DROP TABLE IF EXISTS prolink;")
    cur.execute("DROP TABLE IF EXISTS voordeelcatalgoritme;")
    cur.execute("CREATE TABLE voordeelcatalgoritme (id varchar  PRIMARY KEY, "
                "product1 varchar, "
                "product2 varchar, "
                "product3 varchar, "
                "product4 varchar, "
                "product5 varchar);")
    return


"""
# Deze functie itereerd over alle items die er zijn 
en verwerkt alleproducten in een nieuwe tabel 
met de recommended items erbij
"""


def fillidlinktable():
    cur.execute("select all_p._id from all_p")
    ids = cur.fetchall()

    counter = 0

    for id in ids:
        itemrecords = getitemrecords(id[0])
        recomendedlist = recomendeditems(itemrecords[0][1], itemrecords[0][2], itemrecords[0][3])
        # print("list met recomende id's", [i[0] for i in recomendedlist])
        if len(recomendedlist) == 5:
            cur.execute("INSERT INTO voordeelcatalgoritme (ID, product1, product2, product3,product4,product5) "
                        "VALUES ( %s, %s, %s, %s,%s,%s)", (
                            id, recomendedlist[0][0], recomendedlist[1][0], recomendedlist[2][0], recomendedlist[3][0],
                            recomendedlist[4][0]))
        elif len(recomendedlist) == 4:
            cur.execute("INSERT INTO voordeelcatalgoritme (ID, product1, product2, product3,product4) "
                        "VALUES ( %s, %s, %s, %s,%s)",
                        (id, recomendedlist[0][0], recomendedlist[1][0], recomendedlist[2][0], recomendedlist[3][0]))
        elif len(recomendedlist) == 3:
            cur.execute("INSERT INTO voordeelcatalgoritme (ID, product1, product2, product3) "
                        "VALUES ( %s, %s, %s, %s)",
                        (id, recomendedlist[0][0], recomendedlist[1][0], recomendedlist[2][0]))
        elif len(recomendedlist) == 2:
            cur.execute("INSERT INTO voordeelcatalgoritme (ID, product1, product2) "
                        "VALUES ( %s, %s, %s)", (id, recomendedlist[0][0], recomendedlist[1][0]))
        elif len(recomendedlist) == 1:
            cur.execute("INSERT INTO voordeelcatalgoritme (ID, product1) "
                        "VALUES ( %s, %s)", (id, recomendedlist[0][0]))
        elif len(recomendedlist) == 0:
            cur.execute("INSERT INTO voordeelcatalgoritme (ID) "
                        "VALUES ( %s)", (id))

        counter += 1
        if counter % 1000 == 0:
            print(counter, "/34000 producten zijn ingeladen")

    print("De producten zijn ingeladen")
    return


def main_loop():
    print("Beginnen met producten laden...")
    searchitems = createrecomendeditemsrecords()
    createrecomendeditemstable()
    fillrecomendeditems(searchitems[0], searchitems[1], searchitems[2])
    createidlink()
    fillidlinktable()

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()


main_loop()
