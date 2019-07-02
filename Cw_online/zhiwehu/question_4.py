##values='34,67,55,33,12,98'

while True:
    try:
        values=input('Give me a seq of coma-separated numbers: ')
        list_of_values=values.split(',')
        if len(list_of_values) <= 1:
            raise Exception  
        tuple_of_values=tuple(list_of_values)
        break
    except Exception:
        print('You have to give me a seq of coma-separated numbers: ')
      

print(list_of_values)
print(tuple_of_values)
