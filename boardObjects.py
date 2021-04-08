import pygame

class Object():
    def __init__(self, xPos, yPos, speed):
        self.x = xPos
        self.y = yPos
        self.speed = speed
        self.polygonList = []

    def updateLocation(self, x, y):
        self.x = x
        self.y = y
        return
    
    def getLocation(self):
        return (self.x, self.y)

    def move(self, board, keyPress, incr):
        return

    def collide(self): # if collision happens?
        return

    def draw(): # draw this object on the back buffer
        return

class Marker(Object):
    def __init__(self, xPos, yPos, speed, health, pushState):
        self.health = health
        self.pushState = pushState
        self.theRect = pygame.Rect(80,94,1,1)
        super().__init__(xPos, yPos, speed)

    def isPushing(self):
        return self.pushState

    def setIsPushing(self, state):
        # Call `fillCapture`
        self.pushState = state
        return

    def getHealth(self):
        return self.health

    def updateHealth(self):
        self.health -= 1
        return

    def move(self):
        
        return

class Sparx(Object):
    def __init__(self, xPos, yPos, speed):
        super().__init__(xPos, yPos, speed)


class Qix(Object):
    def __init__(self, xPos, yPos, speed, orientation, directionOfTravel):
        self.orientation = orientation
        self.directionOfTravel = directionOfTravel
        super().__init__(xPos, yPos, speed)

    