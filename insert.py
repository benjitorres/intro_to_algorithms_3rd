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

"""
explaining the steps I used to solve this and why it works 

we define the function we want to use as 'insert_sort' because we want to use to sort numbers in a list or array

so we say i is the range between 1 and the length of the array

we define key as the number i in the array
we also say j is i minus 1

while j is greater than or equal to zero AND key is less than j, we define number j in the array as j plus 1
once this step finishes, we take one away from j
then we redefine key as the number j plus one in the array

once these three steps are done, we return the array which will list all of them in order

idk i give up on more clarity but yearh
"""
