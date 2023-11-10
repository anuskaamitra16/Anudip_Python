#WAP to find armstrong number
#take user input
num=str(int(input("Enter a number:")))
#taking another variable
digit_sum=0
#checking if the number is armstrong or not
for i in num:
    digit_sum = digit_sum + int(i)** len(num)
if int(num) == digit_sum:
    print(num, "is an Armstrong Number")
else:
    print(num, "is an Armstrong Number")
    
#Output
'''
Enter a number:153
153 is an Armstrong Number
'''
    
