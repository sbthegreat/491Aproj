from views import nameScreen
import constants

def Control(state):
    nameScreen.Draw(state)
    if state.direction == constants.Direction.UP:
        state.currentUser.name += constants.ALPHABET[state.alphabetIndex]
        state.resetDirection()
    elif state.direction == constants.Direction.RIGHT:
        state.alphabetIndex = (state.alphabetIndex + 1) % constants.ALPHA_SIZE
        state.resetDirection()
    elif state.direction == constants.Direction.LEFT:
        state.alphabetIndex = (state.alphabetIndex - 1) % constants.ALPHA_SIZE
        state.resetDirection()
    elif state.direction == constants.Direction.DOWN:
        state.setPage(constants.Page.CALIBRATE)
        state.resetDirection()