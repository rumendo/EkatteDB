import MySQLdb

con = MySQLdb.connect(
	host="localhost",
	user="root",
	passwd="root",
	db="ekatte")
x = con.cursor()

try:
    x.execute("""LOAD DATA LOCAL INFILE '/home/rumendo/ekatte/data/Ek_obl.csv' INTO TABLE region   FIELDS TERMINATED BY ',' ENCLOSED BY '"'   LINES TERMINATED BY '\n'  IGNORE 1 LINES;""")
    con.commit()
except:
    con.rollback()

try:
    x.execute("""LOAD DATA LOCAL INFILE '/home/rumendo/ekatte/data/Ek_obst.csv' INTO TABLE municipality   FIELDS TERMINATED BY ',' ENCLOSED BY '"'   LINES TERMINATED BY '\n'   IGNORE 1 LINES;""")
    con.commit()
except:
    con.rollback()

try:
    x.execute("""LOAD DATA LOCAL INFILE '/home/rumendo/ekatte/data/Ek_atte.csv' INTO TABLE city   FIELDS TERMINATED BY ',' ENCLOSED BY '"'   LINES TERMINATED BY '\n'   IGNORE 1 LINES;""")
    con.commit()
except:
    con.rollback()
