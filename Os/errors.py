import os
import sys

line=input('How old are you? ')
filepath='C:\Scripts\Os\in\errors.txt'
print(filepath)
filepath=input('Give me a filepath: ')

try: 
    file=open(filepath,'w')
    age=int(line)
    file.write(str(age)+'\n')
    file.close()
except ValueError as e:
    print('The value "%s" entered cannot be converted to a number' %line)
    print('Error type:',e)
except FileNotFoundError as e:
    print('Error opening file "%s" ' %line)
    print('Error type:',e)
except:
    print('SORRY - WE HAVE AN ERROR',sys.exc_info()[0])
else:
    print('Actions completed successfully')
