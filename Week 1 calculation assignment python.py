def calculator():
    numb=int(input("Enter first number: "))
    numb2=int(input("Enter second number: "))
    operation=input("Enter operation (+, *, /, - ): ")
# perform calculation by operation:
    if  operation=="+":                     
        result= numb+ numb2
    elif operation=="*":
        result= numb * numb2
    elif operation == "-":
        result = numb-numb2
    elif operation=="/":
        if numb2 !=0:
            result=numb/numb2
        else:
            print("Error: Division by zero is undefined.")
            return
    else:
        print("Invalid operation. please enter one of /, *, - , +")
        return
    print(f"{numb}{operation}{numb2}={result}")
# To run the calculator function
calculator()

