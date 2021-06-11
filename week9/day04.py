'''Find whether an array is subset of another array:'''
def subsetHelper(arr1,arr2):
  # arr1 = [1,2,3]
  # arr2 = [2,2,2,3]
  for i in arr1:
    if arr2.count(i) < arr1.count(i):
      return False
  return True

def subset(arr1, arr2):
  if len(arr1) >= len(arr2):
    return subsetHelper(arr2,arr1)
  else:
    return subsetHelper(arr1,arr2)

a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1, 13, 21]
# print (subset(a,b))

'''Sort an array of 0s, 1s and 2s'''
def sort012(arr):
  return [0 for i in range(arr.count(0))]+[1 for i in range(arr.count(1))]+[2 for i in range(arr.count(2))]

# print(sort012([0, 1, 2, 0, 1, 2]))

'''Sort an array in wave form
'''
def waveSort(arr, n):
     
    for i in range(0, n, 2):

        if (i> 0 and arr[i] < arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]
         
        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]