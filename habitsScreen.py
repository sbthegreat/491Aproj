import numpy as np
import cv2
import constants
import calendar
import datetime
import user

def Draw(state):
    screen = np.zeros((800,800,3), np.uint8)
    cv2.putText(screen, "Prev", constants.LEFT_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Next", constants.RIGHT_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(screen, "Home", constants.DOWN_NAV, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    today = datetime.date.today()
    display = calendar.Calendar().itermonthdates(today.year, state.selectedMonth)
    
    HEIGHT = 70
    WIDTH = 70
    START = (100, 100)
    OFFSET = 15
    WEEK = ['M', 'T', 'W', 'Th', 'F', 'Sa', 'Su']
    
    row = 0
    col = 0
    
    cv2.putText(screen, calendar.month_name[state.selectedMonth], (START[0] - 40, START[1] - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    for date in display:
        brushingTimes = state.currentUser.brushingTimes
        if date < state.currentUser.registerDate or date > today:
            color = (255, 255, 255) # white
        else:
            if date in brushingTimes:
                if brushingTimes[date] == 1:
                    color = (255, 0, 0) # blue
                else:
                    color = (0, 255, 0) # green
            else:
                color = (0, 0, 255) # red
        
        cv2.rectangle(screen, (START[0] + col * WIDTH + 1, START[1] + row * HEIGHT + 1), ((START[0] + (col + 1) * WIDTH, START[1] + (row + 1) * HEIGHT)), color)
        cv2.putText(screen, str(date.day), (START[0] + col * WIDTH + OFFSET, START[1] + (row + 1) * HEIGHT - OFFSET), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
        if row == 0:
            cv2.putText(screen, WEEK[col], (START[0] + col * WIDTH + OFFSET, START[1] - OFFSET), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    
        col += 1
        
        if col % 7 == 0:
            col = 0
            row += 1
    
    cv2.imshow('BrushSmart', screen)