import psycopg2


con = psycopg2.connect("dbname=vdshoptest user=postgres password=kip")
cur = con.cursor()

cur.execute("select prefences, profile_id from session where profile_id != 'null' order by profile_id")

prefences = cur.fetchall()

for prefencenid in prefences:
    #prefence = json.loads(prefence[0])
    prefence = prefencenid[0]
    #print(type(prefence))
    #print(prefence)
    conv = list(prefence.split(","))
    #print(conv)
    #print(type(conv))
    catlst = []
    try:
        for i in conv:

            if 'category' in i:
                i = list(i.split("{'"))
                #i = i[0:-2]
                #print(type(i))
                #print(i[1][0:-3])
                if i[1] == "'":
                    i.pop(1)
                catlst.append(i[1][0:-3])
                #print(catlst)
                #print(i, end= "  ")
        recom = list(prefencenid)+catlst
        recom.pop(0)
        #print(recom)

        for j in recom:
            if str(j).__contains__("views"):
                recom.remove(j)

        if len(recom) >=4:
            cur.execute("select idcategory from category where category = '{}' and sub_category = '{}' and sub_sub_category ='{}'".format(recom[1],recom[2],recom[3]))
        elif len(recom) == 3:
            cur.execute("select idcategory from category where category = '{}' and sub_category = '{}'".format(recom[1], recom[2]))
        elif len(recom) == 2:
            cur.execute("select idcategory from category where category = '{}'".format(recom[1]))
        elif len(recom) == 1:
            cur.execute("select idcategory from category where category IS NULL")
        reccatid = cur.fetchall()
        #print(reccatid[0][0])
        recom.append(reccatid[0][0])
        #print(recom[4])

        try:
            if len(recom) > 1:
                cur.execute("SELECT id FROM product where category_idcategory = {} ORDER BY RANDOM() LIMIT 1;".format(recom[-1]))
                prodid= cur.fetchall()
                print(prefencenid[1],prodid[0][0])
                recommendation = str(prodid[0][0])
                cur.execute("UPDATE profile SET recommendations = '{}' WHERE id = '{}';".format(recommendation,prefencenid[1]))
        except:
            print("error")

    except:
        #print('error',conv)
        print('error')

con.commit()
con.close()
