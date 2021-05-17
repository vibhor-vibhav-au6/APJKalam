def swap(A,B):
    # A,B = B,A
    A += B
    B -= A
    A -= B
    return (A,B)

def find_perfect_square(N):
  for i in range(N):
    if i*i == N:
      return True
    
    if i*i>N:
      return False

def find_perfect_square(N):
    prime_num = []
    for i in range(1, N):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break

        if i > 1 and isPrime == True:
            prime_num.append(i) 
            
    return(prime_num)     
