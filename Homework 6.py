# Write a Python program that removes all negative numbers from a list and
# returns a new list containing only non-negative numbers.
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
list_positive=[]
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
print(list)
for l in list:
    if(l>0):
     list_positive.append(l)
print(list_positive)