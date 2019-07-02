### cw 1 ###
##import pickle
##
##def createWordsList():
##    wordsList=[]    
##    while True:
##        words=input('Give me a words, word "end" ending reading: ')  
##        for i in filter(lambda x: x,words.split(' ')):
##            if i=='end':
##                print (wordsList)
##                return wordsList
##            else:
##                wordsList.append(i)
##
##with open('words.pickle', 'wb') as fs:
##    pickle.dump(createWordsList(), fs)
##
##def loadList():
##    with open('words.pickle', 'rb') as fr:
##        return sorted(pickle.load(fr))   
##   
##print(loadList())
####################################################################

### cw 2 ###
##def det(pkt1,pkt2,pkt3):
##    d=pkt1[0]*pkt2[1]+pkt2[0]*pkt3[1]+pkt3[0]*pkt1[1]
##    d-=pkt3[0]*pkt2[1]+pkt1[0]*pkt3[1]+pkt2[0]*pkt1[1]   
##    if abs(d)<=0.000001:
##        return True
##    else:
##        return False
##
##pointList=[]
##while len(pointList)<3:
##    try:
##        line=input(f'Enter {len(pointList)+1} a point: ')
##        line=line.split(' ')
##        x=float(line[0])
##        y=float(line[1])
##    except ValueError as e:
##        print('Occur error:', e,)
##        print(f' You have to enter a point nr {len(pointList)+1} again!!!')
##    else:
##        pointList.append((x,y))
##
##print(det(*pointList))
####################################################################

####################################################################

### cw 3 ###
##from time import localtime,strftime
##
##myDict={}
##
##'''
##myDict ={'11:31:59': 'Python', '11:32:32': 'python res', '11:32:49': 'Ala Kuba Python Ola',\
##'11:33:01': 'ala', '11:32:58': 'kuba python ola', '11:32:02': 'python', '11: 32:12': 'fpython',\
##'11:32:21': 'python2', '11:32:59': 'ola'} 
##'''
##
##while True:
##    line=input('Give me a line of text, line "end" ending reading: ')
##    if line=='end':
##        break
##    else:
##        time=strftime('%H:%M:%S',localtime())
##        myDict[time]=line
##
##print(dict(filter(lambda x: 'python' in x[1].lower().split(' '), myDict.items())))
##
##'''
##keyValue=filter(lambda x: 'python' in x[1].lower().split(' '), myDict.items())
##newDict={}
##for k,v in keyValue:
##    newDict[k]=v
##print(newDict)
##'''
##
##'''
##print({k:v for k,v in myDict.items() if 'python' in v.lower().split(' ')})
##'''

####################################################################
