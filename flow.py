#! /usr/bin/python
# Author: Jose R de la Vega
#email: j.r.delavega17@gmail.com
 
# Program to read a pcap file and output the unique
# source destination pairs.
 
import math
import sys
import os
from scapy.all import *

# esta funcion pide como input si deseas evaluar los primeros N paquetes de un flow 
def checkOption():
	if len(sys.argv[2]) != 0:
		return True
	else:
		return False

# esta funcion verifica el flag y si este es cierto entonces verifica que N no sea mayor que la cantidad de paquetes en un flow
# de ser asi los evalua todos aunque no cupla con N.
def checkFlagAndSize(lista):
	if flag:
		if N > len(lista):
			return False
		else:
			return True
	else:
		return False

 
# esta funcion devuelve una lista con los tama~os de los primeros N paquetes
def sizesOfNPackets(lista):
	listSizes = [] # lista a devolver
	
	if checkFlagAndSize(lista):
		for i in range(0, N):
			listSizes.append(lista[i].len)
		return listSizes
	else:
		for i in range(len(lista)):
			listSizes.append(lista[i].len)
		return listSizes
 
# esta funcion devuelve el tama~o maximo entre los primeros N paquetes
def getMaxSize(lista):
	maximo = lista[0]
	for i in range(len(lista)):
		if(lista[i] > maximo):
			maximo = lista[i]
	return maximo
 
#esta funcion devuelve el tama~o minimo entre los primeros N paquetes
def getMinSize(lista):
	minimo = lista[0]
	for i in range(len(lista)):
		if(lista[i] < minimo):
			minimo = lista[i]
	return minimo
 
#esta funcion devuelve el promedio de tama~o de los primeros N paquetes
def getAvgSize(lista):
	avg = 0
	for i in range(len(lista)):
		avg = avg + lista[i]
	avg = avg/len(lista)
	return avg
 
#esta funcion devuelve el variance de tama~os de los primeros N paquetes
def getVariance(lista, mean):
	lista2 = [] #lista que va a contener el queadrado de la diferencia
	for e in lista:
		e = pow(e - mean, 2)
		lista2.append(e)
	return getAvgSize(lista2)
 
#esta funcion es para probar que todos los protocols de un flow sean iguales
def checkProto(lista):
	protocol = lista[0].proto
	for i in range(len(lista)):
		if protocol != lista[i].proto:
			return False
	return True
 
#-----------------------------------------------------
if len(sys.argv) != 4:
	sys.exit("ERROR: %s needs exactly 4 parameters:\n %s <file to read> <N packets> <output file>" %(sys.argv[0], sys.argv[0]))
print("Reading files. Please wait...")
#st = sys.argv[1] + "*" + ".pcap"
a = []
f = os.listdir("./")
name = sys.argv[1]
filteredList = list( filter((lambda x: name in x ), f))
#contofFiles = 1
for filename in filteredList:
	x = rdpcap(filename)
	a.extend(x)
#	print "finished reading file", contofFiles
#	contofFiles = contofFiles + 1
print("Finished.")
print
print "Packets: ", len(a)
M = {} # un mapa para guardar src, dst distintos; representa un flow

# el siguiente for cuenta cuantos pares de src / dst hay de cada uno
for i in range(len(a)):
	sd = a[i]["IP"].dst + " - " + a[i]["IP"].src # un string compuesto del dst + src
	if sd in M:
		M[sd].append(a[i]) # a~adir paquete al flow correspondiente
	else:
		M[sd] = [a[i]] # a~ade al mapa
					   # una lista con el
					   # paquete del flow nuevo
 
flag = checkOption()
if flag:
	N = sys.argv[2]
print

filename = sys.argv[3]
filename = filename + ".arff"
thefile = open(filename, "wb")

for key, value in M.iteritems():
	srcProto = value[0].proto
	srcPortNum = value[0]["IP"].src
	dstPortNum = value[0]["IP"].dst
	sizes = sizesOfNPackets(value)
	maxSize = getMaxSize(sizes)
	minSize = getMinSize(sizes)
	avgSize = getAvgSize(sizes)
	varianceSize = getVariance(sizes, avgSize)
	thefile.write(str(srcProto) + "," + str(srcPortNum) + "," + str(dstPortNum) + "," + str(maxSize) + "," + str(minSize) + "," + str(avgSize) + "," + str(varianceSize) + "," + name + '\n')
	
#for key,value in M.iteritems():
# print key, ": ", len(value)
thefile.close()
print