x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print(f"{x} is the largest number.")
elif y > x:
    print(f"{y} is the largest number.")
else:
    print("Both numbers are equal.")
    