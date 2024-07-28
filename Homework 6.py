# Write a Python program that removes all negative numbers from a list and
# returns a new list containing only non-negative numbers.
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
print("Original list:")
print(list)
for a in total_entries:
    if (list[a] < 0):
        list.remove(list[a])
print("New list:")
print(list)
