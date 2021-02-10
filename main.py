# main.py
# Created by Anatole Hernot on 2021.02.02


import math

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


    # always re-round position

    def step(self):
        # compute position after next step
        pass

    def moveUp(self):
        # Move up for one timeStep (if possible)
        if self.position <= MAX_FLOOR - (self.speed * 1):
            self.position += self.speed
            return True
        return False

    def moveDown(self):
        # Move down for one timeStep (if possible)
        if self.position >= MIN_FLOOR + (self.speed * 1):
            self.position -= self.speed
            return True
        return False














    # if on floor (not final dest) and same direction: stop







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





CURRENT_TIME = 0

def updatePriority(callTuple: tuple):
    # Unpack list
    priority, floorRequest, multiplier, timeOfCall = callTuple

    # Compute time delta since call
    timeSinceCall = CURRENT_TIME - timeOfCall

    # compute priority
    priority = multiplier * math.exp(priority * timeSinceCall)

    # Pack
    return (priority, floorRequest, multiplier, timeOfCall)



callList = []
for i, callTuple in enumerate(callList):
    callList[i] = updatePriority(callTuple)




# elevator will go to
# any floor > 0 will likely wanna go down
# 0 will go to any floor > 0

# priority based on waiting time as well



callQueue = list()

callQueue.append( (1, 10) )  # priority, floor
# priority multiplier, priority, floor


# priority multiplier: 1 for outside call, 2 for inside call

# e^(priority * deltaTime) every step
