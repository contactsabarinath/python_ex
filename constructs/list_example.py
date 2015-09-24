

##################### populate the items in the list ##################################

############### +, lst.append(), lst.extend(), lst.insert() ###########################

lst = ['sql','pl/sql']
print (lst)

lst = lst + ['oracle'] # note list is concatenated with another list not just a string
print (lst)

lst.append('python') # append takes one arguement and appends to the list - that one element can be in turn could be list
print (lst)

lst.extend(['Hadoop','Hive','Pig']) # extend takes in one arguement. this is always a list and add each member individually
print (lst)


lst.insert(0,'MapReduce')
print (lst)

##################### search the list ##################################

################### in , lst.count(), lst.index()


print ('Hadoop' in lst)

print (lst.count('sql') )
 
print (lst.index('MapReduce') )

print (lst[4] )



##################### remove the items from list ##################################

##################### del lst[0] , lst.remove('item'), lst.pop(), lst.pop(n) ##########################

print('Entering Delete Section')
print (lst)

del lst[0]
print (lst)

lst.append('jython')
print (lst)

lst.remove('jython')
print (lst)

lst.pop()
print (lst)

lst.pop(2)
print (lst)
