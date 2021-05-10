'''1. The Bathroom Object has the following attributes:
length: length of the closet in feet
breadth: breadth of the closet in feet
has_sink: True or False depending on whether the bathroom has a slab or not
has_bathtub: True or False depending on whether the bathroom has a bathtub or not
has_tap: True or False depending on whether the bathroom has a tap or not
has_shower: True or False depending on whether the bathroom has a shower or not'''


class Bathroom:
    def __init__(self, length, breadth, has_sink, has_tub, has_shower,                 has_tap):
        self.length = length
        self.breadth = breadth
        self.has_sink = has_sink
        self.has_tub = has_tub
        self.has_tap = has_tap
        self.has_shower = has_shower

        
        '''
        2. The Bathroom Object supports the following methods:
        bathing(): checks if atleast any one of the tap, shower or sink are available
        and returns “Suitable for bathing”, if not available it returns “Unsuitable for
        bathing”
        '''

    def bathing(self):
        if self.has_sink or self.has_tap or self.has_shower == True:
            return ('Suitable for bathing')
        else:
            return ('Unsuitable for bathing')
