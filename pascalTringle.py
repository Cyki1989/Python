rows=10
cValues=[]
width=50
for i in range(0,rows):
    lValues=cValues.copy()
    cValues=[]
    sValues=''
    end=i
    for j in range(0,end+1):
        if j==0 or j==end:
          cValues.append(1)
          sValues+='%4s ' %(1)
        else:
          tNumber=lValues[j-1]+lValues[j]  
          cValues.append(tNumber)          
          sValues+='%4s ' %(tNumber)
    else:
        print(sValues.center(width))
          
            
