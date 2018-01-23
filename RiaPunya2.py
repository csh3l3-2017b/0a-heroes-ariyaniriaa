import csv
import random
import math
import operator
import time
import xlsxwriter


dataTrain = []
role =[]
name = []
newFile =[]
a = 'MARKSMAN'
b = 'MAGE'
c = 'TANK'
d = 'ASSASIN'
e = 'FIGHTER'
f = 'SUPPORT'

#Load Data CSV
def DataTrain('test.csv', dataTrain=[]):
	with open('test.csv','rb') as csvfile:
    	barisData = csv.reader(csvfile)
    	next(barisData,None)
    	dataset = list(barisData)
    		for i in range(len(dataset)):
        	dataTrain.append(dataset[i])

DataTrain('test.csv', trainingSet);
#Implementasi Rule
for i in range(len(dataTrain)):
	name.append(dataTrain[i][0])
	if int(dataTrain[i][5]) >= 500 :
		role.append(b)
	elif int(dataTrain[i][1]) >= 270 :
		
		role.append(a)
	elif int(dataTrain[i][3]) >= 25 :
		
		role.append(c)
	elif int(dataTrain[i][2]) >= 121 :
		
		role.append(d)
	elif int(dataTrain[i][4]) >= 2580 :
		
		role.append(e)
	else :
		
		role.append(f)
	newFile.append([name[i],role[i]])

#Save File CSV
with open('prediction.csv', 'wb') as csvfile:
    fieldnames = ['Name', 'Role']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(newFile)):
    	writer.writerow({'Name': newFile[i][0], 'Role': newFile[i][1]})


