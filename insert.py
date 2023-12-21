#usr/bin/env python3
def insert_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
      arr[j + 1] = key
  return arr

list = [5, 4, 1, 3, 2, 6]
sorted = insert_sort(list)
print(sorted)
