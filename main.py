#https://github.com/Ofaydin18 
import cv2
import numpy as np
import pyautogui as pgi
videoname = input("Video Name: ")
if videoname == "":
    videoname = input("Video name required: ")
    #this ''if block'' not working very well i ll fix this.
    
        
cc = cv2.VideoWriter_fourcc(*"XVID")
frameTime = 20
screen = pgi.size()
output = cv2.VideoWriter(videoname+".avi",cc,20.0,screen)

while True:
    img = pgi.screenshot()
    frames = np.array(img)
    frames = cv2.cvtColor(frames,cv2.COLOR_BGR2RGB)
    output.write(frames)
    cv2.imshow("Recording",frames)
    if cv2.waitKey(frameTime) ==ord("q"):
        break

cv2.destroyAllWindows()
output.release()