
# Input the lengths of the sides from the user
a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
c = float(input("Enter the length of side 'c': "))

# Calculate the semi perimeter
s=(a+b+c)/2

# calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is:" %area)

#output

#Enter the length of side 'a': 5
#Enter the length of side 'b': 6
#Enter the length of side 'c': 7
#The area of the triangle is: 14.70
