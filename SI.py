# Input from the user
principal = float(input("Enter the principal amount (in Rs.): "))
rate_of_interest = float(input("Enter the rate of interest per year (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

# Convert the rate of interest to decimal
rate_of_interest = rate_of_interest / 100

# Calculate the simple interest
simple_interest = (principal * rate_of_interest * time_period)

# Display the result
print(f"Simple Interest on Rs. {principal} for {time_period} years at {rate_of_interest*100}% per year is Rs. {simple_interest}")


#OUTPUT

#Enter the principal amount (in Rs.): 200
#Enter the rate of interest per year (in percentage): 5
#Enter the time period (in years): 5
#Simple Interest on Rs. 200.0 for 5.0 years at 5.0% per year is Rs. 50.0
