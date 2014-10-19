#! /usr/bin/python
# Author: Jose R de la Vega
#email: j.r.delavega17@gmail.com
 
# Program to read a pcap file and output the unique
# source destination pairs.
 
import math
import sys
import os
from scapy.all import *

class Packet:
	def __init__(self, List):
		self.proto = List[0]
		self.src = List[1]
		self.dst = List[2]
		self.len = List[3]

# Checks if the user wants to use a specific amout of packets (currently not using it)
def checkOption():
	if len(sys.argv[2]) != 0:
		return True
	else:
		return False

# this function verifies the flag and if it is true then verifies that N is not greater than the ammount of packets in a flow
# if that is true then it evaluates all packets without taking in count N.
def checkFlagAndSize(lista):
	if flag:
		if N > len(lista):
			return False
		else:
			return True
	else:
		return False

# this function returns a list with the size of the first N packets
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
 
# this function returns the maximum size of the first N packets
def getMaxSize(lista):
	maximo = lista[0]
	for i in range(len(lista)):
		if(lista[i] > maximo):
			maximo = lista[i]
	return maximo
 
# this function returns the minimum size of the first N packets
def getMinSize(lista):
	minimo = lista[0]
	for i in range(len(lista)):
		if(lista[i] < minimo):
			minimo = lista[i]
	return minimo
 
# thisfunction returns the average size of the first N packets
def getAvgSize(lista):
	avg = 0
	for i in range(len(lista)):
		avg = avg + lista[i]
	avg = avg/len(lista)
	return avg
 
# this function returns the variance of the first N packet
def getVariance(lista, mean):
	lista2 = [] #list that will have the square of the difference
	for e in lista:
		e = pow(e - mean, 2)
		lista2.append(e)
	return getAvgSize(lista2)
 
# this function is to test that all the protocols of a flow are equal
def checkProto(lista):
	protocol = lista[0].proto
	for i in range(len(lista)):
		if protocol != lista[i].proto:
			return False
	return True

def GetPacketInfo(packet):
	pInfo = []
	pInfo.append(packet.proto)
	pInfo.append(packet["IP"].src)
	pInfo.append(packet["IP"].dst)
	pInfo.append(packet.len)
	
	return pInfo

 
#-----------------------------------------------------
if len(sys.argv) != 4:
	sys.exit("ERROR: %s needs exactly 4 parameters:\n %s <file to read> <N packets> <output file>" %(sys.argv[0], sys.argv[0]))
print("Reading files. Please wait...")
#st = sys.argv[1] + "*" + ".pcap"
f = os.listdir("./")
name = sys.argv[1]
filteredList = list( filter((lambda x: name in x ), f))
del f # f is not needed any more, let us clear some memory

M = {} # a dictionary to store different src, dst; represents a flow
countofFiles = 1
while len(filteredList):
	if len(filteredList[0]) == 0:
		continue
	x = rdpcap(filteredList[0])
	for i in range(len(x)):
		packet = Packet(GetPacketInfo(x[i]))
		sd = x[i]["IP"].dst + " - " + x[i]["IP"].src # string used as key for dictionary; dst + src
		if sd in M:
			M[sd].append(packet) # add a packet size to the corresponding flow
		else:
			M[sd] = [packet] # add to dictionary
						   				# a list with the 
										# packet of the new flow
	del filteredList[0] #i wont need the file i just read so let me clear it from filteredlist
	print "finished reading file", countofFiles
	countofFiles += 1
print("Finished.")


# this for counts how many pairs of src / dst are there of each one
#for i in range(len(a)):
#	sd = a[i]["IP"].dst + " - " + a[i]["IP"].src # string used as key for dictionary; dst + src
#	if sd in M:
#		M[sd].append(a[i]) # add a packet to the corresponding flow
#	else:
#		M[sd] = [a[i]] # add to dictionary
					   # a list with the 
					   # packet of the new flow
 
flag = checkOption()
if flag:
	N = sys.argv[2]
print

filename = sys.argv[3]
filename = filename + ".arff"
thefile = open(filename, "wb")

for key, value in M.iteritems():
	srcProto = value[0].proto
	srcPortNum = value[0].src
	dstPortNum = value[0].dst
	sizes = sizesOfNPackets(value)
	maxSize = getMaxSize(sizes)
	minSize = getMinSize(sizes)
	avgSize = getAvgSize(sizes)
	varianceSize = getVariance(sizes, avgSize)
	thefile.write(str(srcPortNum) + "," + str(dstPortNum) + "," + str(maxSize) + "," + str(minSize) + "," + str(avgSize) + "," + str(varianceSize) + "," + name + '\n')
	
#for key,value in M.iteritems():
# print key, ": ", len(value)
thefile.close()
print