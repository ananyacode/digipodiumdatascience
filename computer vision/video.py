import cv2
VIDEO_PATH=r"/Users/ananyashukla/Downloads/video (2160p) (1).mp4"
vid = cv2.VideoCapture(VIDEO_PATH)

while True:
    status,img = vid.read()
    if not status:
        print('video is not available')
        break
    img= cv2.resize(img,None,fx=.25,fy=.25)
    cv2.imshow('Video',img)
    key = cv2.waitKey(15)
    if key == 27:
        break
cv2.destroyAllWindows()
vid.release()