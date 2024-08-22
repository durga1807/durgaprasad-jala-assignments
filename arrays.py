arr = [10, 20, 30, 40]
sum = 0
for i in range(0, len(arr)):
    sum = sum + arr[i]
print("Sum of all integer values in array: ", sum)


# Write a function to calculate the average value of an array of integers.

def cal_average(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num + i

    avg = sum_num / len(num)
    return avg


print("The average is", cal_average([10, 21, 32, 43, 54]))

# Write a program to find the index of an array element.

arr = [1, 3, 5, 3, 1, 2, 6, 5, 3, 8, 6, 9]

index = arr.index(3)
print("Index of 3: ", index)

index = arr.index(9)
print("Index of 9: ", index)

index = arr.index(8)
print("Index of 8: ", index)

# Write a function to test if array contains a specific value.


arr = [4, 5, 45, 40, 50]
for num in arr:
    if num == 5:
        print("Element exist")

# Write a function to remove a specific element from an array.


arr = [44, 55, 0, 15, 19, 5, 4]

arr.remove(0)
print(arr)

# Write a function to copy an array to another array


arr = ['k', 'a', 's', 'h', 'i']
arr1 = []
arr1 = arr.copy()
print(arr1)

# Write a function to insert an element at a specific position in the array.


arr = [101, 303, 404, 505, 606, 707, 808, 909]
arr.insert(1, 202)  # insert 202 at index 1 in arr
print(arr)

# Write a function to find the minimum and maximum value of an array.
arr = [100, 3, 3000, 20, 500, 9999, 10000, 10003]


minposition = arr.index(min(arr))
print("The minimum is at position:", minposition)

maxposition = arr.index(max(arr))
print("The maximum is at position::", maxposition)

# Write a function to reverse an array of integer values.


arr = [9, 8, 7, 6, 5]
arr.reverse()
print(arr)

# Write a function to find the duplicate values of an array.

arr = [21, 11, 31, 13, 11]
for i in range(0, len(arr)):
    for k in range(i + 1, len(arr)):
        if arr[i] == arr[k]:
            print("Duplicate element in given array:", arr[k])

# Write a program to find the common values between two arrays.


arr = ['k', 'a', 's', 'h', 'i']
arr1 = ['s', 'h', 'g']
print("Common values in given arrays:", set(arr).intersection(arr1))

# Write a method to remove duplicate elements from an array.y
arr = [11, 22, 33, 11, 44, 55]
finalarr = []
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)

# Write a method to find the second largest number in an array.

arr = [101, 404, 202, 909, 606, 505, 808, 303, 707]
arr.sort()
print("Second largest number:", arr[-2])

# Write a method to find number of even number and odd numbers in an array.


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evennumbers = 0
oddnumbers = 0

for i in arr:
    if i % 2 == 0:
        evennumbers += 1
    else:
        oddnumbers += 1
print("Even Numbers in given array:", evennumbers)
print("Odd Numbers in given array:", oddnumbers)

# Write a function to get the difference of largest and smallest value.

arr = [10, 6, 11, 13, 14]
arr.sort()
print("Diffrence of largest and smallest value:", arr[4] - arr[0])

# Write a method to verify if the array contains two specified elements(12,23).

arr = [1, 12, 19, 23, 33, 54]
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")
