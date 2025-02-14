from pyspark.sql import SparkSession

if __name__ == "__main__":
    print(" Pyspark Application Started...")
    #initializting sparksession
    spark = SparkSession \
            .builder \
            .appName(" pySpark Demo") \
            .master("local[*]") \
            .getOrCreate()\

    spark.sparkContext.setLogLevel('INFO')

    DF=spark.read.csv("D:/datasets/MForecast.csv", multiLine=True)

    DF.show()

    spark.stop()
    print("pySpark  Application Completed. ")