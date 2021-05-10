import bed , closet, kitchen, bathroom, bedroom,flat, apartment
'''
Making Bed and Closet OBJECTS using Class Bed & Class Closet

BED:
(length, breadth, year_made,has_headboard, has_posts, material)

CLOSET:
(length, breadth, max_capacity)
1.store_item()
2.fetch_item()
'''
bed_normal = bed.Bed(1,1,2000,1,1,'wood')
closet_normal = closet.Closet(8,3,20)
print

''' 
Making Rooms , Bathroom and Kitchen OBJECTS using respective CLASSES
BEDROOM:
(length, breadth, heigth, has_balcony,has_window, num_lights,has_ac, has_fan, has_charging_points)
>carpet_area()
>add_bed()
>add_closet()
>remove_bed
>remove_closet()

KITCHEN:
(slab_material, length,breadth,has_sink,has_slab, furnishing_material, lpg_pipeline)
>cook()

BATHROOM:
(length, breadth, has_sink, has_tub, has_shower,has_tap)

'''
kitchen_lpg = kitchen.Kitchen('granite',10,10,1,1,'wood',1)
kitchen_no_lpg = kitchen.Kitchen('marble',10,10,1,1,'marble', False)
bathroom_shower = bathroom.Bathroom(10,10,1,1,1,1)

room_unfurnished = bedroom.Bedroom(10,10,10,1,1,4,1,1,1)
room_furnished = bedroom.Bedroom(10,10,10,1,1,1,1,1,1,)
room_furnished.add_bed(1,1,2020,1,1,'wood')
room_furnished.add_closet(8,3,20)
# print (room_furnished.bed.__dict__)
# print (room_unfurnished.__dict__)


'''
Making flat OBJECT from Class Flat
>change_owner()
>rent_out()
'''
flat_2bhk = flat.Flat()
# flat_2bhk.add_room()
flat_2bhk.bed_rooms.append(room_unfurnished)
flat_2bhk.bed_rooms.append(room_furnished)
flat_2bhk.bath_rooms.append(bathroom_shower)
flat_2bhk.kitchens.append(kitchen_lpg)

flat_3bhk = flat.Flat()
# flat_3bhk.add_room()
flat_3bhk.bed_rooms.append(room_unfurnished)
flat_3bhk.bed_rooms.append(room_furnished)
flat_3bhk.bed_rooms.append(room_furnished)
flat_3bhk.bath_rooms.append(bathroom_shower)
flat_3bhk.bath_rooms.append(bathroom_shower)
flat_3bhk.kitchens.append(kitchen_lpg)

'''
Making apartment OBJECT from Apartment class
(builder_name, amneties, parking_spots,number_floors, maintenance_monthly, has_elevator, num_stairs,fire_safety)
>rent_flat(maintainance)
>issue_parking_spot(flat_index)
>revoke_parking_spot(flat_index)
'''

sankalpApartments = apartment.Apartment('AttainU', ['power backup', 'security guard', 'Gym'], 20,5, 1000, True,2, False)

AshfaqueApartmnets = apartment.Apartment('Ashfaque', ['power backup', 'security guard', 'Gym'], 20,5, 1000, True,2, False)

for i in range(11):
  sankalpApartments.flats.append(flat_2bhk)
  sankalpApartments.flats.append(flat_3bhk)
  AshfaqueApartmnets.flats.append(flat_2bhk)
  AshfaqueApartmnets.flats.append(flat_3bhk)
  
print(sankalpApartments.flats[0].__dict__)

sankalpApartments.rent_flat()

  
print(sankalpApartments.flats[0].__dict__)

