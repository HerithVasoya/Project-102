# calculator automation project

x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))

# prints the operation list
print("1 to Add")
print("2 to Subtract")
print("3 to Mulitply")
print("4 to Divide")

operation = int(input("Which operation do you want? "))

def calculate(x, y):
    if operation == 1:
        add = x + y
        print(x, " + ", y, " = ", add)
    
    elif operation == 2:
        subtract = x - y
        print(x, " - ", y, " = ", subtract)

    elif operation == 3:
        multiply = x * y
        print(x, " x ", y, " = ", multiply)
    
    elif operation == 4:
        divide = x - y
        print(x, " / ", y, " = ", divide)
    




if operation <= 4:
    calculate(x, y)
else:
    print("Invalid answer.")