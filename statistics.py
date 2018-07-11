#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import MySQLdb
import time

con = MySQLdb.connect(
	host="localhost",
	user="root",
	passwd="root",
	db="ekatte",
	charset="utf8")
x = con.cursor()

try:
	print("Number of regions:")
	x.execute("""SELECT COUNT(region) FROM region;""")
	id = x.fetchone()[0]
	print(id)
	con.commit()
except:
    con.rollback()

try:
	print("\nNumber of municipalities:")
	x.execute("""SELECT COUNT(municipality) FROM municipality;""")
	id = x.fetchone()[0]
	print(id)
	con.commit()
except:
	con.rollback()

try:
	print("\nNumber of cities:")
	x.execute("""SELECT COUNT(id_ekatte) FROM city;""")
	id = x.fetchone()[0]
	print(id)
	con.commit()
except:
	con.rollback()


city = raw_input("\nFor what city do you want more information: ")
query = "SELECT * FROM city WHERE name = \'" + city + "\'";

try:
	x.execute(query)
	result = x.fetchall()
	for row in result:
		print("\nEkatte-id: ")
		print(row[0])
		print("\nType: ")
		print(row[1])
		print("\nName: ")
		print(row[2])
		print("\nMunicipality: ")
		print(row[3])
	con.commit()
except:
	con.rollback()

con.close()
