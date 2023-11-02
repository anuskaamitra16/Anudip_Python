# Function to convert kilometers to miles
def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Input from the user
kilometers = float(input("Enter distance in kilometers: "))

# Convert and display the result
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles")


#OUTPUT

#Enter distance in kilometers: 10
#10.0 kilometers is equal to 6.21371 miles
