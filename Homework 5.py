# Write a Python program that reverses the order of elements in a list.
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
list_reverse = []
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
print("Normal list:")
print(list)
for a in total_entries:
    list.reverse()
print("Reversed list:")
print(list)
