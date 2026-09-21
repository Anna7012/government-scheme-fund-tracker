from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, max, min, col, when

spark = SparkSession.builder \
    .appName("GovernmentFundTracker") \
    .master("local[*]") \
    .getOrCreate()

# Read cleaned data
df = spark.read.csv(
    "file:///home/anna/bigdata_project/github_project/data/processed/mgnrega_expenditure_clean.csv",
    header=True,
    inferSchema=True
)

print("=== DATA ===")
df.show()

print("=== SCHEMA ===")
df.printSchema()

# Year-wise expenditure
yearwise = df.groupBy("Financial_Year") \
    .agg(sum("Expenditure_Crore").alias("Total_Expenditure"))

print("=== YEAR-WISE EXPENDITURE ===")
yearwise.orderBy("Financial_Year").show()

# District-wise expenditure
districtwise = df.groupBy("District") \
    .agg(sum("Expenditure_Crore").alias("Total_Expenditure"))

print("=== DISTRICT-WISE EXPENDITURE ===")
districtwise.orderBy(col("Total_Expenditure").desc()).show()

# Average expenditure
average = df.groupBy("District") \
    .agg(avg("Expenditure_Crore").alias("Average_Expenditure"))

print("=== DISTRICT AVERAGE ===")
average.orderBy("Average_Expenditure").show()

# Highest and lowest expenditure
print("=== HIGHEST EXPENDITURE ===")
df.orderBy(col("Expenditure_Crore").desc()).show(1)

print("=== LOWEST EXPENDITURE ===")
df.orderBy(col("Expenditure_Crore")).show(1)

# Underutilisation
overall_avg = df.select(avg("Expenditure_Crore")).first()[0]

result = average.withColumn(
    "Utilization_Level",
    when(col("Average_Expenditure") < overall_avg * 0.8, "Low")
    .when(col("Average_Expenditure") <= overall_avg * 1.2, "Medium")
    .otherwise("High")
)

print("=== UTILIZATION LEVEL ===")
result.orderBy("Average_Expenditure").show()

spark.stop()
