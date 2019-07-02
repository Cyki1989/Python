'''
start = 2000
end = 3200

while start <= end:
    if start%7 == 0:
        break
    start+=1

result = []

while start <= end:
    if start%5 != 0:
        result.append(start)    
    start+=7

print(result)
'''


start, end = 2000, 3200

while start <= end and start%7: start+=1   

result = []

while start <= end:
    if start%5 != 0: result.append(str(start))    
    start+=7

print(','.join(result))

