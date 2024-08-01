# Write a Python function that rotates a list to the left by a given number of steps.
# For example,rotating the list [1, 2, 3, 4, 5] by 2 steps should result in [3, 4, 5, 1, 2].
def rotate_list(numbers, steps):
    temp = []
    list_1 = []
    list_2 = []
    new_list = []
    l = len(numbers)
    c = l - steps
    rotate = range(l, c, -1)
    while c > 0:
        rot = numbers[c - 1]
        temp.append(rot)
        c = c - 1
    # print(temp)
    y = range(len(temp) - 1, -1, -1)
    for b in y:
        list_1.append(temp[b])
    # print(list_1)
    for e in rotate:
        list_2.append(e)
    new_list.append(list_2)
    new_list.append(list_1)
    # for f in range(0,l):
    #     g=len(list_2)-1
    #     h=len(list_1)-1
    #     if(g!=-1):
    #         new_list.append(list_2[g])
    #         g-=1
    #     elif(h!=-1):
    #         new_list.append(list_1[h])
    # return new_list


numbers = []
steps = int(input("Enter the no. of steps"))
x = int(input("Enter the number of entries:"))
total_entries = range(0, x)
for a in total_entries:
    entry = int(input("Enter a number"))
    numbers.append(entry)
# rotate_list(numbers, steps)
print(rotate_list(numbers, steps))
