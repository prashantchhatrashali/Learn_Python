#File Handling:
    
    #Following oprations are performed: 
        #1. Open File
        #2. Read Write File
        #3. Close the file. 
         
#import pandas as pd

#f=open('new.txt')
#f.read()

f=open('new.txt','a')
f.write("I will learn Python in this week only.")
f.close()


f=open('new.txt')
#f.read()
f.seek(0)
#f.read()

for line in f:
    print(line)
