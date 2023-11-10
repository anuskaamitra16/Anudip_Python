#WAP to count all letters , digits , and special symbol

#define a variable with the given string from the question
string ="P@#yn26at^&i5ve"

#set at 0 for each count variable
char_count=0
digit_count=0
symbol_count=0

#for loop for finding out the count of each letters,digits,symbols in the string
for i in string:
    if i.isalpha():
        char_count=char_count+1
    elif i.isdigit():
        digit_count=digit_count+1
    else:
        symbol_count=symbol_count+1

#printing the result
print("The number of letters is:",char_count)
print("The number of digits is:",digit_count)
print("The number ofsymbols is:",symbol_count)

#Output
'''
The number of letters is: 8
The number of digits is: 3
The number ofsymbols is: 4
'''

        
