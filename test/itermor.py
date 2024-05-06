

def is_child(l1,l2):
    index = 0
    for i,num in enumerate(l2):
        for n,x in enumerate(l1):
            if x == num:
                index += 1
                continue
    if index == len(l2):
        print(index, len(l2))
        return True
    else:
        print(index,len(l2))
        return False
print(is_child([1, 2, 3, 4, 5],[1,6,2,5]))