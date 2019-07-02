def binary_search(list,x):
    '''return true if x in list or false in other way'''
    list.sort()
    print(list)
    left=0; right=len(list)-1
    while left<=right:
        center=int((left+right)/2)
        if list[center]==x:
            return True
        elif list[center]<x:
            left=center+1
        else:
            right=center-1
    else:
        return False


from random import randint

list=[randint(0,100) for x in range(0,randint(20,100))]
print(binary_search(list,5))

