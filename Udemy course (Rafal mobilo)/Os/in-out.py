#### 1 ##
##import os
##webAdresses=[]
##line=input('Give me a www adress: ')
##if line:
##    webAdresses.append(line)
##    
##while line:
##    line=input('Give me another www adress: ')
##    if line:
##        webAdresses.append(line)
####else:
####    print(webAdresses)
##
##dirname=os.getcwd()
####print(dirname)
##    
####filename=input('Give me a filename: ')    
##filename='webadresses.txt'
##filepath=os.path.join(dirname,filename)
####print(filepath)
##file=open(filepath, 'w')
##for adress in webAdresses:
##    file.writelines(adress+'\n')
##
##file.close()

## 2 ##

import os
 
filename='webadresses.txt'
dirname=os.getcwd()
filepath=os.path.join(dirname,filename)
print(filepath)

filepath='' 
while not os.path.isfile(filepath):
    filepath=input('Give me a correct filePath: ')

webadresses=[]

file=open(filepath, 'r')
line=file.readline()
while line:
    webadresses.append(line.strip())
    line=file.readline()
file.close()

##print(webadresses)

for adress in webadresses:
    if adress.endswith('.pl'):
        print('adress "%s" is a polish adress' %adress)
        filepath=os.path.join(dirname, 'webs_pl.txt')
    else:
        print('adress "%s" is not a polish adress' %adress)
        filepath=os.path.join(dirname, 'webs_other.txt')
    with open(filepath, 'a+') as file:
        file.write(adress+'\n')   
