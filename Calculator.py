#####################################
#    Building a simple Calculator   #
#####################################

while True:
    x=input('Please select your operation (i.e. add, subtraction, multiply, divide): ')
    a=int(input('Please enter first digit: '))
    b=int(input('Please enter second digit: '))
    
    a1=type(a)
    a2=type(b)
    
    if x=='add':
        y=a+b
        print('Here is your Addition: ',y)
    elif x=='multiply':
        y=a*b
        print('Here is your Multiplication: ',y)
    elif x=='divide':
        if b==0:
            print('Sorry, division by zero is not possible.')    
        else:
            y=a/b
            print('Here is your division: ',y)
    elif x=='subtraction':
        y=a-b
        print('Here is your Subtraction: ',y)
    else:
        print('please rerun the program and choose correct option')

input("Press any key to exit.")