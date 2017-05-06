import datetime

class User():
    def __init__(self, image):
        self.name = ""
        self.image = image
        self.gamePosition = (0,0)
        self.highScore = 0
        self.brushingTimes = {}
        self.registerDate = datetime.date.today()