seq = [1,2,4,68,9,5,3,6,7]

def sub_sequence(seq, x):
    x = 0
    count = 0
    output = []
    if x > (len(seq) -1):
        print(output,key=(len))
        return
    output.append()

    while True:
        i = lst(x)
        if i != seq[len(seq)-1] and i < seq[seq.index(i)+1]:
            output[count].append(i)
            x +=1
        else:
            ouput[count].append(i)
            x +=1
            count += 1
            return sub_sequence(seq,x)
