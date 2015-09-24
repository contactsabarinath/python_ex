# program for string manipulation

'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__',
 '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'capitalize', 'casefold', 'center', 'count',
 'encode', 'endswith', 'expandtabs',
 'find', 'format', 'format_map',
 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

 '''
useful_method = ['capitalize','casefold','center','count','find','in','endswith','format']

'''

String Methods:

Case: lower(),upper(),capitalize(),title(),swapcase()

massage:

slice: vstr[str:end:step]
reverse the string using vstr[::-1]
split(char,utmost_split)rsplit()
strip(char_seq),lstrip(),rstrip()
separator.join(seq) # ','.join(['a','b','c'])
len()
find(char,m,n)
replace(old,new)D
index(char,m,n)
partition(substr)

checks:
startswith(),endswith(),isupper(),islower()...
in,not in

format:
center(),rjust(),ljust()
.format()





'''

vstr = 'CRYPTONIC is not a tonic'
vstr1 =  vstr.lower()
value = "50342=Data,231"

#print( vstr.capitalize() )

#print(vstr.casefold() )

#print(vstr.center(90,'*') )

print (vstr.find('not'))
print ( vstr.index('not') )

print ( vstr[13] )

print(vstr1)
print (vstr1.lstrip('onic'))

print(value)
result = value.strip("0123456789=,")
print(result)

result = value.lstrip("0123456789=,")
print(result)

result = vstr1.partition('not')
print(result)

## lstrip strips as much as substring it encounters and stops with the first string that do not match with the sequence


# format function

#print ( '{0} is {1}'.format('S',1) )

#print ( '{a} is {b}'.format(a='Sabari',b='Star'))
