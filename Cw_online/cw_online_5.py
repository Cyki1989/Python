import random

'''
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''
'''
a=[random.randint(0,100) for i in range(random.randint(0,100))]
b=[random.randint(0,100) for i in range(random.randint(0,100))]
print('a = ',a)
print('b = ',b)
'''

'''
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)
'''

'''
c=[a[i] for i in range(0,len(a)) if a[i] in b and a[i] not in a[:i]]
print('c = ',c)
'''
