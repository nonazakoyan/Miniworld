from random import randint

class MiniWorld:
    def __init__(self, daytime, nighttime, oxygen):
        self.day = daytime
        self.night = nighttime
        self.air = oxygen
    def setday(self, oday):
        self.day = oday
    def setnight(self, onight):
        self.night = onight
    def setair(self, oair):
        self.air = oair
    def getday(self):
        return self.day
    def getnight(self):
        return self.night
    def getair(self):
        return self.air
    
class Grass:
    def __init__(self, count):
        self.count = count
    def setgrass(self, countgrass):
        self.count = countgrass
    def getgrass(self):
        return self.count

class Tree(MiniWorld):
    def __init__(self, world):
        self.air = world.air
        self.day = world.day
        self.night = world.night
    def photosynthesis(self, world):
        world.air += 40
        self.setair(world.air)
        print(f"oxygen - {world.getair()}")

class Frog(MiniWorld):
    move_left = randint(0, 1)
    move_right = 1 - move_left
    def __init__(self, world):
        self.air = world.air
        self.day = world.day
        self.night = world.night
    def move(self):
        if self.move_left > 0:
            print("frog move to the left")
        if self.move_right > 0:
            print("frog move to the right")
    def sleep(self, world):
        world.air -= 10
        self.setair(world.air)
        print(f"oxygen - {world.getair()}")
    def awake(self, world):  
        world.air -= 20
        self.setair(world.air)
        print(f"oxygen - {world.getair()}")

class Program:
    day = 10
    night = 10
    oxygen = 42
    world = MiniWorld(day, night, oxygen)
    tree = Tree(world)
    frog = Frog(world)
    grass = Grass(100)
    for week in range(4):
        i, j = 0, 0
        while  i < day:
            tree.photosynthesis(world)
            frog.awake(world)
            if i % 2 == 0:
                frog.move()
            if i % 3 == 0:
                grass.setgrass(grass.getgrass() - 1)
                print(f"frog eating a grass, grass {grass.getgrass()}")
            i += 1

        while j < night:
            frog.sleep(world)
            if j % 2 == 0:
                grass.setgrass(grass.getgrass() + 1)
                print(f"grass {grass.getgrass()}")
            j += 1
    
prog = Program()
prog
