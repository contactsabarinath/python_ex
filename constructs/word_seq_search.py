# program to check if the word has any forbidden letters

def avoid ( vstr,seq):
    for c in seq:
        if c in vstr:
            return (False,c)
    return (True,'')


word = input (" Enter the word\n")
seq = input(" Enter forbidden seq\n")

flag,char = avoid(word,seq)
if flag:
    print('{0} is free of {1}'.format(word,seq) )
else:
    print('{1} is a part of {0}'.format(word,char) )
