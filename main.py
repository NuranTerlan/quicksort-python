import random

# A -> Array, l -> left bound, r -> right bound

def PartitionSeparator(A, l, r):
  x = A[l]
  j = l
  for i in range(l + 1, r + 1):
    if A[i] <= x:
      j += 1
      if A[i] != A[j]:
        print(f"{A[i]} and {A[j]} swapped")
      A[j], A[i] = A[i], A[j]
  A[l], A[j] = A[j], A[l]
  return j


def QuickSort(A, l, r):
  print(f"let's start to quick sort array {A}")
  if l >= r:
    return A
  pivot = PartitionSeparator(A, l, r)
  print(f"pivot is {pivot}")
  # A[pivot] is in the final position

  # sort recursively left side of pivot which is in final pos
  QuickSort(A, l, pivot - 1)
  # sort recurively right side of pivot which is in final pos
  QuickSort(A, pivot + 1, r)


def RandomizedQuickSort(A, l, r):
  print(f"let's start to quick sort array {A}")
  if l >= r:
    return A
  random_key = random.randint(l, r)
  A[l], A[random_key] = A[random_key], A[l]
  pivot = PartitionSeparator(A, l, r)
  print(f"pivot is {pivot}")
  # A[pivot] is in the final position

  # sort recursively left side of pivot which is in final pos
  RandomizedQuickSort(A, l, pivot - 1)
  # sort recurively right side of pivot which is in final pos
  RandomizedQuickSort(A, pivot + 1, r)


unsorted_arr = [random.randint(1, 100) for _ in range(20)]
print("initial given array: ", unsorted_arr)

RandomizedQuickSort(unsorted_arr, 0, len(unsorted_arr) - 1)
print("\nresult of quick sort: ",unsorted_arr)