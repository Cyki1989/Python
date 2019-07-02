## 1. Wyświetl parzyste elementy zbioru <1;100> ##
## 1.a Easy way ##
'''
for i in range(1,101):
    if i%2==0:
        print(i)
'''
## 1.b Easy way using function ##
'''
def EvenFromSet(s,e):
    for i in range(s,e+1):
        if i%2==0:
            print(i)
        
EvenFromSet(1,100)   
'''
## 1.c Fastes way using function ##
'''
def EvenFromSet(s,e):
    if s%2==1: s=s+1
    for i in range(s,e+1,2):
        print(i)
        
EvenFromSet(1,1)   
'''
## 1.d Way using filter function ##
'''
def EvenFromSet(s,e):   
    print(list(filter(lambda x: x%2==0,
                      list(range(s,e+1)))))
        
EvenFromSet(1,100) 
'''


#### 2. Wyświetl n-elementow ciagu Fibonaciego ##
##import time
##t1=time.time()
#### Fib iterative ## place 1 ##
####################################################################
##def fib(n):
##    if n<=1:
##        print([1])
##    else:
##        fib_catches=[1,1]
##        for i in range(3,n+1):
##            fib_catches.append(fib_catches[len(fib_catches)-1]+
##                               fib_catches[len(fib_catches)-2])
##        else:
##            print(fib_catches)
##
##fib(10)
####################################################################
##t2=time.time()
#### Fib recursive ## place 4 ##
####################################################################
##def f(n):
##    if n<=2: 
##        return 1
##    else:
##        return f(n-1)+f(n-2)
##
##def fib(n):
##    fib_catches=[]    
##    for i in range(1,n+1):
##        fib_catches.append(f(i))
##    else:
##        print(fib_catches)
##
##fib(10)
####################################################################
##t3=time.time()
#### Fib recursive with memorization ## place 3 ##
####################################################################
##fib_catches={}
##def f(n):
##    if n in fib_catches:
##        return fib_catches[n]
##    else:
##        if n<=2:
##            fib_catches[n]=1
##            return fib_catches[n]
##        else:
##            fib_catches[n]=f(n-1)+f(n-2)
##            return fib_catches[n]
##
##def fib(n):  
##    for i in range(1,n+1):
##        f(i)
##    else:
##        print(list(fib_catches.values()))
##
##fib(10)
####################################################################
##t4=time.time()
#### Fib with yieald ## place 2 ##
####################################################################
##def f(n):
##    a1=1
##    a2=1
##    yield a1
##    yield a2
##    i=3
##    while i<n+1:
##        sum=a1+a2
##        yield sum
##        a1=a2
##        a2=sum
##        i+=1
##
##def fib(n):
##    print(list(f(n)))
##'''    for i in f(n): print(i)'''
##        
##fib(10)
####################################################################        
##t5=time.time()
##
##print('Fibo iterative time:', t2-t1)
##print('Fibo recurive time:', t3-t2)
##print('Fibo recurive with memorization time:', t4-t3)
##print('Fibo with yield', t5-t4)


## 3. Wyświetl kwadrat zlozony z losowej malej literki o boku z zakresu[5,10] ##
## 3a. Kwadrat wypelniony ##
'''
import random

letter=chr(random.randint(97,122))
number=random.randint(5,11)
line=letter*number
square=''

for i in range (number):
    square+=line
    if i !=number-1:
        square+='\n' 
else:
    print(square)
'''

## 3a. Kwadrat pusty w srodku ##
'''
import random

letter=chr(random.randint(97,122))
number=random.randint(5,11)
lineOut=letter*number
lineIn=letter+' '*(number-2)+letter
square=''
for i in range (number):
    if not i or i==number-1:
       square+=lineOut 
    else:
       square+=lineIn  
    if i !=number-1:
        square+='\n' 
else:
    print(square)
'''
## 4 Wyswietl slownik z calkowitymi wartosciami klucza ##
## 4a Easy way ##
'''
def reduceDictionary(Dict):
    newDict={}
    for key in Dict:
        if isinstance(key,int):
            newDict[key]=Dict[key]
    return newDict

Dict={1:2, 'two':3, 2:3, 3:4, 'one':2}
print(reduceDictionary(Dict))
'''
## 4b With filter function ##
'''
def reduceDictionary(Dict):
    newDict={}
    goodKey=filter(lambda x: isinstance(x,int) ,Dict)
    for i in goodKey:
            newDict[i]=Dict[i]   
    return newDict

Dict={1:2, 'two':3, 2:3, 3:4, 'one':2}
print(reduceDictionary(Dict))
'''
## 4c With filter function revers ##
'''
def reduceDictionary(Dict):
    newDict={}
    goodKey=filter(lambda x: not(isinstance(x,int) or isinstance(x,float)),Dict)
    for i in goodKey:
            newDict[i]=Dict[i]   
    return newDict

Dict={1:2, 'two':3, 2:3, 3:4, 'one':2, 1.2:2, 5.3:2}
print(reduceDictionary(Dict))
'''

## 4d With comprehension ##  
'''
Dic={1:2, 'two':3, 2:3, 3:4, 'one':2}
newDic={k:v for k,v in Dic.items() if isinstance(k,int)}
print(newDic)
'''

