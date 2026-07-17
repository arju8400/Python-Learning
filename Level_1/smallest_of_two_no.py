x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x < y:
    print(f"{x} is the smallest number.")
elif y < x:
    print(f"{y} is the smallest number.")           
    
else:
    print("Both numbers are equal.")