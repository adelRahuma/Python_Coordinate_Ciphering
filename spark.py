import shapefile
import time
import random
import os
import csv
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import FloatType
import geopandas as gpd
import matplotlib.pyplot as plt

def process_1(df, random_numbers, random_nums):
    df = df.withColumn('y1', col('y').getItem(col('random_numbers')))
    df = df.drop('y').drop('random_numbers')
    df = df.withColumn('index_y', col('random_numbers'))
    return df


def process_2(df, random_nums):
    df = df.withColumn('x1', col('x').getItem(col('random_nums')))
    df = df.drop('x').drop('random_nums')
    df = df.withColumn('index_x', col('random_nums'))
    return df


start_time = time.perf_counter()

# Initialize SparkSession
spark = SparkSession.builder.appName("ShapefileProcessing").getOrCreate()

sf = shapefile.Reader("./data/Libya/LBY_adm1.shp")
Polygon_Number = len(sf)
print(Polygon_Number, "Polygons")

xt = []
yt = []
for i in range(0, Polygon_Number):
    Vertices_Number = len(sf.shape(i).points)
    print(Vertices_Number, "Vertices")
    xx = [x for x, y in sf.shape(i).points]
    yy = [y for x, y in sf.shape(i).points]

    xt.extend(xx)
    yt.extend(yy)

# Create Spark DataFrame from the shapefile data
df = spark.createDataFrame(zip(xt, yt), schema=["x", "y"])

# Save DataFrame as a temporary table for Spark SQL operations
df.createOrReplaceTempView("sample")

# Code block to measure execution time
# ...

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

# Now generate random list for all vertices
num_polygons = df.count()
random_numbers = random.sample(range(0, num_polygons), num_polygons)
random_nums = random.sample(range(0, num_polygons), num_polygons)

# Save random numbers as a CSV file
with open("sorted_numbers.csv", mode="w", newline="") as random_nums_file:
    writer = csv.writer(random_nums_file)
    writer.writerow(["y", "x"])
    for num, nums in zip(random_numbers, random_nums):
        writer.writerow([num, nums])

# Perform data processing using Spark DataFrame transformations
df = df.withColumn("random_numbers", col("row_number").cast(FloatType()))
df = df.withColumn("random_nums", col("row_number").cast(FloatType()))

# Perform process_1 using Spark DataFrame transformations
df = process_1(df, random_numbers, random_nums)

# Perform process_2 using Spark DataFrame transformations
df = process_2(df, random_nums)

# Save processed DataFrame as CSV
df.toPandas().to_csv('sample.csv', index=False)

# Create the shapefile from the encrypted coordinates
FILE_HEADER = ['x1', 'y1']
USE_COLS = ['x1', 'y1']
w = shapefile.Writer('LBY_adm0.shp', shapeType=5)
w.autoBalance = 1
w.field("longitude", "C", "40")
w.field("latitude", "C", "40")

# Read processed DataFrame from CSV
df = spark.read.csv('sample.csv', header=True)

# Create GeoDataFrame from Spark DataFrame
geometry = gpd.GeoDataFrame(df.toPandas(), geometry=gpd.points_from_xy(df['x1'], df['y1']), crs='EPSG:4326')

for i in range(len(geometry)):
    if i > 0:
        w.record(geometry["x1"][0], geometry["y1"][0])
        wkt = geometry["geometry"][9:-2]
        coords = wkt
        part = []

for c in coords:
    z = str(c).replace('(', '').replace(')', '')
    a, x1, y1 = z.split(" ")
    part.append([float(x1), float(y1)])

w.poly([part])
w.close()

# Draw the shape
shpFilePath = "LBY_adm0.shp"
listx = []
listy = []
test = shapefile.Reader(shpFilePath)
for sr in test.shapeRecords():
    for xNew, yNew in sr.shape.points:
        listx.append(xNew)
        listy.append(yNew)

plt.plot(listx, listy)
plt.show()

# Stop SparkSession
spark.stop()
