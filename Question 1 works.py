import random

ordered_lst = [1,3,4,5,6,7,8,9]

def shuffle_array(ordered_lst):
    shuffle_lst = []
    print (ordered_lst)

    for i in range(len(ordered_lst)):
        x = random.randint(0,len(ordered_lst))
        x = x-1
        shuffle_lst.append(ordered_lst[x])
        ordered_lst.remove(ordered_lst[x])
    return (shuffle_lst)



print(shuffle_array(ordered_lst))

