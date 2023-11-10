#WAP to count and display the vowels in a given text
def vow(string, vowels):
    final= [ each for each in string if each in vowels]
    print(len(final))
    print(final)

#Driver Code
string = "Welcome to python training"
vowels= "AaEeIiOoUu"
vow(string,vowels);

#Output
'''
8
['e', 'o', 'e', 'o', 'o', 'a', 'i', 'i']
'''
