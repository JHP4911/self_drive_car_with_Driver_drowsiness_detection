import cv2                                       # import libraries of python OpenCV

title = 'car control'
cv2.namedWindow(title)                           # capture frames from a camera
video = cv2.VideoCapture(0)
face_found = False                               # set flag 0 for face
eyes_found = False                               # set flag 0 for eyes


if video.isOpened():                             # check if video is opened
    rval, frame = video.read()                   # return the value as  video frame
else:
    rval = False                                 # else return 0

# Paths to haarcascade_frontalface_alt.xml and haarcascade_eye.xml files which are available in OpenCV dist
faceCascade = cv2.CascadeClassifier("C:/Users/HP/Anaconda2/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier('C:/Users/HP/Anaconda2/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_eye.xml')

while rval:                               # infinite loop till the return value is true
    cv2.imshow(title, frame)              # Display an image and title in a window
    rval, frame = video.read()            # reads frames from a camera
    face_found = False                    # make face flag 0
    if len(faceCascade.detectMultiScale(frame))>0:    # check the length of frame in detection              
        faces = faceCascade.detectMultiScale(frame)   # Detects faces of different sizes in the input image

        for (x, y, w, h) in faces:                    # To draw a rectangle in a face(x and y coordinate, width and height)
            if w > 0:                                 # if width is greater than 0
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)   # draw a reactangle
                #print ("face found")
               
                if len(eye_cascade.detectMultiScale(frame))>0:     # check the lenth of eye frame
                    eyes = eye_cascade.detectMultiScale(frame)     # Detects eyes of different sizes in the input image
                    for (ex, ey, ew, eh) in eyes:                  # To draw a rectangle in eyes
                        if ew > 0:                                 # if the eye width is greater then 0
                            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)    #make frame
                            #print("eyes found")
                            if eyes_found == False:               # check if eye flag is 0
                                %run -i version2.ipynb            # run the programe to send on to the saini.txt
                                eyes_found = True                 # update the eye flag to 1
                else:                                            
                    #print("eyes not found")
                    if eyes_found == True:                       # if eye is not found, check if eye flag is 1
                        %run -i version3.ipynb                   # run the programe to send off to the saini.txt
                        eyes_found = False                       # update the eye flag to 0
                       
               
    else:                                                        # if face is not detected
        #print("face not found")
        if face_found == False:                                  # if face flag is 0            
            %run -i version3.ipynb                               # run the programe to send off to the saini.txt
            face_found = True                                    # update face flag to 1
            eyes_found = False                                   # also update the eye flag to 0 (cause if it was detected and it is still 1)
           
           

               
    key = cv2.waitKey(20)                                        # Wait for Esc key to stop
    if key == 27:
        break

video.release()                                                 # Close the window
cv2.destroyWindow(title)                                        # De-allocate any associated memory usage 

