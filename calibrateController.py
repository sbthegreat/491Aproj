import calibrateScreen
import constants
import user

def Control(state):
    calibrateScreen.Draw(state)
    if state.direction == constants.Direction.UP:
        state.currentUser.gamePositionY -= constants.GAME_INCREMENT
        state.resetDirection()
    elif state.direction == constants.Direction.RIGHT:
        state.setPage(constants.Page.HOME)
        state.resetDirection()
    elif state.direction == constants.Direction.LEFT:
        state.setPage(constants.Page.ENTERNAME)
        state.resetDirection()
    elif state.direction == constants.Direction.DOWN:
        state.currentUser.gamePositionY += constants.GAME_INCREMENT
        state.resetDirection()