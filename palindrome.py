#WAP to find palindrome number
#take user input
num=int(input("Enter a number:"))
#check number is palindrome or not
num_str= str(num)
is_palindrome= True

for i in range (len(num_str)//2):
    if num_str[i] != num_str[-(i+1)]:
        is_palindrome= False
        break

if is_palindrome:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")

#Output
'''
Enter a number:121
121 is a palindrome number
'''
    
        
