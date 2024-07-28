#Write a Python program that checks if a given list is a palindrome
# (i.e., it reads the same forwards and backwards).
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
if(list==list.reverse()):
    print("The list is palindrome")
else:
    print("The list is not palindrome")