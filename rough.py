queue1 = [1,2,3,4]
queue2 = []

from queue import Queue

# print(help(Queue))


class stack:
  def __init__(self):
    self.q1 = Queue()
    self.q2 = Queue()
    self.size = 0
  
  def push(self, a):
    self.q1.put(a)
    self.size += 1
    return a
  
  def pop(self):
    count  = 0
    while count < self.size-1:
      self.q2.put(self.q1.get())
      count += 1    
    temp = self.q1.get()
    self.size -= 1
    self.q1, self.q2 =  self.q2, self.q1

    return temp

stack1 = stack()
print(stack1.push('a'))
print(stack1.push('roopam'))
print(stack1.push('sri'))
# stack1.peek()
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())



