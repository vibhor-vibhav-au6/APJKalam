'''
1. The Apartment has the following attributes:
flats: list of all flats
builder_name: name of the builder who built the apartment
amneties: list of all amneties in the apartments
parking_spots: number of parking spots available
number_floors: number of floors in the building
maintenance_monthly: monthly maintenance to be paid to the society
has_elevator: True or False 
num_stairs: Number of flights of stairs in the building
fire_safety: True or False 
'''

class Apartment:
    def __init__(self, builder_name, amneties, parking_spots,number_floors, maintenance_monthly, has_elevator, num_stairs,fire_safety):
        self.flats= []
        self.builder_name= builder_name
        self.amneties= amneties
        self.parking_spots=parking_spots
        self.number_floors= number_floors
        self.maintenance_monthly= maintenance_monthly
        self.has_elevator= has_elevator
        self.num_stairs= num_stairs
        self.fire_safety= fire_safety


    '''
    2. The Apartment Object supports the following methods:
    rent_flat(): Takes the first unrented flat from the list of flats and calls its rent_out() function. To the returned value add 500 if the building has lift facility and an extra 500 if fire safety measures are present. Add to this 500 for each of the amneties in the apartment and also adds the monthly societal maintenance to return the final rent.

    issue_parking_spot(): Issues a new parking spot if one is available
    revoke_parking_spot(flat): takes a flat as input and revokes its parking permissions and makes the new parking spot available.'''

    def rent_flat(self):

        rent = 0
        for i in self.flats:
            if i.current_renter == None:
                rent += (len(self.amneties) + 1) * 500
                rent += self.maintenance_monthly
                if self.has_elevator == True:
                    rent += 500
                if self.fire_safety == True:
                    rent += 500
                break
        rent += i.rent_out(rent)
        
        return (rent)

    def issue_parking_spot(self, flat_index):
        parking_spots_alloted = 0
        for i in self.flats:
            if i.has_parking_permission == True:
                parking_spots_alloted += 1

        if parking_spots_alloted < self.parking_spots:
            self.flat[flat_index].has_parking_permission = True
            return ('Flat ' + flat_index + ' alloted parking')

    def revoke_parking_spot(self, flat_index):
        self.flat[flat_index].has_parking_permission = False



# new = Apartment('abc', ['a', 'b', 'c'], 20,5, 1000, True,2, False)