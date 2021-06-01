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
while(i**2<=n): 0,1,4,9,16,25,36,49,64,81
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
Big O' = O(M+N) = O(K)


'''
n= int(input(“Enter the limit”))
for i in range(n): -->o(n)
  for j in range(i): --> 0+1+2+3--+n = n(n+1)/2 = n**2 
    for k in range(100): o(100)--> O(1) 
      print(“Time complexity”)
'''
Big O' = 100* O(N**2)* o(n)= O(N**3)

'''
n= int(input(“Enter the limit”))
for i in range(n): o(n)
  j = 1
  while(j<=i**2):    o(n**2)
    for k in range(n/2): o(n)
      print(“Time complexity”)
'''
Big O' = O(N)*O(N**2)*O(N/2) = O(N**4)