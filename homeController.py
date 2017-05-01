import masterController as master
import homeScreen
import constants

def Control(state):
    homeScreen.Draw(state)
    if state.direction == constants.Direction.RIGHT:
        state.setPage(constants.Page.GAME)
        state.resetDirection()