from pyspark.sql import SparkSession

if __name__ == "__main__":
    print("Hello, Pyspark Application Started...")
    #initializting sparksession
    spark = SparkSession \
            .builder \
            .appName(" pySpark Demo") \
            .master("local[*]") \
            .getOrCreate()\

    spark.sparkContext.setLogLevel('INFO')

    StudentDF=spark.read.json("D:/datasets/StudentJson.json", multiLine=True)

    StudentDF.show()

    spark.stop()
    print("pySpark Demo Application Completed. ")