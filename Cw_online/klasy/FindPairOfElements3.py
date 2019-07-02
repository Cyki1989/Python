class FindPairOfElements:

    def __init__(self,numbers,target):
        self.pair_index=[]
        for i, num in enumerate(numbers):
            for j, num2 in enumerate(numbers[i+1:]):
                if num+num2==target:
                   self.pair_index.append((i,i+j+1))            
            

    def __str__(self):
        return str(self.pair_index)


numbers=[10,20,10,40,50,60,70]
target=50
print(FindPairOfElements(numbers,target))

