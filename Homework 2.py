# Write a Python program that takes a list of numbers and
# counts how many of them are even and how many are odd.
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
list = []
odd = 0
even = 0
for a in total_entries:
    entry = int(input("Enter a number"))
    list.append(entry)
    if (entry % 2 == 0):
        even = even + 1
    else:
        odd = odd + 1
print(odd, "odd entries")
print(even, "even entries")
