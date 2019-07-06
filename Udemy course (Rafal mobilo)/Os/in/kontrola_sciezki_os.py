import os 
import time
import datetime

## Dane wejsciowe ##
inCataloguePath=os.getcwd()
##print(inCataloguePath)
outCataloguePath='C:\Scripts\Os\out'
today=str(datetime.date.today())
##print(today)
outFolderPath=os.path.join(outCataloguePath,today)
##print(outCataloguePath)
outFileName=today+'.csv'
outFilePath=os.path.join(outCataloguePath,outFileName)
##print(outFilePath)

## Warunki uruchomienia programu ##

print('InCatalogue exists?: ',os.path.exists(inCataloguePath))
print('InCatalogue exists?: ',os.path.isdir(inCataloguePath))      

print('OutCatalogue exists?: ',os.path.exists(outCataloguePath))
print('OutCatalogue exists?: ',os.path.isdir(outCataloguePath))

print('OutFolder exists?: ',os.path.exists(outFolderPath))
print('OutFolder exists?: ',os.path.isdir(outFolderPath))  

print('OutFile exists?: ',os.path.exists(outFilePath))
print('OutFile exists?: ',os.path.isdir(outFilePath))

## Warunki uruchomienia programu ##
