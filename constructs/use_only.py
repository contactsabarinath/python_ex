#program to check if the word consists only of given sequence

import get_dic

def uses_only(d1):
    lstr = d1['word']
    lseq = d1['seq']
    if lstr.strip(lseq) == '':
        return (True,'')
    else:
        return (False,lstr.strip(lseq))

def uses_all(d1):
    lstr = d1['word']
    lseq = d1['seq']
    if lseq.strip(lstr) == '':
        return (True,'')
    else:
        return (False,lseq.strip(lstr))
    
print('Program for this input: enter a word and seq as a pair')
d = get_dic.get_val()
print('Entered word is {0} and seq is {1}'.format(d['word'],d['seq']))


result,vstr = uses_only(d)
if result:
    print ('The word : {0} uses only the letters from {1}'.format(d['word'],d['seq']))
else:
    print ('The word : {0} uses letters {2} in addition to {1}'.format(d['word'],d['seq'],vstr))

print ('{:*^90}'.format('*'))

result,vstr = uses_all(d)
if result:
    print ('The word : {0} uses all the letters from {1}'.format(d['word'],d['seq']))
else:
    print ('The word : {0} uses does not use the letters {2} in addition to {1}'.format(d['word'],d['seq'],vstr))
    
#print (d)
