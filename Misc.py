'''
def creator():
    list=[]
    i=1
    while i<=200:
        list.append(i)
        i+=1
    return list

print(creator())

numbers=list(range(1,201))
print(numbers)'''

#thislist = ["apple", "banana", "cherry"]
#for i in thislist:
#  print(i)

#thislist = ["apple", "banana", "cherry"]
#for i in range(len(thislist)):
#  print(thislist[i])


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1