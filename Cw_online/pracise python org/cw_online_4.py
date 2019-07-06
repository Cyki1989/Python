### cw 4 ###
'''
while True:
    try:
        n=int(input('Give me a positive integer number: '))
        if n<=0:
            raise Exception
        break
    except ValueError:
        print('Wrong value type! Read the statement!')
    except Exception:
        print('Number <=0! Read the statement!')


divisorsRange=n//2+1
divisors=[i for i in range(0,divisorsRange)]

print(divisors)

for i in range(2,divisorsRange):
    if divisors[i]>0:
        if n%i!=0:
            divisors[i]=0
            w=i+i
            while w<divisorsRange:
                divisors[w]=0
                w+=i
    else:
        continue
else:
    divisors.append(n)
    divisors=list(filter(lambda x: x, divisors))
    print(divisors) 
'''

'''
### Drugi sposób mniej wydajny moim zdaniem ###

while True:
    try:
        n=int(input('Give me a positive integer number: '))
        if n<=0:
            raise Exception
        break
    except ValueError:
        print('Wrong value type! Read the statement!')
    except Exception:
        print('Number <=0! Read the statement!')


divisorsRange=n//2+1
divisors=[i for i in range(0,divisorsRange)]
divisors.append(n)
print(divisors)

for i in divisors:
    if i>1:
        if n%i!=0:
            divisors[i]=0
            w=i+i
            while w<divisorsRange:
                divisors[w]=0
                w+=i
    else:
        continue
else:
    divisors=list(filter(lambda x: x, divisors))
    print(divisors)
''' 
   