## 4e With comprehension reverse ##  
'''
Dic={1:2, 'two':3, 2:3, 3:4, 'one':2, 1.2:2, 5.3:2}
newDic={k:v for k,v in Dic.items()
        if not (isinstance(k,int) or isinstance(k,float))}
print(newDic)
'''

## 4f With comprehension reverse with function##  

##def reduceDictionary(Dict):
##    ''' function return dictionatry without int and float keys '''
##    newDict={k:v for k,v in Dict.items()
##             if not(isinstance(k,int) or isinstance(k,float))}
##    return newDict
##
##Dict={1:2, 'two':3, 2:3, 3:4, 'one':2, 1.2:2, 5.3:2}
##print(reduceDictionary(Dict))


#### 5. Znajdz liczby pierwsze w liscie i zwroc zbior ##
#### 5a lista jako input  ##
##from math import sqrt
##
##def isPrime(x):
##    ''' check if given argument is prime '''
##    if not isinstance(x,int) or x<=1:
##        return False
##    if x in (2,3):
##        return True
##    if not x%2 or not x%3:
##        return False   
##    k=1; sign=-1; n=6*k+sign; end=int(sqrt(x))
##    while n<=end:
##        if not x%n:
##            return False
##        sign*=-1
##        if sign<0:
##            k+=1
##        n=6*k+sign
##    return True
##
##setOfPrime=set()
##    
##def reduceList(List):
##    ''' check if given list contain prime numbers '''
##    for x in List:
##        if isinstance(x,list) or isinstance(x,tuple) or isinstance(x,set):
##            reduceList(x)
##        elif isinstance(x,dict):
##            reduceList(list(x.items())
##        elif isPrime(x):
##            setOfPrime.add(x)
##    return setOfPrime
##
##List = [1,5,7,9,14,'kaszanka',[5,'wiadro'],(123,11,0.9,5.5,[17,23]),{19:43,'a':3,'ślimak':17,2:2}, 13, 29]
##print(reduceList(List))

#### 5b dowolna kolekcja jako input ##
##from math import sqrt
##
##def isPrime(x):
##    ''' check if given argument is prime '''
##    if not isinstance(x,int) or x<=1:
##        return False
##    if x in (2,3):
##        return True
##    if not x%2 or not x%3:
##        return False   
##    k=1; sign=-1; n=6*k+sign; end=int(sqrt(x))
##    while n<=end:
##        if not x%n:
##            return False
##        sign*=-1
##        if sign<0:
##            k+=1
##        n=6*k+sign
##    return True
##
##setOfPrime=set()
##    
##def reduceCollection(collection):
##    ''' check if given colection contain prime numbers '''
##    if isinstance(collection,dict):
##        reduceCollection(list(collection.items()))
##    elif isinstance(collection,list) or \
##         isinstance(collection,tuple) or isinstance(collection,set):            
##        for x in collection:
##            if isinstance(x,list) or isinstance(x,tuple) or isinstance(x,set):
##                reduceCollection(x)
##            elif isinstance(x,dict):
##                reduceCollection(list(x.items()))
##            elif isPrime(x):
##                setOfPrime.add(x)
##    else:
##        if isPrime(collection):
##            setOfPrime.add(collection)
##    return setOfPrime
##
##setOfPrime.clear()
##List = [1,5,7,9,14,'kaszanka',[5,'wiadro'],(123,11,0.9,5.5,[17,23]),{19:43,'a':3,'ślimak':17,2:2}, 13, 29]
##print(reduceCollection(List))
##
##setOfPrime.clear()
##Dict = {1:5, 3:2, 7:9}
##print(reduceCollection(Dict))
##
##setOfPrime.clear()
##Set = {1,2,3,4,5,6,7,8,9}
##print(reduceCollection(Set))
##
##setOfPrime.clear()
##Tuple = (1,5,7,9,14,'kaszanka',[5,'wiadro'],(123,11,0.9,5.5,[17,23]),{19:43,'a':3,'ślimak':17,2:2}, 13, 29)
##print(reduceCollection(Tuple))
##
##setOfPrime.clear()
##print(reduceCollection(3))


#### 5c lista jako input bez zmiennej globalnej ##
##from math import sqrt
##
##def isPrime(x):
##    ''' check if given argument is prime '''
##    if not isinstance(x,int) or x<=1:
##        return False
##    if x in (2,3):
##        return True
##    if not x%2 or not x%3:
##        return False   
##    k=1; sign=-1; n=6*k+sign; end=int(sqrt(x))
##    while n<=end:
##        if not x%n:
##            return False
##        sign*=-1
##        if sign<0:
##            k+=1
##        n=6*k+sign
##    return True
##
##    
##def reduceList(List):
##    ''' check if given list contain prime numbers '''
##    listOfPrime=[]
##    for x in List:
##        if isinstance(x,list) or isinstance(x,tuple) or isinstance(x,set):
##            listOfPrime+=reduceList(x)
##        elif isinstance(x,dict):
##            listOfPrime+=reduceList(list(x.items()))
##        elif isPrime(x):
##            listOfPrime.append(x)
##    return set(listOfPrime)
##
##List = [1,5,7,9,14,'kaszanka',[5,'wiadro'],(123,11,0.9,5.5,[17,23]),{19:43,'a':3,'ślimak':17,2:2}, 13, 29]
##print(reduceList(List))


