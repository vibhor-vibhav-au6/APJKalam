def pow(x,y):
  if y == 0:
    return 1
  
  return x*pow(x,y-1)

# 2**4 = 2*2*2*2
# pow(2,3)
# 2* pow(2,3-1)
# 2* pow(2,2-1)
# 2 * pow(2,0)

# print(pow(3,3))