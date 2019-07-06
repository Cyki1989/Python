## Recursive solution with rev_sort outside function
'''
def is_hoppable(data):
    if data == []:
            return True
    for x in enumerate(data,1):
        if x[0] <= x[1]:
            if is_hoppable(data[x[0]:]):
                return True
    return False
            

data = [4,2,0,0,2,0]
data = data[::-1]
print(is_hoppable(data))
'''

## Recursive solution with 2 fuctions
'''
def is_hoppable(data):
    data = data[::-1]
    if helper(data):
        return True
    return False     


def helper(data):
    if data == []:
            return True
    for x in enumerate(data,1):
        if x[0] <= x[1]:
            if helper(data[x[0]:]):
                return True
    return False            

data = [2,2,0,0,2,0]
print(is_hoppable(data))
'''
