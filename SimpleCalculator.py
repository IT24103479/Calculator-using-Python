#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
    
def power(a,b):
    return a**b
    
def rem(a,b):
    return a%b
#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
    
    if choice =='#':
         return -1
    if choice == '$':
         return  True
       
    if choice not in ['+','-','*','/','^','%']:
       print("Unrecognized operation")
       return True
       
    
    
    first = input("Enter first number: ")
    if first in ['$','#']:
        if first == '#':
            return -1
        return True
        
    try:
        a = float(first)
    except:
        print("Not a valid number,please enter again")
        return True

  
    second = input("Enter second number: ")
    if second in ['$','#']:
        if second == '#':
            return -1
        return True
    try:
        b = float(second)
    except:
        print("Not a valid number,please enter again")
        return True

           
           
        
        
    try:
        if choice == '+':
            print(add(a, b))
        elif choice == '-':
            print(sub(a, b))
        elif choice == '*':
            print(mul(a, b))
        elif choice == '/':
            print(div(a, b))
        elif choice == '^':
            print(power(a, b))
        elif choice == '%':
            print(rem(a, b))
    except:
        print("Something Went Wrong")
       
      
    return True
       
      


#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()