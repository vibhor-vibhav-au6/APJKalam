import bed
import closet



class Bedroom:
  def __init__(self,length, breadth, heigth, has_balcony,has_window, num_lights,has_ac, has_fan, has_charging_points):
    self.length = int(length)
    self.breadth = int(breadth)
    self.height = heigth
    self.has_balcony = has_balcony
    self.has_window = has_window
    self.num_lights = num_lights
    self.has_ac = has_ac
    self.has_fan = has_fan
    self.has_charging_points = has_charging_points
    self.bed = None
    self.closet = None
  
# carpet_area(): Returns the carpet area of the room which is calculated as length*breadth
  def carpet_area(self):
    return (self.length * self.breadth)

# add_bed(): creates a Bed object using user inputs [using input() function] and assigns it to the bed attribute of the bedroom 
  def add_bed(self):
    length = input('len of bed:')
    breadth = input('breadth of bed:')
    year = input('enter the year made? ')
    if (year < 2015):
      posts = False
    else:
      posts = input('has posts?')
      
    headboard = input('has head board?')
    material  = input('material')
    self.bed = bed.Bed(length, breadth, year, posts,headboard, material)



  
  def add_closet(self,length, breadth, max_capacity):
    # length = input('length of closet')
    # breadth = input('breadth of closet')
    # max_capacity = input('max_capacity of closet')

    self.closet = closet.Closet(length, breadth, max_capacity)
     

# remove_bed(): Checks if the bed attribute is None. If not, then makes it None and returns “bed removed from the room”. If bed attribute is already None, then it returns “No bed found in the room”.  
  def remove_bed(self):
    if self.bed == None:
      return ('No Bed foundin the room!')
    else:
      self.bed = None
      return ('Bed removed from the room')
    

# remove_closet(): Checks if the closet attribute is None. If not, then makes it None and returns “closet removed from the room”. If closet attribute is already None, then it returns “No closet found in the room”.
  def remove_closet(self):
    if self.closet == None:
      return ('No closet found in the room!')
    else:
      self.closet = None
      return ('closet removed from the room')