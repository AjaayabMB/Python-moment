# Write a Python function that rotates a list to the left by a given number of steps.
# For example,rotating the list [1, 2, 3, 4, 5] by 2 steps should result in [3, 4, 5, 1, 2].
def rotate_list(numbers, steps):
    r = 0
    for i in range(0, steps):
        j = 0
        r = numbers.pop(j)
        numbers.append(r)
    return numbers


numbers = []
steps = int(input("Enter the no. of steps"))
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
for a in total_entries:
    entry = int(input("Enter a number"))
    numbers.append(entry)
print(rotate_list(numbers, steps))
