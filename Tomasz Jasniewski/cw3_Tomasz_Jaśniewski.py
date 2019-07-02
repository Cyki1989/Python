''' ##Easy way 2 time file open##
import random
import string

with open('dane.csv' , 'w') as file:
    for i in range(10):
        line = ''
        for j in range(10):
            choices_arr = [random.randint(0,1000),
                           ''.join(random.choices(string.ascii_uppercase,k=2))]
            line += str(random.choice(choices_arr))
            line += ';'
        file.write(line+'\n')
    file.close()

result =[ [] for i in range(10) ]

with open('dane.csv' , 'r') as file:
    for line in file:
        line = line.split(';')
        for i in range(len(line)-1):
            result[i].append(line[i])            
    file.close()

for i in result:
    print(' '.join(i))
'''


''' ##Easy way 1 time file open for write and read

import random
import string

with open('dane.csv' , 'w+') as file:
    for i in range(10):
        line_w = ''
        for j in range(10):
            choices_arr = [random.randint(0,1000),
                           ''.join(random.choices(string.ascii_uppercase,k=2))]
            line_w += str(random.choice(choices_arr))
            if j != 9: line_w += ';'
        file.write(line_w)
        if i != 9: file.write('\n')

    file.seek(0)
    result =[ [] for i in range(10) ]

    for line_r in file:
        line_r = line_r.strip().split(';')
        print(line_r)
        for i in range(len(line_r)):
            result[i].append(line_r[i])            

    file.close()

for i in result:
    print(' '.join(i))
'''


''' ##1 time file open for write and read with unknown list lenght
import random
import string

with open('dane.csv' , 'w+') as file:
    for i in range(10):
        line_w = ''
        for j in range(10):
            choices_arr = [random.randint(0,1000),
                           ''.join(random.choices(string.ascii_uppercase,k=2))]
            line_w += str(random.choice(choices_arr))
            line_w += ';'
        file.write(line_w + '\n')

    file.seek(0)
    line_size = file.readline().count(';')
    result =[ [] for i in range(line_size) ]
    file.seek(0)
    
    for line_r in file:
        line_r = line_r.split(';')
        for i in range(line_size):
            result[i].append(line_r[i])            

    file.close()

for i in result:
    print(' '.join(i))

'''

'''
## 1 Final solution 
import random
import string

with open('dane.csv' , 'w+') as file:
    for i in range(10):
        line_w = ''
        for j in range(10):
            choices_arr = [random.randint(0,1000),
                           ''.join(random.choices(string.ascii_uppercase,k=2))]
            line_w += str(random.choice(choices_arr))
            if j != 9: line_w += ';'
        file.write(line_w)
        if i != 9: file.write('\n')
    
    file.seek(0)
    print(file.read(), end='\n\n')
    file.seek(0)
    file_r = list(map(lambda l: l.strip().split(';'), file.readlines()))
    for i in range(10):
        for j in range(10):
            if j!= 9: print(file_r[j][i], end=';')
            else: print(file_r[j][i])
    file.close()
'''

'''
## 2 First approach
import string

maximum = -1
double_letters={}
with open('dane.csv', 'r') as file:

    file_r = list(map(lambda l: l.strip().split(';'), file.readlines()))
    for i in range(10):
        for j in range(10):
            if file_r[i][j].isnumeric():
                if int(file_r[i][j]) > maximum:
                   maximum = int(file_r[i][j])
                   maximum_index = (i,j)
            else:
                if file_r[i][j][0] == file_r[i][j][1]:
                    double_letters[(i,j)] = file_r[i][j]
    file.close()
    
print(f'max = {maximum} in position: {maximum_index}')
for k,v in double_letters.items():
    print(f'{v} in position {k}')           
'''    


## 2 Try except
import string
import sys
maximum = -1

with open('dane.csv', 'r') as file:

    file_r = list(map(lambda l: l.strip().split(';'), file.readlines()))
    for i in range(10):
        for j in range(10):
            try:
                if int(file_r[i][j]) > maximum:
                   maximum = int(file_r[i][j])
                   maximum_index = (i,j)
            except ValueError:
                if file_r[i][j][0] == file_r[i][j][1]:
                    print(f'{file_r[i][j]} in position: {i},{j}')
    file.close()
    
print(f'max = {maximum} in position: {maximum_index}')
          



