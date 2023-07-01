import pandas as pd
import shapefile
import geopandas as gpd
import matplotlib.pyplot as plt

file = 'sample01.csv'
num_polygons = pd.read_csv('sampl2.csv')
random_numbers = pd.read_csv('sorted_numbers.csv')
# num_polygons['y3'] = num_polygons['y1'].iloc[random_numbers['y'].values.tolist()]
num_polygons['y2'] = num_polygons['y1'].iloc[num_polygons['index_y'].sort_values(
).index].reset_index(drop=True)
num_polygons.drop('y1', axis=1, inplace=True)
num_polygons.drop('index_y', axis=1, inplace=True)

num_polygons['x2'] = num_polygons['x1'].iloc[num_polygons['index_x'].sort_values(
).index].reset_index(drop=True)
num_polygons.drop('x1', axis=1, inplace=True)
num_polygons.drop('index_x', axis=1, inplace=True)

num_polygons.to_csv(file, sep=',', index=False)


FILE_HEADER = ['x2', 'y2']
USE_COLS = ['x2', 'y2']
w = shapefile.Writer('LBY_adm0.shp', shapeType=5)
w.autoBalance = 1
w.field("longitude", "C", "40")
w.field("latitude", "C", "40")
df = pd.read_csv("sample01.csv", delimiter=",", usecols=USE_COLS)
geometry = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(
    df['x2'], df['y2']), crs='EPSG:4326')
for i in range(len(geometry)):
    if i > 0:
        w.record(geometry["x2"][0], geometry["y2"][0])
        wkt = geometry["geometry"][9:-2]
        coords = wkt
        part = []
for c in coords:
    z = str(c).replace('(', '').replace(')', '')
    a, x2, y2 = z.split(" ")
    part.append([float(x2), float(y2)])
w.poly([part])
w.close()

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
