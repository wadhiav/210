prime_numbers = 0 # declare variable 
#creating a function to check for the prime numbers 
def is_prime_number(x):
    if x >= 2: # has to be 2 or bigger thats where prime starts
        for y in range(2,x): 
            if not ( x % y ): # making the numbers divisible by each other
                return False
    else:
        return False # stop the nonprimes coming through
    return True 
	        
# to create a loop for the how many prime numbers the user wishes to check
for i in range(int(input("How many numbers you wish to check: "))): # simple input statement
    if is_prime_number(i): # taking the number inputed and running it through the statement 
        prime_numbers += 1 # adding 1 to the string 
        print (i) 

print (str(prime_numbers)) # the print str since we cant print strings and intergers 




