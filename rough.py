
def hammingWeight(n):
    
    sum = 0
    
    while(n != 0):
        sum += 1
        print(bin(n), bin(n-1))
        n = n & (n-1)
        
        
    return sum

print(hammingWeight(0b1011))
