'''
n= int(input(“Enter the limit”))
for i in range(n):
  for j in range(n):
    for l in range(n):
      …
        …
          …
            K for loops in total
              …
                …
                  …
                  for z in range(n):
                  print(“Time complexity”)
'''
Big O' = O(N**K)

'''
n= int(input(“Enter the limit”))
def func(n):
  if n>=1:
    func(n-1)
    print(“Time complexity”)

'''
Big O' = O(N)

'''
n= int(input(“Enter the limit”))
i = 1
while(i**2<=n):
  print(“Time complexity”)
  i += 1
'''
Big O' = O(logN)



'''
N= int(input(“Enter the limit”))
M= int(input(“Enter the limit”))
a = b = 0
for i in range(N):
  a = a + 1
for j in range(M):
  b = b + rand()
'''
Big O' = O(M+N)


'''
n= int(input(“Enter the limit”))
for i in range(n):
  for j in range(i):
    for k in range(100):
      print(“Time complexity”)
'''
Big O' = 100* O(N**2)= O(N**2)

'''
n= int(input(“Enter the limit”))
for i in range(n):
  j = 1
  while(j<=i**2):
    for k in range(n/2):
      print(“Time complexity”)
'''
Big O' = O(N)*O(N**2)*O(N/2) = O(N**4)