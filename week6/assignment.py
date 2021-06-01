'''
Given a Square Matrix of Dimension NXM , find all Non-Diagonal Elements which are prime Numbers .
'''

d = {}

def isPrime(num):
  if num in d:
    return d[num]

  if num > 1: 
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            d[num] = False
            return False
    else:
        d[num] = True
        return True
  else:
    return False

def func(matrix):
  res = []
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if i != j:
        if isPrime(matrix[i][j]) == True:
          res.append(matrix[i][j])
  
  return res


# print(func([[1,2,3] , [4,5,6] , [7,8,9]]))

'''Given a integer array , find all the numbers which are palindrome'''

def isPalindrome(num):
  if str(num) == str(num)[::-1]:
    return True
  return False

def palindromeChecker(arr):
  return [i for i in arr if isPalindrome(i) == True ]



# print(palindromeChecker([1 , 2 , 256 , 252 , 1441 , 969 ,2331]))

'''
Given an integer array , find all the numbers whose digit sum is even
'''
def isDigitSumEven(num):
  if num < 10:
    if num%2  == 0 : return True

  digitSum = 0
  while num > 0:
    digitSum += num%10
    num = num //10
  
  if digitSum%2 == 0:
    return True
  
  return False

def digitSumChecker(arr):
  return [i for i in arr if isDigitSumEven(i) == True]

# print(digitSumChecker([1 , 2 , 1111,56 ,22 ,89 ,100]))

'''
Given an array of size n and a number k, find all elements that appear more than n/k times'''

def nkTimes(arr, k):
  d = {}
  nk =len(arr)//k
  for i in arr:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  
  return [i for i in d if d[i]>nk]

# print(nkTimes( [ 3 ,1, 2, 2, 2, 1, 4, 3, 3 ], 4))


'''
Given an array arr[], find the maximum j – i such that arr[j] > arr[i] 
'''

def maxIndexDiff(arr, n):
    maxDiff = -1
    for i in range(0, n):
        j = n - 1
        while(j > i):
            if arr[j] > arr[i] and maxDiff < (j - i):
                maxDiff = j - i
            j -= 1
 
    return maxDiff


    
