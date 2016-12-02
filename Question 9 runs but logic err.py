L = [2,3,5,7,9,13]
low = 10
high = 14

def bi_search(L,low,high):
    sta =  0
    end = (len(L) - 1)

    while sta < end:
        mid = (sta + end) //2 # add and divide with whole whole numbers

        if L[mid]>low and L[mid]<high:
            print ("True")
        elif L[mid]<low:
            sta =mid +1
        elif L[mid]>high:
            end=mid-1
        print ("False")
        
print (bi_search(L,low,high))

#for some reason the output is false. cant figure out what is wrong with the code
