width = 128
height = 128

#resource types: coal, iron, water, sand, 
class Resource:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def take(self, value):
        self.value -= value

    def add(self, value):
        self.value += value

    def get_value(self):
        return self.value
    
    
class Map:
    def __init__(self):
        self.dimension = (width,height)

        #create locations of resources by distribution
        #total resource value distributed randomly to 5 sites

        #

class Player:
    def __init__(self):
        self.score = 0
        self.inventory = {}
        self.position = (width//2, height//2)

    def extract(self, value):
        

class Game:
    def __init__(self):
        self.playing = True
        self.map = Map()
        self.step = 0
        self.player = Player()

    def play(self):
        
        while self.playing:


            self.step += 1



class Event: