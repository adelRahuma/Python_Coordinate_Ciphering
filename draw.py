import csv
import shapefile
import pandas as pd
import geopandas as gpd


from shapely.geometry import Point
from geopandas import GeoDataFrame
#import pandas as pd
FILE_HEADER = [ 'x', 'y']
USE_COLS = [ 'x', 'y']

# Create a polygon shapefile writer
w = shapefile.Writer('LBY_adm0.shp',shapeType=5)
w.autoBalance = 1
w.field("longitude", "C", "40")
w.field("latitude", "C", "40")
df = pd.read_csv("sample.csv", delimiter=",",usecols=USE_COLS)
geometry = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df['x'], df['y']),crs = 'EPSG:4326')
for i in range(len(geometry)):
        if i>0:
            w.record(geometry["x"][0],geometry["y"][0])
            wkt = geometry["geometry"][9:-2]
            coords = wkt
            part = []
for c in coords:
    z = str(c).replace('(','').replace(')','')
    a,x,y = z.split(" ")
    part.append([float(x),float(y)])
    # create a polygon record with the list of coordinates.
w.poly([part])
#w.save("polys.shp")
w.close()

