class Sun:
    def __init__(self, daytime: int, nigthtime: int):
        self.day = daytime
        self.nigth = nigthtime

class Tree:
    def __init__(self, air: int):
        self.air = air
    def foo(self):
        sun = Sun(10, 10)
        if sun.day > 0:
            for i in range(sun.day):
                self.air += 60
        print(self.air)
        
class Grass:
    def __init__(self):
        print("frog eating a grass")

class Frog():
    def __init__(self, move_length,move_width):
        self.move_length = move_length
        self.move_width = move_width
        
    def move(self):
        if self.move_length:
            print("frog move left and right")
        if self.move_width:
            print("frog move up and down")
    def sleep(self):
        self.move_length = 0
        self.move_width = 0
        print("frog is sleep")
    def awake(self):
        tree = Tree(20)
        sun = Sun(10, 10)
        print("555")
        if sun.day > 0:
            for i in range(sun.day):
                tree.air -= 10
                if i % 4 == 0:
                    grass = Grass()
        
frog = Frog(0, 5)
frog.awake()
