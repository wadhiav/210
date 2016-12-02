word = input("please enter the word you would like to convert: ")
vowels = "aieou"
no_vow_word ="" # this empty sting for the no vowel word 
count = 0
number = 0

for x in word: # take each letter from input
    print (x)
    count = 0 
    number = 0
    
    for y in vowels:
        number += 1 #this is to add a count to the letters it finds with vowels

        if x == y:
            count -= 1 # this takes the aieou away 
        elif x != y and count != -1 and number == 5: # simply checking the function again for vowels 
            no_vow_word = no_vow_word + (x) 

print(no_vow_word)
