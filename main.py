import random

# A -> Array, l -> left bound, r -> right bound

def Partition3Separator(A, l, r):
  pivot_value = A[l]
  pivot_begin_key = i = l
  pivot_end_key = r

  while i <= pivot_end_key:
    if A[i] < pivot_value:
        #if A[i] != A[pivot_begin_key]:
        print(f"Swapped: {A[i]} <--> {A[pivot_begin_key]}")
        A[i], A[pivot_begin_key] = A[pivot_begin_key], A[i]
        pivot_begin_key += 1
        i += 1
    elif A[i] == pivot_value:
        i += 1
    else:
        #if A[i] != A[pivot_end_key]:
        print(f"Swapped: {A[i]} <--> {A[pivot_end_key]}")
        A[i], A[pivot_end_key] = A[pivot_end_key], A[i]
        pivot_end_key -= 1
  return pivot_begin_key, pivot_end_key


def QuickSort(A, l, r):
  print(f"let's start to quick sort array {A}")
  random_key = random.randint(l, r)
  A[l], A[random_key] = A[random_key], A[l]
  pivot_range = Partition3Separator(A, l, r)
  print(f"pivot range is {pivot_range}")
  # A[pivot] is in the final position

  # sort recursively left side of pivot which is in final pos
  QuickSort(A, l, pivot_range[0] - 1)
  # sort recurively right side of pivot which is in final pos
  QuickSort(A, pivot_range[1] + 1, r)
  return A


def RandomizedQuickSort(A, l, r):
  if l >= r:
    return A
  print(f"let's start to quick sort array {A}")
  random_key = random.randint(l, r)
  A[l], A[random_key] = A[random_key], A[l]
  pivot_range = Partition3Separator(A, l, r)
  print(f"pivot range is {pivot_range}")
  # A[pivot] is in the final position

  # sort recursively left side of pivot which is in final pos
  RandomizedQuickSort(A, l, pivot_range[0] - 1)
  # sort recurively right side of pivot which is in final pos
  RandomizedQuickSort(A, pivot_range[1] + 1, r)


unsorted_arr = [random.randint(1, 100) for _ in range(20)]
print("initial given array: ", unsorted_arr)

RandomizedQuickSort(unsorted_arr, 0, len(unsorted_arr) - 1)
print("\nresult of quick sort: ",unsorted_arr)