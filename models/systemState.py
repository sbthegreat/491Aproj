from models import user
import constants
import collections
import datetime

class SystemState():
    def __init__(self):
        self.currentUser = user.User(None)
        self.trailPoints = collections.deque()
        self.currentPage = constants.Page.HOME
        self.direction = constants.Direction.NONE
        self.lastSwipe = 0
        self.userList = []
        self.alphabetIndex = 0
        self.selectedMonth = datetime.date.today().month
        self.active = True
        self.gameStart = 0
        self.lastGermCheck = 0
        self.germList = []
        self.gameScore = 0
        self.quadrantOrder = [constants.Quadrant.TOPRIGHT, constants.Quadrant.TOPLEFT, constants.Quadrant.BOTTOMLEFT, constants.Quadrant.BOTTOMRIGHT]
        self.curId = 0
        self.currentQuadrant = 0
        self.lastQuadrantTransition = 0
        self.motionStart = (400,400)
        
    def setPage(self, newPage):
        self.currentPage = newPage
        trailPoints = collections.deque()
    
    def resetDirection(self):
        self.direction = constants.Direction.NONE

    # adds points to the trail, pops off oldest point if past length limit
    def addPoint(self, x):
        self.trailPoints.append(x)
        if len(self.trailPoints) > constants.POINT_LIMIT:
            self.trailPoints.popleft()
