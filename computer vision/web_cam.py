import cv2 # library version 4

# CREATE A VIDEOCAPTURE OBJECT
CAM_IDX=0
cam=cv2.VideoCapture(CAM_IDX)
while cam.isOpened():
    status,img=cam.read() # read the frame/image
    if status:
        cv2.imshow('Webcam',img) # display the frame/image
        key=cv2.waitKey(10) 
        if key== 27:
            break
    else:
        print('Webcam is not available')
        break
# free up resources
cv2.destroyAllWindows()
cam.release()