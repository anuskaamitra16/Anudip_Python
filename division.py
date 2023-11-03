def div(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed"
    return num1 / num2

# Get user input for the numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the div() function and display the result
result = div(num1, num2)
print(f"{num1} divided by {num2} is {result}")

#OUTPUT
#Enter the first number: 10
#Enter the second number: 2
#10.0 divided by 2.0 is 5.0

