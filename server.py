import folium 
import pandas as pd
from folium.plugins import MarkerCluster
import random as ra
l = pd.read_csv('C:\\Users\ASTRA\Desktop\cdr\cdrdata.csv',parse_dates=["time_stamp"])
length = len(l)



x0=[]
y0=[]
x1=[]
x2=[]
x3=[]
y1=[]
y2=[]
y3=[]

a0=[]
b0=[]
a1=[]
a2=[]
a3=[]
b1=[]
b2=[]
b3=[]

m = folium.Map(location=[28.60170452,77.41982998], zoom_start=12, tiles="Stamen Terrain")
for i in range(1,length):
    z = l.iloc[i]
    lat = z.latitude
    lng =z.longitude
    age = z.age
    if (z.age <= 20):
        x0.append(lat)
        y0.append(lng)
    elif((20 < age) and (age <= 30 )):
        x1.append(lat)
        y1.append(lng)
        
    elif(( 30< age) and (age <=40 )):
        x2.append(lat)
        y2.append(lng)
       
    elif((40 < age) and (age <=50 )):
         x3.append(lat)
         y3.append(lng)  
   
for i in range(0,5000):
    r0 = ra.randint(0,len(x0)) - 1
    r1 = ra.randint(0,len(x1))  - 1 
    r2 = ra.randint(0,len(x2))    -1  
    r3 = ra.randint(0,len(x3))-1
    
    
    a0.append(x0[r0])
    b0.append(y0[r0])
    
    a1.append(x1[r1])
    b1.append(y1[r1])
    
    a2.append(x2[r2])
    b2.append(y2[r2])
    
    a3.append(x3[r3])
    b3.append(y3[r3])
    

          
l0 = list(zip(a0,b0))   
l1 = list(zip(a1,b1))     
l2 = list(zip(a2,b2))   
l3 = list(zip(a3,b3)) 


icons0 = [folium.Icon(icon="car", color='red') for _ in range(len(l0))]
icons1 = [folium.Icon(icon="car", color='green') for _ in range(len(l1))]
icons2 = [folium.Icon(icon="car", color='blue') for _ in range(len(l2))]
icons3 = [folium.Icon(icon="car", color='black') for _ in range(len(l3))]

cluster0 = MarkerCluster(locations=l0, icons=icons0)
cluster1 = MarkerCluster(locations=l1, icons=icons1)    
cluster2 = MarkerCluster(locations=l2, icons=icons2)
cluster3 = MarkerCluster(locations=l3, icons=icons3)


fg_ac0 = folium.FeatureGroup(name="<20", show=False)
fg_ac0.add_child(cluster0)

fg_ac1 = folium.FeatureGroup(name="20-30", show=False)
fg_ac1.add_child(cluster1)

fg_ac2 = folium.FeatureGroup(name="30-40", show=False)
fg_ac1.add_child(cluster2)
fg_ac3 = folium.FeatureGroup(name="40-50", show=False)
fg_ac3.add_child(cluster3)


m.add_child(fg_ac0)

m.add_child(fg_ac1)

m.add_child(fg_ac2)

m.add_child(fg_ac3)

m.add_child(folium.LayerControl())

m.save('C:\\Users\\ASTRA\\Desktop\\newv3.html')

