# Write a Python program that calculates the sum of only the positive numbers in a list.
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
sum = 0
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
    if (entry > 0):
        sum = sum + entry
print("Sum of only positive numbers:", sum)
