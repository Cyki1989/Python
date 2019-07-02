while True:
    try:  
        n=int(input('Give me a number of dictionary elements: '))
        break
    except:
        print('You have to give me a int number of elements')

print({i:i*i for i in range(1, n+1)})
