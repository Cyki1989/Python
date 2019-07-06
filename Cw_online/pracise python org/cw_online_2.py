### cw 2 ### 1 sposob obslugi bledow z rasie exception ###
'''
import sys
num=''
check=''
while not(num and check):
    try:
        line=input('Give me a two number: ')
        num=float(line.split(' ')[0])
        check=float(line.split(' ')[1])
        if check==0:
            raise Exception('Second number has to !=0')
    except ValueError:
        print('You have enter a two numeric numbers:',sys.exc_info()[0])
    except Exception as e:
        print(e,sys.exc_info()[0])
    except:
        print ('Occuring an unknownd error:',sys.exc_info()[0])
    else:
        if num%check:
            print('%d is not divided by %d'%(num,check))
        else:
            print('%d is divided by %d'%(num,check))
'''   

### cw 2 drugi sposob ###
'''
import sys
num=''
check=''
while not(num and check):
    try:
        line=input('Give me a two number: ')
        num=float(line.split(' ')[0])
        check=float(line.split(' ')[1])
        result=num%check
    except ValueError:
        print('You have enter a two numeric numbers',sys.exc_info()[0])
    except ZeroDivisionError:
        print('Second number has to !=0',sys.exc_info()[0])
    except:
        print ('Occuring an unknownd error:',sys.exc_info()[0])
    else:
        if result:
            print('%d is not divided by %d'%(num,check))
        else:
            print('%d is divided by %d'%(num,check))       
'''           
