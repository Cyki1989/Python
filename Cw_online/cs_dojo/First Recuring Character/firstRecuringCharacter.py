from random import randint

def firstRecuringCharacter(data):
    for i in range(len(data)):
        if data[i] in data[:i]:
            return data[i]
    return None


data =''.join([chr(randint(97,122)) for i in range(randint(1,20))])
print(data)
print(firstRecuringCharacter(data))

