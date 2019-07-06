import time
t1=time.time()
## Fib iterative ## place 1 ##
##################################################################
def fib(n):
    if n<=1:
        print([1])
    else:
        fib_catches=[1,1]
        for i in range(3,n+1):
            fib_catches.append(fib_catches[len(fib_catches)-1]+
                               fib_catches[len(fib_catches)-2])
        else:
            print(fib_catches)

fib(10)
##################################################################
t2=time.time()
## Fib recursive ## place 4 ##
##################################################################
def f(n):
    if n<=2: 
        return 1
    else:
        return f(n-1)+f(n-2)

def fib(n):
    fib_catches=[]    
    for i in range(1,n+1):
        fib_catches.append(f(i))
    else:
        print(fib_catches)

fib(10)
##################################################################
t3=time.time()
## Fib recursive with memorization ## place 3 ##
##################################################################
fib_catches={}
def f(n):
    if n in fib_catches:
        return fib_catches[n]
    else:
        if n<=2:
            fib_catches[n]=1
            return fib_catches[n]
        else:
            fib_catches[n]=f(n-1)+f(n-2)
            return fib_catches[n]

def fib(n):  
    for i in range(1,n+1):
        f(i)
    else:
        print(list(fib_catches.values()))

fib(10)
##################################################################
t4=time.time()
## Fib with yieald ## place 2 ##
##################################################################
def f(n):
    a1=1
    a2=1
    yield a1
    yield a2
    i=3
    while i<n+1:
        sum=a1+a2
        yield sum
        a1=a2
        a2=sum
        i+=1

def fib(n):
    print(list(f(n)))
'''    for i in f(n): print(i)'''
        
fib(10)
##################################################################        
t5=time.time()

print('Fibo iterative time:', t2-t1)
print('Fibo recurive time:', t3-t2)
print('Fibo recurive with memorization time:', t4-t3)
print('Fibo with yield', t5-t4)
