class Sentence:
    
    def __init__(self, sentence):
        self.sentence=sentence.split()
        self.current=0
        self.end=len(self.sentence)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        current=self.current
        if self.current>=self.end:
            raise StopIteration
        self.current+=1
        return self.sentence[current]

    
def WordFromSentenceGenerator(sentence):
    sentence=sentence.split()
    current=0
    while current<len(sentence):
        yield sentence[current]
        current+=1


def WordFromSentenceGenerator2(sentence):
    sentence=sentence.split()
    for word in sentence:
        yield word

    
        
s1=Sentence("Ala ma kota")   

s2=WordFromSentenceGenerator2("Ala ma kota")
print(s2)
for i in s2:
    print(i)


      
