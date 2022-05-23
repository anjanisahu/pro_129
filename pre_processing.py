import csv 
data1=[] 
data2=[]
with open("planets2.csv","r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        data1.append(i)

headers=data1[0] 
planet_data=data1[1:]
#iss mein ham words ko small letters mein kar rhe h
for i in planet_data:
    i[2]=i[2].lower()
    
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("dataset_2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planet_data)
    
         
        
    
    
    
        