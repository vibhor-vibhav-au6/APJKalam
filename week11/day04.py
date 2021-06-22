class Node:
  def __init__(self,val):
    self.data = val
    self.left = None
    self.right = None

def inorder(head):
  if head:
    inorder(head.left)
    print(head.data)
    inorder(head.right)

def postorder(head):
  if head:
    postorder(head.left)
    postorder(head.right)
    print(head.data)


head = Node(3)
head.left = Node(4)
head.right = Node(5)
head.left.left = Node(5)
head.left.right = Node(4)
head.right = Node(5)
head.right.right = Node(7)

print(inorder(head))
print(postorder(head))