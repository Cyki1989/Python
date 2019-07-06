import sys
file_path = 'C:\Scripts\Os\in\orders.txt'
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2]) 
        except ValueError as e:
            print('\n','Value error in order: "%s"' % line, sep='')
            print('Amount should be a integer >0', e, '\n')            
        except IndexError as e:
            print('\n','Index error in order: "%s"' % line, sep='')
            print('Order should have 3 expression, splited with coma', e, '\n')
        except:
            print('\n Unknown error in order: "%s"' % line,
                  'Error type: "%s"' % str(sys.exc_info()[0]),sep='\n',end='\n')
            
        print ('Order from drugstore "%s", item "%s", amount %d'
               % (pharmacy_name, item, amount))
 
print("Processing finished")
