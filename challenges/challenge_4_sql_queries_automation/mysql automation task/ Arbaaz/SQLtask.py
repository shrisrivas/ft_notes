import mysql.connector as connection
import pandas as pandas
import csv

#create database
mydb = connection.connect(host="localhost", user="root", passwd="12345",use_pure=True)
cursor = mydb.cursor()
query = "Create database CarbonNanoTubes;"
cursor.execute(query)
mydb.close()

#create table
mydb = connection.connect(host="localhost", database = 'CarbonNanoTubes ',user="root", passwd="12345", use_pure=True)
query = "CREATE TABLE IF NOT EXISTS carbontubes (Chiral_indice_n0 INT(10), Chiral_indice_n1 INT(10), Chiral_indice_n2 INT(10), Chiral_indice_m0 INT(10), Chiral_indice_m1 INT(10), Initial_atomic_coordinate_u0 INT(10), Initial_atomic_coordinate_u1 INT(10), Initial_atomic_coordinate_v0 INT(10), Initial_atomic_coordinate_v1 INT(10), Initial_atomic_coordinate_w0 INT(10), Initial_atomic_coordinate_w1 INT(10), Calculated_atomic_coordinates_u0 INT(10), Calculated_atomic_coordinates_u1 INT(10), Calculated INT(10) )"
cursor = mydb.cursor()
cursor.execute(query)
with open('carbon_nanotubes.csv') as data:
    next(data)
    data_csv = csv.reader(data, delimiter = ";")
    for j in data_csv:
        l = []
        for i in j:
            k = i.split(',')
            l.extend( k)
        s=','.join(l)
        cursor.execute(f'insert into CarbonNanoTubes.carbontubes values ({s})')
    print("all the data is inserted")
mydb.commit()    
