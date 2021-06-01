'''
Write a program to print sum of right diagonal of a matrix:
'''

def rtDiagonalSum(matrix):
  # i = len(matrix)
  j = len(matrix[0]) - 1
  sum = 0
  for i in range(len(matrix)):
    sum += matrix[i][j-i]
    print (sum)

  return sum


m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# print(rtDiagonalSum(m))

'''
Write a program to print sum of border elements of a square Matrix
'''

def borderSum(matrix):
  sum = 0
  l = len(matrix)
 
  for i in range(l-1):
    if (i==0):
      for j in range(l):
        sum += matrix[i][j] + matrix[l-1][j]
    else:
      sum += matrix[i][0] + matrix[i][l-1]
  return sum

m2 = [[1,2,3,4],[4,5,6,5],[7,8,9,6],[4,9,8,7]] 
# print(borderSum(m2))

'''
Write a function to return sum of rows of a matrix as a list
'''
def sumRows(matrix):

  return [sum(matrix[i]) for i in range(len(matrix))]

print(sumRows(m2))