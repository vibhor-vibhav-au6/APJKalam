'''
n = 5
**
  **
    **
  **
**
n=3
**
  **
** 
'''
# n = int(input('enter n'))
n = 5

# for i in range(n):
#   if i < n//2:
#     print (' '*i, '**')
#   else:
#     print (' '*(n-1-i), '**')


'''
n = 5
  1
 121
12321
n = 4
   1
  121
 12321
1234321 
'''
# for i in range(1,n+1):
#   l = [j for j in range(1,i+1)]  
#   l = l[:-1:]+l[::-1]
#   print(' '*(n-i), *l, sep = '')
  


'''
n = 3
 1
121
 1
n = 5
  1
 121
12321
 121
  1 
'''
# for i in range(1,n+1):
#   if i <= n//2:
#     l = [j for j in range(1,i+1)]  
#     l = l[:-1:]+l[::-1]
#     print(' '*(n-i), *l, sep = '')
#   else:
#     l = [j for j in range(1, n-i+2)]
#     l = l[:-1:]+l[::-1]
#     print(' '*(i-1), *l, sep = '')



'''
n = 5 
1
21
321
21
1
'''
# for i in range(n+1):
#   if i <= n//2:
#     l = [j for j in range(1,i+1)]    
#   else:
#     l = [j for j in range(1, n-i+2)]

#   print( *l[::-1], sep = '')



'''
n=3
.....
.. ..
.   .
.. ..
.....
n = 5
.......
... ...
..   ..
.     .
..   ..
... ...
.......

'''

for i in range(n-1):
  print('.'*(n-i-2), ' '*i,' '*i, '.'*(n-i-1),sep ='')
for i in range(n-2,-1,-1):
  print('.'*(n-i-1), ' '*i,' '*i, '.'*(n-i-1),sep ='' )
