





def print_row():
    row = 0
    while row < 1:

        rowpos = 1    
        print('+',end = " ")
        rowpos = rowpos + 1
        
        while rowpos <= 11:
            #print (rowpos, end = " ")
            if (rowpos -  ( (rowpos // 5) * 5) ) == 1 :
                print ('+',end = " ")
            else:
                print ('-',end = " ")
            rowpos = rowpos + 1
        print()
        row = row + 1
    
def print_col(n):
    col = 0
    while col < n:
        colpos = 1
        print ('|',end = " ")
        colpos = colpos + 1
        
        while colpos <= 11:
            if (colpos - ( (colpos//5) * 5 ) ) == 1:
                print ('|',end = " ")
            else:
                print(" ",end = " ")
            colpos = colpos + 1
        print()
        col = col + 1


print('enter number of rows')
r = int(input())
print('enter number of columns')
c = int(input())
for i in range(r - 1):
   print_row()
   for j in range(c):
       print_col(c)
print_row()

