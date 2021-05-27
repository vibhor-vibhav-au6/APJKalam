'''Write a program using recursion to count the number of
vowels in a string.'''
'anything'
# 1+ vowelCounter('nything')
# vowelCounter('ything')
# vowelCounter('thing')
# vowelCounter('ing')
# 1+vowelCounter('ng')
# vowelCounter('g')
# vowelCounter('')



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

# print(fibonacci(4))

# 1,1,2,3,5,8...
# 1,2,3,4,5,6

# f(n) = f(n-1)+f(n-2)
# f(6) = f(5) + f (4)

# f(5) = 5+3 = 8
  

'''
Write a program to find the length of a string using recursion
'''
# vibhor
# 1+ lengthOfString(ibhor)
# 2+ lengthOfString(bhor)
# 3+ lengthOfString(hor)
# 4+ lengthOfString(or)
# 5+ lengthOfString(r)
# 6 + lengthOfString('')

def lengthOfString(string):
  if string == '':
    return 0

  return 1+lengthOfString(string[1:])

# print(lengthOfString('1234567890'))




