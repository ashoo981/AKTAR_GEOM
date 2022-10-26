
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile
import time 


from  utilities  import readProperties
import psycopg2

df = pd.read_excel('.\\Data\\PostgreAktar.xlsx','KaisOkunan')

coor = readProperties.ReadConfig.get_aktar_geom()
conn= None
dbname= readProperties.ReadConfig.get_database_name()
users= readProperties.ReadConfig.get_database_username()
host= readProperties.ReadConfig.get_database_host()
passwrd = readProperties.ReadConfig.get_database_password()
port = readProperties.ReadConfig.get_database_port()

conn = psycopg2.connect(f"dbname={dbname} user={users} password={passwrd} host={host} port={port}")

ids = df['id']
nadpiss = df['nadpis']
obyasneniee = df['obyasnenie']
geoms =df['geom']


for i in range( len(df['id'])-1):
    id= str( ids[i])
    nadpis= str( nadpiss[i])
    obyasnenie= str( obyasneniee[i])
    geom =str( geoms[i])

    if  nadpis == 'nan':
        print("geometri verisi boş")

    else:   

        sql =  f"insert into aktar_parsel (geom,id,nadpis,obyasnenie) values (ST_GeomFromText('" + geom +"'  )," + id +"," + nadpis +"," + "'"+ obyasnenie + "'" +")"
        #sql =  f"insert into aktar_parsel (geom) values (ST_GeomFromText('POLYGON(('"+geom +"')) ' ))"

        sqlr =(sql.replace("(('","((")).replace("'))","))")
        #sql="'insert into aktar_parsel (geom) values  (ST_GeomFromText("'POLYGON(( '{text_geom}' )) )'"

        ###print (sqlr)
       

        cursor  = conn.cursor()
        cursor.execute(sqlr)
        conn.commit()
        print ("kayıt eklendi.")

time.sleep(10)       
