class FindPairOfElements:

    def __init__(self,numbers,target):
        lookup={}
        self.pair_index=[]
        for i, number in enumerate(numbers):
            if target-number in lookup:
                self.pair_index.append((i,lookup[target-number])) 
            lookup[number]=i
                

    def __str__(self):
        return str(self.pair_index)


numbers=[10,20,10,40,50,60,70]
target=50
print(FindPairOfElements(numbers,target))

