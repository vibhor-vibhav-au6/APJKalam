s = 'a2c3f6'

def stringGen(s):
  if len(s) == 0:
    return s

  return s[0]*int(s[1]) + stringGen(s[2:])

print(stringGen(s))


