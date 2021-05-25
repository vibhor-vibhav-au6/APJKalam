'''Write a program using recursion to count the number of
vowels in a string.'''


def vowelCounter(string):
  if string == '':
    return 0
  if string[0] in 'aeiouAEIOU':
    return 1 + vowelCounter(string[1:])
  else:
    return vowelCounter(string[1:])
 
  
# print(vowelCounter(input('enter a string')))

'''
Write a program to find the fibonacci number in a string
'''
def fibonacci(n):
  if n == 1:
    return 1
  if n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
  

'''
Write a program to find the length of a string using recursion
'''
def lengthOfString(string):
  if string == '':
    return 0
  return 1+lengthOfString(string[1:])

print(lengthOfString('vibhor'))