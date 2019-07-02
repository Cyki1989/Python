import os 
import time

print(os.getcwd())
##dir=input('Please give me a catalogue namepath')
dir='C:\Scripts\Os'
print(dir)
if not os.path.isdir(dir):
  print('Wrong catalogue namepath')
else:
##    file=input('Please give me a file name')
    file='test.txt'
    path=os.path.join(dir,file)
    print(path)
##    if not os.path.isfile(path):
    if not os.path.exists(path):        
        print("File dosen't exist")
    else:
        print("Properties of file:")
        cTime=time.localtime(os.path.getctime(path))
        print("Time of creation: %d-%d-%d %d:%d:%d " %cTime[0:6])
        mTime=time.localtime(os.path.getmtime(path))
        print("Last modification: %d-%d-%d %d:%d:%d " %mTime[0:6])
        aTime=time.localtime(os.path.getatime(path))
        print("Last opened: %d-%d-%d %d:%d:%d " %aTime[0:6])
        print("Size in bajts: ", os.path.getsize(path))
        print("Actual catalogue: ", os.path.dirname(path))
        print("Actual catalogue: ", os.path.split(path)[0])
        print("Relative path to file: ", os.path.basename(path))
        print("Relative path to file: ", os.path.split(path)[1])
        print("Abs path to file: ", os.path.abspath(path))
