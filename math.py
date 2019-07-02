percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']

print('min=',min(percent),'max=',max(percent))
sumOfPoints = 4988
sum=0
for i in range(0,len(countries)):
    print(countries[i], round(percent[i],2),int(percent[i]),\
          round(percent[i]/100*sumOfPoints))
    sum+=round(percent[i]/100*sumOfPoints)
else:
    print(sum)
    
    
               
               
 
