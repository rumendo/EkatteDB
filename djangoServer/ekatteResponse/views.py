#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import sys
import unicodedata
import json
import MySQLdb
import csv

def invert_dict(d):
    return {v:k for k,v in d.items()}

def index(request):
    con = MySQLdb.connect(
    	host="localhost",
    	user="root",
    	passwd="root",
    	db="ekatte",
    	charset="utf8")
    x = con.cursor()

    with open('cyrillicMapping.csv') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        cyrillicList = invert_dict(dict(content))

    print(cyrillicList)
    city = ''
    cityRaw = request.GET['city'].split(';')
    for letterCode in cityRaw:
        if letterCode[2:] in cyrillicList:
            foundLetter = cyrillicList[letterCode[2:]]
            city += foundLetter

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

    try:
        if(not x.execute("SELECT * FROM city c JOIN municipality m ON c.municipality = m.municipality  JOIN region r ON m.region = r.region WHERE c.name = %s", (city,))):
            return HttpResponse("The city you are trying to search does not exist.")
        result = x.fetchall()
        con.commit()
    except:
    	con.rollback()

    con.close()
    return HttpResponse(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))
