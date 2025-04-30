
###############################################################################

'''
i=7
while i<100:
    print(i)
    i+=7
'''
    
'''
Colors=['Pink','Red','Green','Black', 'Yellow']

for i in Colors:
    print(i)
'''

'''    
n=0
while not(1<=n<=100):
    n=int(input("Please enter a valid number in range of 100: "))
    print("Thank you, This is a valid number!")



x=0
for i in range (5):
    x = int(input("Please enter a number between 1-100: "))
    if 1<=x<=100:
        print("Valid number", x)
        break
    else:
        print("Enter valid number")
        
'''        

###############################################################################
'''
If else 

age = int(input("Please enter your age: "))

if age>18:
    print("You are eligible to apply for license")
else:
    print("Please apply for license after 18 years of age!")

'''    
###############################################################################

#if (alone) statement
'''
if age>18:
    print("You are eligible to apply for license")
print("Warning!! Speed thrills but Kilss!")   
'''
###############################################################################

#if elif and else statement
'''
handsome = input("Please enter True or false for Handsome: ")
good_salary = input("Please enter True or false for good salary: ")

if handsome == 'true' and good_salary == 'true':
    print("You will marry a super model.")
    
elif handsome != 'true' and good_salary == 'true':
    print("You will marry a good girl.")

elif handsome=='true' and good_salary!='true':
    print("You will somehow marry a girl.")

else:
    print("Ram jaane Tumhara kya hi hoga.")

'''
###############################################################################

#Nested if-Can be used for minimum two conditions when one condition is true, 
#enter second condition.
'''
experience=int(input('Please enter your working experience: '))

if (experience >= 10):
    location=(input('Please enter your residence location: '))
    if location=='bangalore':
        print('You can apply for this job. Thank you')
        
    else:
        print('Sorry! This job is for Bangalore residents only.')
else:
    print('You need atleast 10 years of experience in order to apply for this role.')
    
'''
###############################################################################



























