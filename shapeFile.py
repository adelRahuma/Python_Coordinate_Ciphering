import shapefile as shp
import os
import csv
import matplotlib.pyplot as plt
shape = shp.Reader("./data/Libya/LBY_adm0.shp")
#first feature of the shapefile
sf = shp.Reader(shape)
feature = shape.shapeRecords()[0]
first = feature.shape.__geo_interface__  
shape.shapes()
print(shape.shapeType,len(shape))
def shp2csv(shp_file):
    '''Outputs a csv file based on input shapefile vertices'''
    out = os.path.splitext(shp_file)[0]+'_pnts.csv'
    with open(out, 'w') as csv:
        with shp.Reader(shp_file) as sf:
            for shp_rec in sf.shapeRecords():
                #com_id =sf.fields == [ 'Libya'].index.get_values()
                csv.write('{}\n'.format(shp_rec.record))
                for pnt in shp_rec.shape.points:
                    csv.write('{}\n'.format(pnt))

def createShapeFile():
    out_file = 'GPS_Pts.shp'

    #Set up blank lists for data
    x,y,id_no,date,target=[],[],[],[],[]
    print('jjjjjjjjjjjjjjjjjjjjjjjjjjjj')
    #read data from csv file and store in lists
    with open('./data/World_Countries_pnts.csv', 'rb') as csvfile:
      r = csv.reader(csvfile, delimiter=',')
      for i,row in enumerate(r):
         if i > 0: #skip header
            x.append(float(row[3]))
            y.append(float(row[4]))
            id_no.append(row[0])
            date.append(''.join(row[1].split('-')))#formats the date correctly
            target.append(row[2])
            print(shp.POINT,'<<-----')
            #break
#Set up shapefile writer and create empty fields
    w = shp.Writer(shp.POINT)
    w.autoBalance = 1 #ensures gemoetry and attributes match
    w.field('X','F',10,8)
    w.field('Y','F',10,8)
    w.field('Date','D')
    w.field('Target','C',50)
    w.field('ID','N')
   
    #loop through the data and write the shapefile
    for j,k in enumerate(x):
     w.point(k,y[j]) #write the geometry
     w.record(k,y[j],date[j], target[j], id_no[j]) #write the attributes
    
    #Save shapefile
    w.save(out_file)
shp2csv('./data/Libya/LBY_adm0.shp')
#createShapeFile()