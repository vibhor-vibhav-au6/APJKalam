import string

alpha = string.ascii_lowercase

# print(alpha[25])

n = int(input('enter N \n'))
L = []
i = 0

'''
n =  5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
'''
while i < n:
    s = "-".join(alpha[i:n])
    # print (s)
    cs = (s[::-1]+s[1:]).center(4*n-3, "-")
    # print(cs)
    L.append(cs)
    i += 1
# print (*L, sep = "\n")
print('\n'.join(L[::-1]))


'''
n = 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''


while i < n:
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    i += 1
print('\n'.join(L[::-1]+L[1::]))