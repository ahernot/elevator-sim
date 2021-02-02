# main.py
# Created by Anatole Hernot on 2021.02.02

MIN_FLOOR = 0
MAX_FLOOR = 10


class Elevator:

    def __init__(self):
        # Fixed parameters
        self.waitTime = 1.0  # wait 1.0 steps when stopped on a floor

        self.direction = 0
        self.position = 0.0 # in floor decimal values (here, at floor 0)
        self.speed = 0.1  # in floors per timeStep

        # Queues (to modify)
        self.callQueue = list()
        self.movementQueue = list()


    def step(self):
        # compute position after next step
        pass

    def moveUp(self):
        if self.floor < MAX_FLOOR:
            self.floor += 1
            return True
        return False

    def moveDown(self):
        if self.floor > MIN_FLOOR:
            self.floor -= 1
            return True
        return False

    def goTo(self, floor):
        # go to desired floor
        pass

    def call(self, floor, direction=0):
        # call from floor
        # direction = -1 for down, = +1 for up

        # Estimate desired direction
        if direction == 0:
            if floor > 0:
                direction = -1
            else:
                direction = 1

        (self.callQueue).append()



# elevator will go to
# any floor > 0 will likely wanna go down
# 0 will go to any floor > 0

# priority based on waiting time as well