# Write a Python program that checks if a given list is a palindrome
# (i.e., it reads the same forwards and backwards).
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
stuff=range(x,0)
list = []
list2 = []
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
for b in stuff:
    r=list[b]
    list2.append(r)
    b-=1
if (list == list2):
    print("The list is palindrome")
else:
    print("The list is not palindrome")
    print(list2)