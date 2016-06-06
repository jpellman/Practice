#! /usr/bin/python
# Matroska.py
# Authored by John Pellman
# Birthday: April 21st, 2014
# Last Revision: April 21st, 2014

# Takes each letter of a string and nests it in a directory whose name is the previous letter, like a Russian Matroska doll.

import os, sys


dollStr = ""

if len(sys.argv) > 1:
	dollStr = sys.argv[1]

while not dollStr:
	dollStr = raw_input("Please give me a string whose letters you would like to nest within one another (much like a Matroska doll: ")

currentDir = os.getcwd()
for letter in dollStr:
	currentDir=currentDir+"/"+letter
	os.mkdir(currentDir)
	
