#Import Required PySpark Packages
from pyspark.sql import SparkSession

if __name__ == "__main__":
    print("Application Started ...")

    spark = SparkSession \
            .builder \
            .appName("First pySpark Demo") \
            .master("local[*]") \
            .getOrCreate()\

    input_File_path  ="file:///D://datasets//sample.txt"

    tech_rdd = spark.sparkContext.textFile(input_File_path)

    print("Printing data in the tech_rdd: ")
    print(tech_rdd.collect())

    print("Application completed.")
