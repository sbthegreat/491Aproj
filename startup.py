# -*- coding: utf-8 -*-

import face_recognition
import cv2
import os
import user
import pickle

def getUser():
    directory = os.path.dirname(os.path.abspath(__file__)) + "\\users"
    userFiles = next(os.walk(directory))[2] # list of user files
    userList = []
    loadedEncodings = []

    for userFile in userFiles:
        file = open("users\\" + userFile,'rb')
        loadedUser = pickle.load(file)
        file.close()
        
        userList.append(loadedUser)
        loadedImage = loadedUser.image
        loadedEncodings.append(face_recognition.face_encodings(loadedImage)[0])

    onScreenFaces = []
    onScreenEncodings = []
    processing = True

    cap = cv2.VideoCapture(0)
    while True:
        # Grab a single frame of video
        ret, frame = cap.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)

        # Only process every other frame of video to save time
        if processing:
            # Find all the faces and face encodings in the current frame of video
            onScreenFaces = face_recognition.face_locations(small_frame)
            onScreenEncodings = face_recognition.face_encodings(small_frame, onScreenFaces)

            if len(onScreenFaces) != 0:
                for encoding in onScreenEncodings:
                    # See if the face is a match for a known face
                    match = face_recognition.compare_faces(loadedEncodings, encoding)
                    
                    for id in range(len(loadedEncodings)):
                        if match[id].any(): # if any of the faces on screen match the loaded user's
                            cap.release()
                            return userList[id], userList, False
                cap.release()
                newUser = user.User(frame) # only reached if face on screen was not recognized
                return newUser, userList, True
        processing = not processing