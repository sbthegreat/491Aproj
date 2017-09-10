import datetime

class User():
    def __init__(self, image):
        self.name = ""
        self.image = image
        self.gamePositionX = 400
        self.gamePositionY = 400
        self.highScore = 0
        self.brushingTimes = {}
        self.registerDate = datetime.date.today()