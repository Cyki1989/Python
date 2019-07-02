class FindPairOfElements:

    def __init__(self,numbers,target):
        self.pair_index=[]
        n=len(numbers)
        i=0
        while i<n:
            second_number=target-numbers[i]
            j=i+1
            while j<n:
                if numbers[j]==second_number:
                    self.pair_index.append((i,j))
                j+=1
            i+=1           

    def __str__(self):
        return str(self.pair_index)


numbers=[10,20,10,40,50,60,70]
target=50
print(FindPairOfElements(numbers,target))

