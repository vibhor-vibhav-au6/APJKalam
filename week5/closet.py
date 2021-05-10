class Closet:
  def __init__(self,length, breadth, max_capacity):
    self.length = length
    self.breadth = breadth
    self.max_capacity = max_capacity
    self.items = []

  def store_item(self):
    toAdd = input('enter the items to push: ')
    self.items.append(toAdd)

  def fetch_item(self):
    self.items.pop(0)


# newCloset = Closet(10,10,20)
# print(newCloset.__dict__)
# newCloset.store_item()
# newCloset.store_item()
# print (newCloset.__dict__)
# newCloset.fetch_item()
# print (newCloset.__dict__)