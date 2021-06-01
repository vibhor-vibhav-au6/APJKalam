'''
Tell space complexity of following piece of code: (5 marks)
for i in range(n): 
  for j in range(n):
    print(“Space complexity”)

'''
# O(N) = o(n) * o(n) = o(n^2)

'''
Reverse an array of integers and do not use inbuilt functions like “reverse”, don’t use shorts hands like “arr[::-1]”. Only use following approach:
swap first and last element,
then second and second last element,
till middle.
'''

def rev(arr):
  l = len(arr)

  for i in range(l//2):
    arr[i], arr[l-i-1] = arr[l-i-1], arr[i]
  
  return arr




print(rev([1,2,3,4,5,6,7,8,9]))