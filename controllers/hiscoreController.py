from views import hiscoreScreen
import constants

def Control(state):
    hiscoreScreen.Draw(state)
    if state.direction == constants.Direction.DOWN:
        state.setPage(constants.Page.HOME)
        state.resetDirection()