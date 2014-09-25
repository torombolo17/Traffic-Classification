#! /usr/bin/python
# Author: Jose R de la Vega
#email: j.r.delavega17@gmail.com

# Program to read the data produced by flow.py and make
# a header in the format .arff about the data given


import math
import sys
import os

f = os.listdir("./")
name = sys.argv[1] #name of the file that you are going to open
thefile = filter((lambda x: name in x ), f)
thefile = thefile[0]
filename = raw_input("Enter the name you want to use for the file: ")

dataFile = open(thefile, "r")
content = []
for line in dataFile: #divides every line of the file and puts it in content
	attribute = line.split()
	content.append(attribute)
#print content

other = []

for e in content: #split the lines in content by a coma "," and put them in other
	other.append(e[0].split(","))
#print other

#make a list for every attribute
listSrcPort = []
listDestPort = []
listMax = []
listMin = []
listAvg = []
listVari = []
listApp = []

#for each list in other put the respective attribute in the attribute list
for lists in other:
	listSrcPort.append(lists[0])
	listDestPort.append(lists[1])
	listMax.append(lists[2])
	listMin.append(lists[3])
	listAvg.append(lists[4])
	listVari.append(lists[5])
	listApp.append(lists[6])

#change all the lists to sets so you only stay with the different values of each attribute
#then make it a list again so it's easier to work with
listSrcPort = list(set(listSrcPort))
listDestPort = list(set(listDestPort))
listMax = list(set(listMax))
listMin = list(set(listMin))
listAvg = list(set(listAvg))
listVari = list(set(listVari))
listApp = list(set(listApp))

dataFile.close() #close the file


#create the file that will contain the header
header = filename + "-header.arff"	
headerFile = open(header, "wb")
headerFile.write("@relation networkflows\n\n")

#create the header of the .arff file 
headerFile.write("@attribute sourcePortNumber {")
for i in range(len(listSrcPort)):
	if i == len(listSrcPort)-1:
		headerFile.write(listSrcPort[i])
	else:
		headerFile.write(listSrcPort[i]+",")
headerFile.write("}\n")

headerFile.write("@attribute destinationPortNumber {")
for i in range(len(listDestPort)):
	if i == len(listDestPort)-1:
		headerFile.write(listDestPort[i])
	else:
		headerFile.write(listDestPort[i]+",")
headerFile.write("}\n")

headerFile.write("@attribute maximumSize {")
for i in range(len(listMax)):
	if i == len(listMax)-1:
		headerFile.write(listMax[i])
	else:
		headerFile.write(listMax[i]+",")
headerFile.write("}\n")

headerFile.write("@attribute minimumSize {")
for i in range(len(listMin)):
	if i == len(listMin)-1:
		headerFile.write(listMin[i])
	else:
		headerFile.write(listMin[i]+",")
headerFile.write("}\n")

headerFile.write("@attribute averageSize {")
for i in range(len(listAvg)):
	if i == len(listAvg)-1:
		headerFile.write(listAvg[i])
	else:
		headerFile.write(listAvg[i]+",")
headerFile.write("}\n")

headerFile.write("@attribute varianceOfSizes {")
for i in range(len(listVari)):
	if i == len(listVari)-1:
		headerFile.write(listVari[i])
	else:
		headerFile.write(listVari[i]+",")
headerFile.write("}\n")

headerFile.write("@attribute application {")
for i in range(len(listApp)):
	if i == len(listApp)-1:
		headerFile.write(listApp[i])
	else:
		headerFile.write(listApp[i]+",")
headerFile.write("}\n")
headerFile.write("\n")

headerFile.write("@data\n")
headerFile.close()