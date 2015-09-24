


def count_letter(word,letter):
    count = 0
    for i in word:
        print(i)
        if i == letter:
            count = count + 1
    print()
    print('Count of %s in %s is %d' %(letter,word,count))
    print (word.count('a') ) 


vstr = input('Enter word\n')
vltr = input('Enter letter\n')
count_letter(vstr,vltr)
