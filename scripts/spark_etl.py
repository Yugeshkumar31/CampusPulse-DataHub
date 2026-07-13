from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour

spark = SparkSession.builder.appName("CampusPulse").getOrCreate()
print("STARTED")

students = spark.read.csv("/app/data/raw/students.csv", header=True, inferSchema=True)
library = spark.read.csv("/app/data/raw/library.csv", header=True, inferSchema=True)

print("DATA LOADED")

print("Students:", students.count())
print("Library:", library.count())

library = library.withColumn("entry_time", col("entry_time").cast("timestamp"))
library = library.withColumn("exit_time", col("exit_time").cast("timestamp"))

library = library.withColumn(
    "duration",
    (col("exit_time").cast("long") - col("entry_time").cast("long")) / 3600
)

library = library.withColumn("hour", hour(col("entry_time")))

print("TRANSFORM DONE")

library.write.mode("overwrite").csv("/app/data/processed/library_clean", header=True)
students.write.mode("overwrite").csv("/app/data/processed/students_clean", header=True)

print("DONE")