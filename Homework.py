# Write a Python program that takes a list of numbers
# and calculates the sum of all the numbers in the list.
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
sum = 0
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
    sum = sum + entry
print(list)
print(sum)
