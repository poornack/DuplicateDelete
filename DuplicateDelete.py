#**********************************
#Author:  Poorna Chander Kalidas
#**********************************

import hashlib
import os
import glob
import string

#*************
#  Begin Def
#*************

#Print a Dict where its elements are Strings. Options param indent to set the number of spaces to put in front of a line      
def printDict(inputDict, indent = 0):
    
    space = ""
    
    for x in range(indent):
        space += " "
    
    for keys,values in inputDict.items():
        print space + keys + "      " + values

#Print the duplicate Dict findDuplicates() returns.   
def printDuplicateDict(inputDict):

    for keys,values in inputDict.items():
        #print keys + ":   "
        print "{}:".format(keys)
        for filename in values:
            print "    {}".format(filename)
            
        print ""
        
#Finds duplicates and enters it in a Dict and returns it     
def findDuplicates(inputDict):
    
    dictOfDuplicates = {}
    
    numberOfDuplicates = 0
    duplicateFound = 0
    
    
    for keyOriginal,valueOriginal in inputDict.items():
        
        listOfDuplicates = []
        
        for keyComparer,valueComparer in inputDict.items():
            if valueOriginal == valueComparer and keyOriginal != keyComparer:
                
                listOfDuplicates.append(keyComparer)
                del inputDict[keyComparer]
                duplicateFound = 1
        
        if duplicateFound == 1:
            numberOfDuplicates += 1;
            listOfDuplicates.append(keyOriginal)
            dictOfDuplicates[numberOfDuplicates] = listOfDuplicates
            
            del inputDict[keyOriginal]
            duplicateFound = 0
            
            
            
    return dictOfDuplicates
#*************
#  End Def
#*************

#****************
#  Begin Script
#****************

#Has to be entered the as the parameters for glob. Not used at the moment
fileTypesToCheck = ["*.jpg", "*.MTS"] 

directoryToCheck = raw_input("Enter the directory to check: ")

#Change working directory to inputted value
os.chdir(directoryToCheck)

#Add file extention to check. This is case sensitive
listOfJpgAndMts = []
listOfJpgAndMts.extend(glob.glob("*.JPG"))
listOfJpgAndMts.extend(glob.glob("*.jpg"))
listOfJpgAndMts.extend(glob.glob("*.MTS"))
listOfJpgAndMts.extend(glob.glob("*.mts"))

#Initialize dict to hold file name and crc
crc = {}

#Calculate crc for each file in  list and store in dict
for file in listOfJpgAndMts:
    m = hashlib.md5()
    m.update(open(file, 'rb').read())
    crc[file] = m.hexdigest()

print "List of JPGs and MTS files in directory:"
printDict(crc, 6)
print "\n"

#Find duplicates
dictOfDuplicates = findDuplicates(crc)
print "List of duplicated found:"
printDuplicateDict(dictOfDuplicates)


#Deleting duplicate files is yet to be implemented

#****************
#  End Script
#****************
    
