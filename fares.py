def calculate_fare(distance):
    if 1 <= distance <= 50:
        fare = distance * 8
    elif 51 <= distance <= 100:
        fare = distance * 10
    else:
        fare = distance * 12

    return fare

# Input from the user
distance = int(input("Enter the distance (in kilometers): "))

# Calculate and display the fare
fare = calculate_fare(distance)

print(f"The fare for {distance} kilometers is Rs. {fare}")


#OUTPUT

#1
#Enter the distance (in kilometers): 15
#The fare for 15 kilometers is Rs. 120

#2
#Enter the distance (in kilometers): 54
#The fare for 54 kilometers is Rs. 540

#3
#Enter the distance (in kilometers): 120
#The fare for 120 kilometers is Rs. 1440
