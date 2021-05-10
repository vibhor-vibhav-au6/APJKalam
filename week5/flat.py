'''
1. The Flat has the following attributes:
bed_rooms: a list of all the bedrooms , initialize as empty list
bath_rooms: a list of all the bathrooms , initialize as empty list
kitchens: a list of all the kitchens, initialize as empty list
owner_name: name of the flat owner, initialize as None
current_renter: name of the current renter, initialize as None
has_parking_permission: Initialize as False
'''
# import bedroom
# import kitchen
# import bathroom


class Flat:
  def __init__(self):
    self.bed_rooms = []
    self.bath_rooms = []
    self.kitchens = []
    self.owner_name = None
    self.current_renter = None
    self.has_parking_permission = False

    '''
    2. The Flat Object supports the following methods:
    rent_out(): Checks if flat is already on rent, if not then it returns the rent of the flat which is calculated as 5*carpet_area per month. Then it asks the user whether they agree to pay that amount or not using input(), if they say Y/Yes/yes then take another input() as their name and set the current_renter attribute. Return the rent value as well.
      PS: carpet area of the flat is the sum of carpet area of all the rooms in the house.
    change_owner(): Takes a name as input from the user and changes the owner of the
    flat to that person'''
  def __rentHelper(self):
    superArea = 0

    for i in self.bed_rooms:        
      superArea += i.carpet_area()
    
    for i in self.bath_rooms:
      area = i.length * i.breadth 
      superArea = superArea + area
    
    for i in self.kitchens:
      area = i.length * i.breadth
      superArea += area

    
    
    return (superArea*5)

  def change_owner(self):
    name = input('Enter the name of the new owner!')
    self.owner_name = name


  def rent_out(self, maintainance):
    if self.current_renter != None:
      return ('Flat is unavailable!')
    
    rent = maintainance + self.__rentHelper()

    response = input('The monthly rent would be '+ str(rent) + ' Would like to continue? ')

    if response == 'y' or 'yes' or 'YES' or 'Y' or 'Yes':
      self.current_renter = input('Please enter your Name:')
      print('Welcome '+ self.current_renter+ '. You are renting the flat for INR ' +str(rent) )
      return (rent)
    
  
  # def add_room(self):
  #   length = input('enter room length : ')
  #   breadth = input('enter room breadth')
  #   height = input('enter room height')
  #   has_balcony = input('balcony present ? ')
  #   num_lights = input('No of light sources? ')
  #   has_window = input('windows present? ')
  #   has_ac = input('AC available?')
  #   has_fan = input('Fan present? ')
  #   has_charging_points = input('Charging points present? ')      

  #   newRoom = bedroom.Bedroom(length, breadth, height, has_balcony,has_window, num_lights,has_ac, has_fan, has_charging_points)
  #   self.bed_rooms.append(newRoom)

  # def add_batroom(self):
  #   length = input('enter bathoom length  : ')
  #   breadth = input('enter bathoom breadth  : ')
  #   has_sink = input('bathroom has_sink')
  #   has_tub = input('bathroom has_tub')
  #   has_tap = input('bathroom has_tap')
  #   has_shower = input('bathroom has_shower')

  #   self.bath_rooms.append(bathroom.Bathroom(length,breadth,has_sink,has_tub,has_shower, has_tap))

  # def add_kitchen(self):
  #   length = input('enter bathoom length  : ')
  #   breadth = input('enter bathoom breadth  : ')
  #   has_sink = input('kitchen has_sink')
  #   has_slab = input('kitchen has_slab')
  #   furnishing_material = input('kitchen furnishing_material')
  #   lpg_pipeline = input('kitchen lpg_pipeline')
  #   slab_material = input('kitchen slab_material')

  #   self.kitchens.append(kitchen.Kitchen(slab_material, length,breadth,has_sink,has_slab, furnishing_material, lpg_pipeline))

  # def evict_renter(self):
  #   renter = self.current_renter
  #   self.current_renter = None
  #   return (renter + ' evicted!')

      
      




