from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import os
import sys

spark_driver = SparkSession.builder.master("local[*]").appName("Spotify songs data").\
    config('spark.jars.package', 'mysql:mysql-connector-java:8.0.27').\
    getOrCreate()
query = '(select * from tracks order by release_year desc limit 10)'
url='jdbc:mysql://localhost:3306/Spotify'
user='root'
password='Nikhil@2000'

Full_load=spark_driver.read.format('jdbc').\
    option('url', url).\
    option('driver', 'com.mysql.cj.jdbc.Driver').\
    option('dbtable','Tracks').\
    option('user', user).\
    option('password', password).\
    load()

Full_load.show()
"""def Daily_Append(url,user,password):
    option('query','select  * from tracks  where track_id=(select max(track_id)+10 from tracks;')
   """

