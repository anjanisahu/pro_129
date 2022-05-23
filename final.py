import csv
data_set1=[]
data_set2=[]
with open("dataset_2_sorted.csv","r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        data_set2.append(i)

with open("planets.csv","r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        data_set1.append(i)   
        
header1=data_set1[0] 
planet_data1=data_set1[1:]

header2=data_set2[0]
planet_data2=data_set2[1:]     

headers=header1+header2
planet_data=[]

for index , data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planet_data)

    
    
    
         
        