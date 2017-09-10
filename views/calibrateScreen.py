import numpy as np
import cv2
import constants

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    cv2.putText(screen, "Move up", constants.UP_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Move down", constants.DOWN_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Accept", constants.RIGHT_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Back", constants.LEFT_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    
    cv2.circle(screen, (state.currentUser.gamePositionX, state.currentUser.gamePositionY), constants.GAME_SIZE, (255,255,255))
    cv2.imshow('BrushSmart', screen)