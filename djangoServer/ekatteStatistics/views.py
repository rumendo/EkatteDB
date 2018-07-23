from django.http import HttpResponse
import sys
import json
import MySQLdb

con = MySQLdb.connect(
	host="localhost",
	user="root",
	passwd="root",
	db="ekatte",
	charset="utf8")
x = con.cursor()

def index(request):
    id = []
    try:
    	x.execute("""SELECT COUNT(region) FROM region;""")
    	id.append(x.fetchone()[0])
    	con.commit()
    except:
        con.rollback()

    print(id)

    try:
    	x.execute("""SELECT COUNT(municipality) FROM municipality;""")
    	id.append(x.fetchone()[0])
    	con.commit()
    except:
    	con.rollback()

    print(id)

    try:
    	x.execute("""SELECT COUNT(id_ekatte) FROM city;""")
    	id.append(x.fetchone()[0])
    	con.commit()
    except:
    	con.rollback()

    return HttpResponse(json.dumps(id))
