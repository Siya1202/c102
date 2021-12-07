import cv2
import time
import random
import dropbox

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    #initializing the library in above line , 0 here indicates the camera of our system .

    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name='img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time=time.time
        #imwrite function is used to save the image .
        result=False

    return img_name
    print('snapshot taken')

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='iy_1ZtoovuwAAAAAAAAAASwNm7rsjt8E8b1x65ggfyWoXHq8faTyvOspYr2gC3OT'
    file=img_name
    file_from=file
    file_to='/snapshots/'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        if((time.time()-start_time)>=15):
            name=take_snapshot()
            upload_file(name)

main()
            
