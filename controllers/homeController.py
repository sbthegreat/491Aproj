from views import homeScreen
import constants
import time
import random

def Control(state):
    homeScreen.Draw(state)
    if state.direction == constants.Direction.UP:
        state.setPage(constants.Page.HISCORE)
        state.resetDirection()
    elif state.direction == constants.Direction.RIGHT:
        state.gameStart = time.time()
        state.lastGermCheck = time.time()
        state.lastGermCheck = 0
        state.germList = []
        state.gameScore = 0
        state.curId = 0
        random.shuffle(state.quadrantOrder)
        state.currentQuadrant = 0
        state.setPage(constants.Page.GAME)
        state.resetDirection()
    elif state.direction == constants.Direction.LEFT:
        state.setPage(constants.Page.HABITS)
        state.resetDirection()
    elif state.direction == constants.Direction.DOWN:
        state.setPage(constants.Page.CONFIRM)
        state.resetDirection()