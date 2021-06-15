'''Binary to decimal'''
def binaryToDecimal(num):
  res = 0
  base = 1
  
  while(num):
      lastDigit = num % 10
      num = int(num / 10)
        
      res += lastDigit * base;
      base = base * 2

  return res

'''Write a function to perform XOR between two positive integers:do not use the xor operator.
'''
def DecimaltoBinary(num):
  op = ''
  while num > 0:
    op += str(num%2)
    num = num//2
  
  # op += str(num)
  return int(op[::-1])


def xorOp(num1, num2):
  b1 = DecimaltoBinary(num1)
  b2 = DecimaltoBinary(num2)

  bRes = b1^b2
  return(binaryToDecimal(bRes))
  
  

