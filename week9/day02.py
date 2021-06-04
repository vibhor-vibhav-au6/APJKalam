'''
Write a program perform selection sort using an auxiliary (extra) list,
and tell the time complexity and space complexity of your code
'''
def selSort(arr):
  # n = len(arr)
  res = []
  while len(arr)>0:
    min  = 0
    for i in range(len(arr)):
      if arr[min] > arr[i]:
        min = i
    res.append(arr[min])
    arr.pop(min)
    # arr.remove(arr[min])
  return res

print(selSort([64, 25, 12, 22, 11]))


'''
Write a while loop implementation of selection sort? '''

def selSortWhile(arr):
  n = 0
  
  while n < len(arr):
    min = n 
    next = min+1

    while next < len(arr) :
      if(arr[min] > arr[next]):
        min = next
      next += 1

    arr[n], arr[min] = arr[min],arr[n]
    n += 1

  return (arr)

print(selSortWhile([64, 25, 12, 22, 11]))



