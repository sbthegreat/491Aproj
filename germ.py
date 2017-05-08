import constants

class Germ():
    def __init__(self):
        self.color = (255,255,255)
        self.size = 0
        self.speed = 0
        self.xPos = 0
        self.yPos = 0
        self.direction = 0
        self.active = True
        
    def move(self):
        if self.direction == constants.Direction.UP:
            self.yPos -= self.speed
        elif self.direction == constants.Direction.RIGHT:
            self.xPos += self.speed
        elif self.direction == constants.Direction.DOWN:
            self.yPos += self.speed
        elif self.direction == constants.Direction.LEFT:
            self.xPos -= self.speed