import os 
import time
import datetime

''' Dane wejsciowe '''
inCataloguePath=os.getcwd()
##print(inCataloguePath)
outCataloguePath='C:\Scripts\Os\out'
today=str(datetime.date.today())
##print(today)
outDataPath=os.path.join(outCataloguePath,today)
##print(outDataPath)

''' Warunki uruchomienia programu '''
'''     Czy istnieje katalog wejsciowy   '''
is_input_catalog_ok=os.path.isdir(inCataloguePath)
##print('InCatalogue exists?: ',is_input_catalog_ok)      
'''     Czy istnieje katalog wyjsciowy   '''
is_output_catalog_ok=os.path.isdir(outCataloguePath)
##print('OutCatalogue exists?: ',is_output_catalog_ok)
'''     Czy istnieje katalog lub plik z dzisiejsza data '''
is_today_output_catalog_ok=not os.path.exists(outDataPath)
##print('OutFolder or OutFile not exists?: ',is_today_output_catalog_ok)

''' Testy uruchomienia programu '''
if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('Prerequisits not met! Check the paths!')
    if not is_input_catalog_ok:
        print('InCatalogue not exists!!!')
    if not is_output_catalog_ok:
        print('OutCatalogue not exists!!!')
    if not is_today_output_catalog_ok:
        print('TodayCatalogue or TodayFile already exists!!!')
