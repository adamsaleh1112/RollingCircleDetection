# IMPORT NUMPY AND CV2
import numpy  # importing numpy, an array library that allows video data to be stored in arrays
import cv2  # importing opencv-python, an image processing library that allows functions such as blur, cropping, etc.

# VIDEO = CAN.MP4
vc = cv2.VideoCapture("RollingCan.mp4")  # loads video

# WHILE TRUE
while True:

    # FRAME = VIDEO READ
    ret, frame = vc.read() # setting frame and ret = vc.read() to allow for individual image processing

    # BLACK AND WHITE = IMAGE, BGR2GRAY
    bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts it to grayscale

    # DETECTED = BW.HOUGHCIRCLES
    detected = cv2.HoughCircles(bw, cv2.HOUGH_GRADIENT, 1.2, 100, minRadius=50, maxRadius=1000)  # detects circles

    # IF CIRCLES DETECTED IS NOT 0
    if detected is not None:  # makes sure that it detected at least one

        # CIRCLES = NUMPY DETECTED
        circles = numpy.uint16(numpy.around(detected))  # converts circles to x, y, and radius parameters

        # FOR PARAMETER IN CIRCLES
        for parameter in circles[0, :]:  # iterating through all circles' detected parameters

            # X = PARAM 0, Y = PARAM 1, R = PARAM 2
            x, y, r = parameter[0], parameter[1], parameter[2]  # setting x, y, and radius to the respective parameters

            # DRAW CIRCLE RADIUS = R
            cv2.circle(frame, (x, y), r, (150, 255, 0), 7)  # args: image, coordinates, radius, color, stroke

            # DRAW CIRCLE RADIUS = 1
            cv2.circle(frame, (x, y), 1, (0, 0, 255), 10)  # drawing a circle with a radius of 1 (dot) at same coordinates

            # IMSHOW WINDOW
            cv2.imshow("circle", frame)  # creating window called circle that displays output image
            cv2.waitKey(1)

vc.release()
cv2.destroyWindow("circle")