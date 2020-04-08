'''
Het doel is om uit Itoder de brandnaam te halen via string manipulation
via de brand naam een brand ID krijg
dan een random product ID via brand ID krijgen
Product ID weg schrijven naar profile
'''

import psycopg2


con = psycopg2.connect("dbname=vdshoptest user=postgres password=kip")
cur = con.cursor()

cur.execute("select prefences, profile_id from session where profile_id != 'null' order by profile_id")

prefences = cur.fetchall()

for prefencenid in prefences[:5]:
    prefence = prefencenid[0]
    conv = list(prefence.split(","))
    catlst = []
    try:
        for i in conv:

            if 'brand' in i:
                i = list(i.split("{'"))
                #i = i[0:-2]
                #print(type(i))
                #print(i[1][0:-3])
                if i[1] == "'":
                    i.pop(1)
                catlst.append(i[1][0:-3])
                catlst.append(i[2][0:-3])
                #print(catlst)
                #print(i, end= "  ")
        if catlst[0] == 'brand':
            catlst.pop(0)
        recom = list(prefencenid)+catlst
        recom.pop(0)

        if recom[1] == 'brand':
            recom.pop(1)
        print(recom)
        try:
            cur.execute("select idbrand from brand where brandnaam LIKE '{}'".format(recom[1]))
            #cur.execute("select idbrand from brand where brandnaam LIKE '{}';".format('Zonnatura'))
        except:
            print("error 2")


        reccatid = cur.fetchall()
        print(reccatid[0][0])
        recom.append(reccatid[0][0])
        #print(recom[4])

        try:
            if len(recom) > 1:
                cur.execute("SELECT id FROM product where brand_idbrand = {} ORDER BY RANDOM() LIMIT 1;".format(recom[1]))
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
