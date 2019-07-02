
def sum_of_three(inputset):
    inputset.sort()
    inputset_lenght = len(inputset)
    result = []
    i=0
    while i < inputset_lenght-2:
        j, k = i+1, inputset_lenght-1
        while j < k:
            if inputset[i] + inputset[j] + inputset[k] < 0:
                j+=1
            elif inputset[i] + inputset[j] + inputset[k] > 0:
                k-=1
            else:
                result.append((inputset[i], inputset[j], inputset[k]))
                j+=1; k-=1
                while j < k and inputset[j] == inputset[j-1]:
                    j+=1
                while j < k and inputset[k] == inputset[k+1]:
                    k-=1
        i+=1
        while i < inputset_lenght-2 and inputset[i] == inputset[i-1]:
            i+=1
    return result


inputset = [-25, -10, -7, -3, 2, 4, 8, 10]

print(sum_of_three(inputset))
