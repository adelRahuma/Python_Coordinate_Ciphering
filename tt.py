import shapefile
import pandas as pd
from tkinter import *
import time
import concurrent.futures
import matplotlib.pyplot as plt
import random
import os
import csv
import geopandas as gpd


def process_1(df, random_numbers, random_nums):
    df['y1'] = df['y'].iloc[random_numbers].values
    df.drop('y', axis=1, inplace=True)
    df['index_y'] = random_numbers
    return df


def process_2(df, random_nums):
    df['x1'] = df['x'].iloc[random_nums].values
    df.drop('x', axis=1, inplace=True)
    df['index_x'] = random_nums
    return df


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
df = pd.DataFrame({'x': xt, 'y': yt})
df.to_csv('sample.csv')
plt.plot(xt, yt)
plt.title("Simple Plot")
plt.ylabel("y-axis")
plt.xlabel("x-axis")


# Code block to measure execution time
# ...


plt.show()

start_time = time.perf_counter()
# Now generate random list for all vertices


file = 'sampl2.csv'
if (os.path.exists(file) and os.path.isfile(file)):
    os.remove(file)

num_polygons = pd.read_csv("sample.csv")
random_numbers = random.sample(range(0, len(num_polygons)), len(num_polygons))
random_nums = random.sample(range(0, len(num_polygons)), len(num_polygons))

with open("sorted_numbers.csv", mode="w", newline="") as random_nums_file:
    writer = csv.writer(random_nums_file)
    writer.writerow(["y", "x"])
    for num, nums in zip(random_numbers, random_nums):
        writer.writerow([num, nums])

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_1 = executor.submit(
            process_1, num_polygons, random_numbers, random_nums)
        future_2 = executor.submit(process_2, num_polygons, random_nums)

        result_1 = future_1.result()
        result_2 = future_2.result()

cc = result_1
cc.to_csv(file, sep=',', index=False)

# Create the shapefile from the encrypted coordinates
FILE_HEADER = ['x1', 'y1']
USE_COLS = ['x1', 'y1']
w = shapefile.Writer('LBY_adm0.shp', shapeType=5)
w.autoBalance = 1
w.field("longitude", "C", "40")
w.field("latitude", "C", "40")
# encrypted coordinates file
df = pd.read_csv("sampl2.csv", delimiter=",", usecols=USE_COLS)
geometry = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(
    df['x1'], df['y1']), crs='EPSG:4326')
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

# draw the shape
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
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")