from views import confirmScreen
import constants

def Control(state):
    confirmScreen.Draw(state)
    if state.direction == constants.Direction.UP:
        state.setPage(constants.Page.HOME)
        state.resetDirection()
    elif state.direction == constants.Direction.DOWN:
        state.active = False