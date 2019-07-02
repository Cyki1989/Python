##X = 3
##Y = 5
##
##tab=[]
##
##for x in range(X):
##    row=[]    
##    for y in range(Y):
##        row.append(x*y)
##    tab.append(row)
##
##print(tab)

X = 3
Y = 5

tab=[[x*y for y in range(Y)] for x in range(X)]
print(tab)
