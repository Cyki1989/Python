class SumOfThreeElementsEqualZero:

    def __init__(self,numbers):
        self.three_elements=[]
        for i, num_1 in enumerate(numbers):
            for j, num_2 in enumerate(numbers[i+1:]):
                for k, num_3 in enumerate(numbers[j+1:]):
                    if num_1+num_2+num_3==0:
                        self.three_elements.append([num_1,num_2,num_3])               

    def __str__(self):
        return str(self.three_elements)


numbers=[-25, -10, -7, -3, 2, 4, 8, 10]
print(SumOfThreeElementsEqualZero(numbers))

