#WAP to remove duplicate characters of a given string

#take input given in the question
string="String and String Function"
str=""

#take a variable using the split function
string2=string.split()

#for loop to remove the duplicate characters
for i in string2:
    if i not in str:
        str=str+" "+i

#printing the result
print("The string before removing duplicate:",string)
print("The string after removing duplicate:",str)

#Output
'''
The string before removing duplicate: String and String Function
The string after removing duplicate:  String and Function
'''
