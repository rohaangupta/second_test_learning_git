#defining function for add,sub,mul,divide
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2==0:
        return "can't divide"
    return num1/num2
 

#defining calculator and using all function here 
def calculator():
    print("hey,welcome")


    while True:
                x=float(input("enter first number"))
                y=float(input("enter second number"))
                operation=input("enter the operation(+,-,*,/):")

                if operation=="+":
                    print(f"result: {x} + {y}={add(x,y)}")

                elif operation=="-":
                    print(f"result: {x} - {y}={sub(x,y)}")

                elif operation=="*":
                    print(f"result: {x} *{y}={multiply(x,y)}")

                elif operation=="/":
                    print(f"result: {x} / {y}={divide(x,y)}")

                else:
                    print("invalid operation")
                
                if input("do you want to perform another calculation(y/n)") != "y":
                    break

    print("Bye")

#calling calculator
calculator()

