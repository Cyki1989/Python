##import os
##print(os.getcwd())
##
##file_path='C:\Scripts\Os\in\orders.txt'
####print(file_path)
####print(os.path.isfile(file_path))
##
##if os.path.isfile(file_path):
##    with open(file_path,"r") as file:
##        for line in file:
##            line=line.replace('\n','')
##            order=line.split(',')
##            if len(order)==3:
##                print('''Order from drugstore "%s", item "%s",amount %s'''
##                      % (order[0],order[1],order[2]))
##            else:
##                 print('Line %s malformed!!!' % line)
##        else:
##            print("Processing finished")

import os
print(os.getcwd())

file_path='C:\Scripts\Os\in\orders.txt'
##print(file_path)
##print(os.path.isfile(file_path))

if os.path.isfile(file_path):
    with open(file_path,"r") as file:
        for line in file:
            line=line.replace('\n','').split(',')
            order=[]
            for i in line:
                order.append(i.strip())
            if len(order)==3:
                print('''Order from drugstore "%s", item "%s",amount %s'''
                      % (order[0],order[1],order[2]))
            else:
                 print('Line %s malformed!!!' % line)
        else:
            print("Processing finished")
