# Write a Python program that creates a new list
# containing only the odd numbers from a given list of numbers.
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
list_odd = []
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
    if (entry % 2 != 0):
        list_odd.append(entry)
print("Normal List:")
print(list)
print("Odd only list:")
print(list_odd)
