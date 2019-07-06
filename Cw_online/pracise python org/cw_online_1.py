## 1 ##
import datetime

current_year=datetime.datetime.today().year
name=input('Give me a name: ')
age=input('Give me a age: ')
replicate=input('Give me a number of replicate: ')
if int(replicate)>0:
    print(f'{name} you are 100 years old in {current_year+100-int(age)} year',
          f'\n{name} you are 100 years old in {current_year+100-int(age)} year'
          *(int(replicate)-1))

##message='{0:s} you are 100 years old in {1:d} year'
##print(message.format(name,current_year+100-int(age)))

