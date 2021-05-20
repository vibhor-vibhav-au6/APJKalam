def Decimal_to_Binary(num):
  op = ''
  while num > 0:
    op += str(num%2)
    num = num//2
  
  # op += str(num)
  return int(op[::-1])


# print (Decimal_to_Binary(8))


def Convert_Binary_to_Decimal(l):
  op = 0
  for i in range(len(l)):
    op += l[len(l)-1 - i]*(2**i)
  return (op)

print(Convert_Binary_to_Decimal([1,0,1,0]))

# print(Decimal_to_Binary(3) ^ Decimal_to_Binary(4))

def findSingle( ar):
     
    op = arr[0]
     
    for i in range(1,len(arr)):
        op = op ^ arr[i]
     
    return op
 

arr = [1,1,2,2,3,4,4,]
print ("Element occurring once is", findSingle(arr))

