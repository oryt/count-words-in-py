#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A script that reads a file and prints a list of the 100 most used words in the file

# Copyright 2016 Oscar Ydrefelt
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

wordList =[]
wordListClean = []
wordDic = {}
wordDicSort = {}
theList = []

fileName =  raw_input("Please enter filename ")

# uses try to checks file and Prints error message if the file is not found
try:
	theBook = file(fileName)
	readBook = theBook.read()
	splitBook = readBook.split() # Splits the read content to a list with space as delimeter   

	for word in splitBook: # runs over the list appends each word to list
		wordList.append(word)
except IOError:
	print 'Sorry, the file does not exist.'

for entry in wordList: # runs over the list removes unwanted charachters
	cleanList = entry.replace(',', '').replace('.', '').replace(';' , '').replace('!' , '').replace('\"' , '')
	wordListClean.append(cleanList)

for wd in wordListClean: # runs over the list and creates dic with each unique word as key and the words ocurance in the text as value   
    if not wd in wordDic:
        wordDic[wd] = 1
    else:
        wordDic[wd] += 1

# As a dic has no order and hence cant be sorted we use lambda to create a one time function that points the sorted function to
# use the the second element as the key which in this case it the value for the reourance of the word as listed in the dic       
sortedByValueDict = sorted(wordDic.items(), key = lambda t:t[1])
# pushes the sorted data to a list
for l in sortedByValueDict:
	theList.append(l)

# reverse the list and pushes the 100 first entries to list
theList.reverse()
Top100 = theList[0:100]

# loops over the list removes unwanted charchters and prints each entry 
for things in Top100: 
	stuff = str(things)
	removeStuff = stuff.replace('(', '').replace(')' , '').replace('"' , '').replace(',' , '').replace('\'' , '')
	print (removeStuff)
