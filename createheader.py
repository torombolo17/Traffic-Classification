#! /usr/bin/python
# Author: Jose R de la Vega
#email: j.r.delavega17@gmail.com

import math
import sys
import os

f = os.listdir("./")
name = sys.argv[1]
thefile = filter((lambda x: name in x ), f)
thefile = thefile[0]
filename = raw_input("Enter the name you want to use for the file: ")

dataFile = open(thefile, "r")
content = []
for line in dataFile:
	attribute = line.split()
	content.append(attribute)
#print content

other = []

for e in content:
	other.append(e[0].split(","))
#print other

listProto = []
listSrcPort = []
listDestPort = []
listMax = []
listMin = []
listAvg = []
listVari = []
listApp = []

for lists in other:
	listProto.append(lists[0])
	listSrcPort.append(lists[1])
	listDestPort.append(lists[2])
	listMax.append(lists[3])
	listMin.append(lists[4])
	listAvg.append(lists[5])
	listVari.append(lists[6])
	listApp.append(lists[7])

listProto = list(set(listProto))
listSrcPort = list(set(listSrcPort))
listDestPort = list(set(listDestPort))
listMax = list(set(listMax))
listMin = list(set(listMin))
listAvg = list(set(listAvg))
listVari = list(set(listVari))
listApp = list(set(listApp))

dataFile.close()

header = filename + "-header.arff"	
headerFile = open(header, "wb")
headerFile.write("@relation networkflows\n")
headerFile.write("@attribute protocol {")
for i in range(len(listProto)):
	if i == len(listProto)-1:
		headerFile.write(listProto[i])
	else:
		headerFile.write(listProto[i]+",")
headerFile.write("}\n")

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
headerFile.write("}\n")

headerFile.write("@data\n")
headerFile.close()