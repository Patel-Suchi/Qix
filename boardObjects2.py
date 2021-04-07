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
        self.theRect = pygame.Rect(320,439,25,25)
        self.lastVertex = []
        self.nextVertex = []
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
        keys = pygame.key.get_pressed()
        moveVector = (player.x + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]), player.y + (keys[pygame.K_DOWN] - keys[pygame.K_UP]))

        return

class Sparx(Object):
    def __init__(self, xPos, yPos, speed):
        super().__init__(xPos, yPos, speed)


class Qix(Object):
    def __init__(self, xPos, yPos, speed, orientation, directionOfTravel):
        self.orientation = orientation
        self.directionOfTravel = directionOfTravel
        super().__init__(xPos, yPos, speed)

    