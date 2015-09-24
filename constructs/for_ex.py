
vstr = input('Enter string \n')
vstr2 = ''

'''for x in range(10,0,-1):
    print (x)

'''


for x in range(0,len(vstr)):
    print (x,end=" ")
    print(vstr[x])

for x in range(len(vstr)-1,-1,-1):
    print (x, end = "  ")
    print(vstr[x])
    vstr2 = vstr2 + vstr[x]

print ('Palindrome of %s  is %s' %(vstr,vstr2)  )


    

