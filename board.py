from boardObjects import Marker, Qix, Sparx
import pygame
import copy

class Vertex():
    def __init__(self):
        self.x = 0
        self.y = 0

class Edge():
    def __init__(self):
        self.start = None
        self.end = None
        self.next = None
        self.previous = None

    def addAfter(self, new):
        pass
        # Turn an incursion into a polygon and use it to take out points from uncaptured space

class Board():

    def __init__(self, xPos, yPos, speed, health, pushState):
        self.mainBoard = []     # Contains all possible coordinates entites can exist on
        self.captured = []      # Contains coordinates of 'captured' space
        self.capturedBuffer = []    # Contains all coordinates of space to be 'captured'
        self.playableEdge = []      # Contains coordinates of all traversable space
        self.uncaptured = []    # Contains coordinates of 'uncaptured' space
        self.edges = []         # Contains coordinates of all traversal space
        self.edgesBuffer = []   # Contains edges on Current push
        self.entities = []      # Contains all boardObjects in play
        self.theMarker = Marker(xPos, yPos, speed, health, pushState)
        self.entities.append(self.theMarker)

        pygame.display.init()
        self.mysurface = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
        self.resized = pygame.transform.scale(self.mysurface, (160, 100))

    def gameStart(self):
        
        # Construct mainBoard, starting edges of traversal, and uncaptured space
        self.mainBoard = [ (x,y) for x in range(160) for y in range(100) if 35 < x < 125 and 5 < y < 95 ]

        self.edges = [ (lmao) for lmao in self.mainBoard if (lmao[0] == 36 or lmao[0] == 124) or lmao[1] == 6 or lmao[1] == 94 ]
        self.playableEdge = copy.deepcopy(self.edges)

        self.uncaptured = [losing for losing in self.mainBoard if losing not in self.edges] 

        return

    def updateEdges(self):
        avgX = 0
        avgY = 0

        for i in self.edgesBuffer:
            self.edges.append(i)
            self.playableEdge.append(i)

            avgX+= i[0]
            avgY+= i[1]

        avgX /= len(self.edgesBuffer)
        avgY /= len(self.edgesBuffer)

        self.edgesBuffer = []

        # Set starting point for fill capture to be the average coordinates of all points in the push
        # Straight lines and lines that average to a point belonging to the buffer will capture the whole board lol
        return self.fillCapture(int(avgX), int(avgY))

    def fillCapture(self, x,y):             # Very costly method on a 100 by 100 pixel board (5+ seconds on most captures). Hence the scaled down board size
        self.capturedBuffer.append((x,y))   # Append Starting point

        for coor in self.capturedBuffer:    # Checks adjacent points if they are captured, otherwise capture space and append to buffer

            if (coor[0]+1,coor[1]) in self.uncaptured and (coor[0]+1,coor[1]) not in self.capturedBuffer:
                self.capturedBuffer.append((coor[0]+1,coor[1]))
                self.uncaptured.remove((coor[0]+1,coor[1]))
            
            if (coor[0]-1,coor[1]) in self.uncaptured and (coor[0]-1,coor[1]) not in self.capturedBuffer:
                self.capturedBuffer.append((coor[0]-1,coor[1]))
                self.uncaptured.remove((coor[0]-1,coor[1]))
            
            if (coor[0],coor[1]+1) in self.uncaptured and (coor[0],coor[1]+1) not in self.capturedBuffer:
                self.capturedBuffer.append((coor[0],coor[1]+1))
                self.uncaptured.remove((coor[0],coor[1]+1))
            
            if (coor[0],coor[1]-1) in self.uncaptured and (coor[0],coor[1]-1) not in self.capturedBuffer:
                self.capturedBuffer.append((coor[0],coor[1]-1))
                self.uncaptured.remove((coor[0],coor[1]-1))


        for i in self.capturedBuffer:
            self.captured.append(i)

        self.capturedBuffer = []
    
        return


    def updatePlayable(self): 

        for i in self.edges:
            
            # Checks if edge can be removed and is diagonally adjacent to any uncaptured space
            if not self.checkIfEdge(i) and i in self.playableEdge:
                self.playableEdge.remove(i)

        return


    def checkIfEdge(self, coor):

        if (coor[0]+1,coor[1]+1) in self.uncaptured:
            return True

        if (coor[0]-1,coor[1]+1) in self.uncaptured:
            return True

        if (coor[0]-1,coor[1]-1) in self.uncaptured:
            return True

        if (coor[0]+1,coor[1]-1) in self.uncaptured:
            return True

        return False
    

    def printPercentage(self):  # 50% of board must be captured to win
        result = ((len(self.edges) +len(self.captured)) / len(self.mainBoard)) * 100
        print("{:.1f}% of the Board is Captured".format(result))
        return

    def getMarker(self):
        return self.entities[0]

    def createEntities(self, level): # level determines number of enemy entities

        # Player wants to start at the middle bottom edge
        
        # player = Marker(80, 94, 1, 5, False)  
        # self.entities.append(player)
        # player = Marker(320, 439, 1, 5, False)  

        return

    def draw(self):
        self.resized.fill(0)

        for coor in self.edges:
            pygame.draw.rect(self.resized, pygame.Color(255,255,255),pygame.Rect(coor[0],coor[1],1,1))
        for coor in self.playableEdge: # Omit drawing playable edges in later iterations
            pygame.draw.rect(self.resized, pygame.Color(255,0,255),pygame.Rect(coor[0],coor[1],1,1))
        for coor in self.uncaptured:
            pygame.draw.rect(self.resized, pygame.Color(23,0,0),pygame.Rect(coor[0],coor[1],1,1))
        for coor in self.edgesBuffer:
            pygame.draw.rect(self.resized, pygame.Color(255,0,0),pygame.Rect(coor[0],coor[1],1,1))
        for coor in self.captured:
            pygame.draw.rect(self.resized, pygame.Color(210,105,30),pygame.Rect(coor[0],coor[1],1,1))
        
        for entity in self.entities:
            #print(entity.theRect)
            pygame.draw.rect(self.resized, pygame.Color(0,255,255) , entity.theRect)

        #pygame.draw.rect(resized, pygame.Color(0,255,0) , player)
        self.mysurface.blit(pygame.transform.scale(self.resized, self.mysurface.get_rect().size), (0,0))   # Scale 160 by 100 board to 1280 by 800

        pygame.display.flip()

    def validateMove(self, keyPress, incr):
        return

    def updateLocations(self):
        return