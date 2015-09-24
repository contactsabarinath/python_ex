# program to find out if the words uses only the string of letters

import os
import math
import linecache
os.chdir('c:\python34\sab\swampy')
ltr =  input('Enter string of letters\n')

#http://stackoverflow.com/questions/2081836/reading-specific-lines-only-python

# to read particular line 4 from a file : say from config file to get pwd
vstr = linecache.getline('c:\python34\sab\swampy\words.txt',4)
print(vstr)



# If the file to read is big, and
# you don't want to read the whole file in memory at once:
# it reads sequentially from disk and hence slower

fin = open('words.txt')
for i,line in enumerate(fin):
    if i == 25:
        print (line)


# read the fle and place into memory as a list
fo = open('words.txt')
lines = fo.readlines()
print ( len (lines) )
print (type(lines) )
print (lines[28] )
print (lines[30] )
        

# read entire file into memory for random access
fin = open('words.txt')
for line in fin:
    #print(line.rstrip())
    #print ( type(line) )
    pass
fin.close()
