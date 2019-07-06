### cw 3 ###
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

### extra a ###

new_a=list(filter(lambda x: x<5, a))
print(new_a)
##new_a=list(filter(lambda x: True if x<5 else False, a))
##print(new_a)
new_a=[i for i in a if i<5]
print(new_a)

### extra b ###
print(list(filter(lambda x: x<5, a)))
print([i for i in a if i<5])

### extra c ###
max=15
print(list(filter(lambda x: x<max, a)))
print([i for i in a if i<max])
