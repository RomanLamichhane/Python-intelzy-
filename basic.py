#  Q: given an array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# update the center element to "Hello World" using len function

# Ans:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

centerPos = int((len(arr)) // 2)

arr[centerPos] = "Hello World"

print(arr)
