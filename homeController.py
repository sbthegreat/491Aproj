import mainController as master
import homeScreen
import constants

def Control(state):
    homeScreen.Draw(state)
    if state.direction == constants.Direction.UP:
        state.setPage(constants.Page.HOME)
        state.resetDirection()
    elif state.direction == constants.Direction.RIGHT:
        state.setPage(constants.Page.GAME)
        state.resetDirection()
    elif state.direction == constants.Direction.LEFT:
        state.setPage(constants.Page.HABITS)
        state.resetDirection()
    elif state.direction == constants.Direction.DOWN:
        state.active = False
        state.resetDirection()