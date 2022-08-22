from operator import truediv
import cv2

def take_snapshot():
    videoCaptureObject=cv2.videoCapture(0)
    result=True
    while(result):
        ret, frame=videoCaptureObject.read()
        print(ret)
        cv2.imwrite("NewPicture1.jpg", frame)
        result=False

    videoCaptureObject.realese()
    cv2.destroyAllWindows()

take_snapshot()