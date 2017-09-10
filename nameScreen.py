import numpy as np
import cv2
import constants

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    cv2.putText(screen, "Accept Letter", constants.UP_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Accept Name", constants.DOWN_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    
    cv2.putText(screen, "I don't recognize you. What's your name?", (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, constants.ALPHABET[state.alphabetIndex - 1], (200, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, constants.ALPHABET[state.alphabetIndex], (300, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    cv2.putText(screen, constants.ALPHABET[(state.alphabetIndex + 1) % constants.ALPHA_SIZE], (400, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, state.currentUser.name, (400, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.imshow('BrushSmart', screen)