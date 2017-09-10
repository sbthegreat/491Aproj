from views import habitsScreen
import constants
import datetime

def Control(state):
    habitsScreen.Draw(state)
    if state.direction == constants.Direction.RIGHT:
        state.selectedMonth = (state.selectedMonth % 12) + 1
        state.resetDirection()
    elif state.direction == constants.Direction.LEFT:
        state.selectedMonth = ((state.selectedMonth - 2) % 12) + 1
        state.resetDirection()
    elif state.direction == constants.Direction.DOWN:
        state.setPage(constants.Page.HOME)
        state.resetDirection()