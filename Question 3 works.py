def square(x):
    i = 1

    perfect = 1

    while perfect < x:
        i = i + 1
        perfect = i**2

    i = i -1

    return (i**2)
print (square(2345))
    

