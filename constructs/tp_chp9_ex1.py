# string manipulation

import os

os.chdir('c:\python34\sab\swampy')

def has_no_e(vstr):
    if 'e' not in vstr:
        return True
    else:
        return False

def count_no_e(lst):
    noe = 0
    for word in lst:
        if 'e' not in word:
            noe = noe+1
    return noe


fin = open('words.txt','r')
lines = fin.readlines()
tot = len(lines)
cnt = count_no_e(lines)
print ( 'Total words in the file is {}'.format(tot) )
print ( 'Total words with no e is {}'.format(cnt)   )
print ( 'Percentage of words with no e is {:.2%}'.format( cnt/tot)) 
          
          
'''          
word = input ('Enter a word \n')
result = has_no_e(word)
if result:
    print ("{0} has no 'e'".format(word))
else:
    print ("{0} has 'e'".format(word))
'''
    
