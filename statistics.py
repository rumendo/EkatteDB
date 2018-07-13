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
#query = "SELECT * FROM city c JOIN municipality m ON c.municipality = m.municipality  JOIN region r ON m.region = r.region WHERE c.name = \'" + city + "\'";
try:
	if(not x.execute("SELECT * FROM city c JOIN municipality m ON c.municipality = m.municipality  JOIN region r ON m.region = r.region WHERE c.name = %s", (city,))):
		print("\nThe city you are trying to search does not exist.")
	result = x.fetchall()
	for row in result:
		print("\nName: ")
		print(row[1] + " " + row[2])
		print("\nMunicipality: ")
		print(row[3])
		print(row[5])
		print("\nRegion: ")
		print(row[6])
		print(row[9])
		print("\nEkatte-id: ")
		print(row[0])
	con.commit()
except:
	con.rollback()

con.close()
