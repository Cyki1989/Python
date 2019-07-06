def FillBoxWithCargo(BoxCapasity,cargo):
    
    sizeCargoList=len(cargo)-1
    cargo.sort(reverse=True)
    ##print(cargo)    
    
    minRemainBoxCapaisty=BoxCapasity
    minSelectedBoxItems=[]
    selectedBoxItems=[]
    remainBoxCapaisty=BoxCapasity
    first=0; last=0
    while cargo[first]>BoxCapasity: first+=1    
    last=first
    while first<=sizeCargoList:
        for i in range (last,sizeCargoList+1):
            if cargo[i]<=remainBoxCapaisty:
                selectedBoxItems.append(cargo[i])
                remainBoxCapaisty-=cargo[i]
                last=i
                if remainBoxCapaisty==0:
                    minSelectedBoxItems=selectedBoxItems
                    return minSelectedBoxItems
                elif remainBoxCapaisty<cargo[sizeCargoList]:
                    break
        if remainBoxCapaisty<minRemainBoxCapaisty:
            minRemainBoxCapaisty=remainBoxCapaisty
            minSelectedBoxItems=selectedBoxItems.copy()
        if last==sizeCargoList:
            first+=1
            last=first
            selectedBoxItems=[]
            remainBoxCapaisty=BoxCapasity
        else:
            selectedBoxItems.pop()
            remainBoxCapaisty+=cargo[last]
            if first==last: 
                first=last+1
            last+=1
        if sum(cargo[first:])<sum(minSelectedBoxItems):
            return minSelectedBoxItems
    else:
         return minSelectedBoxItems  


BoxCapasity=90
cargo=[89,80,2,2,2,2,2,2,2,2,2]       

print(FillBoxWithCargo(BoxCapasity,cargo))
print(sum(FillBoxWithCargo(BoxCapasity,cargo)))
