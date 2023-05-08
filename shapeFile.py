import shapefile 
import os
import pandas as pd
import csv
import matplotlib.pyplot as plt

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

df = pd.DataFrame({'X': xt, 'Y': yt, 'ID':i}) # 'ID':tt
df = df.rename(columns={0: "X1", 1: "X2"})
print(df.head())

pd.DataFrame(yt,xt).to_csv('sample.csv') 
plt.plot(xt, yt)
# Adding the title
plt.title("Simple Plot")
# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()
