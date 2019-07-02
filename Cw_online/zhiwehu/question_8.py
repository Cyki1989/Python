user_input=input('Give me a coma-separated seq of words: ')

##print(','.join(sorted(user_input.split(','))))

items=[x for x in user_input.split(',')]
items.sort()
print (','.join(items))
