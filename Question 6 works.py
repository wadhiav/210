def reverse_sentence():
    s = input("Enter a sentence you wish to reverse: ")
    s_split = s.split() # splits the sentence the user will input
    new_s=[] # this is a list the sentences would be inserted into
    x= -1
    y= len(s_split)*-1 # this is to make the numbers of letters to negative
    while x >= y:
        z=s_split[x]
        #next to append x
        new_s.append(z) 
        x = x -1 # bring string to zero since python works from 1 
    s_split = '' # this is to print the string
    print(s_split.join(new_s)) # jin the different words in the split
reverse_sentence()
