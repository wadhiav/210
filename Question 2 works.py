def trailing(x):
    zero_tr = 0
    multiples = 5

    while multiples < x:
        zero_tr = zero_tr + (x / multiples)

        multiples = multiples * 5

    return (zero_tr)
print (trailing(234500000000))
