'''Check if a number is Palindrome'''

def isPalindrome(string):
   if len(string) < '1':
      return True
   else:
      if string[0] == string[-1]:
         return isPalindrome(string[1:-1])
      else:
         return False



# print(isPalindrome('abcdba'))

'''Program for Sum of the digits of a given number'''
def sumDigits(num):
  if num < 10 :
    return num
  return num%10 + sumDigits(num//10)


# print(sumDigits(1))

'''Given a number n, find sum of first n natural numbers'''

def sumNaturalNum(n):
  if n < 1:
    return 0
  return n + sumNaturalNum(n-1)
5

# print(sumNaturalNum(5))


'''Given two number x and y, find product using
recursion'''

def recusiveMul(x,y):
  if y < 1:
    return 0
  return x + recusiveMul(x,y-1)

print(recusiveMul(4,5))

# 4*5 = 4+4+4+4+4 = 5+5+5+5