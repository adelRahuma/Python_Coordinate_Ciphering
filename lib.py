import shapefile
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

sf = shapefile.Reader("./data/Libya/LBY_adm0.shp")

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
    out = os.path.splitext("./data/Libya/LBY_adm0.shp")[0]+'_pnts.csv'
    with open(out, 'w') as csv:
           with shapefile.Reader("./data/Libya/LBY_adm0.shp") as sf1:
              for shp_rec in sf1.shapeRecords():
                print(shp_rec)
                #com_id =sf.fields == [ 'Libya'].index.get_values()
                csv.write('{}\n'.format(shp_rec.record))
                for pnt in shp_rec.shape.points:
                    csv.write('{}\n'.format(pnt))

df = pd.DataFrame({'X': xt, 'Y': yt, 'ID':i}) # 'ID':tt
df = df.rename(columns={0: "X1", 1: "X2"})

print(df.head())

# plotting the data
plt.plot(xt, yt)
# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()