from pyspark.sql.session import SparkSession

spark = SparkSession.builder.master("local[*]").appName("MY").\
    config('spark.jars.package','org.mongodb.spark:mongo-java-driver-3.12.10' ).\
    getOrCreate()

df= spark.read.format('jdbc').\
           option('url', 'jdbc:"mongodb://localhost:27017/mydatabase."').\
           option('driver', 'com.mongodb.jdbc.Drive').\
           option('dbtable','Superstore').\
           load()
df.show()

