import mysql.connector
import pandas  as pd
from pyspark.sql import SparkSession

appName ="PySpark MySql Example "
master ="local"
spark =SparkSession.builder.master(master).appName(appName).getOrCreate()

#Establish a connection
conn = mysql.connector.connect(user='root' , database= 'sakila' ,password='Nikhil@2000', host='localhost',port=3306)
cursor =conn.cursor()
query ="SELECT * from actor"

pf=pd.read_sql(query,con=conn)
conn.close()

df=spark.createDataFrame(pf)
df.show()