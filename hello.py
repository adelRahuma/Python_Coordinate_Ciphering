import shapefile
import os
shape = shapefile.Reader("./data/World_Countries.shp")
#first feature of the shapefile
feature = shape.shapeRecords()[0]
first = feature.shape.__geo_interface__  
shape.shapes()
# for shp_rec in shape.shapeRecords():
#                 print('{}\n'.format(shp_rec.record))

#                 for pnt in shp_rec.shape.points:
#                    print('{}\n'.format(pnt))
print(shape.shapeType,len(shape))
def hi(a,b):
    return a+b

def shp2csv(shp_file):
    '''Outputs a csv file based on input shapefile vertices'''
    
    out = os.path.splitext(shp_file)[0]+'_pnts.csv'

    with open(out, 'w') as csv:
        with shapefile.Reader(shp_file) as sf:

            for shp_rec in sf.shapeRecords():
                csv.write('{}\n'.format(shp_rec.record))

                for pnt in shp_rec.shape.points:
                    csv.write('{}\n'.format(pnt))


x= hi(3,6) 
print('\n hello world \n',x)
shp2csv('./data/World_Countries.shp')