import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattedance-default-rtdb.firebaseio.com/",
    'storageBucket':"faceattedance.appspot.com"
})


#importing the image into list

folderpath="Image"
path=os.listdir(folderpath)
imglist=[]
studentid=[]
for path in path:
    imglist.append(cv2.imread(os.path.join(folderpath, path)))
    studentid.append(os.path.splitext(path)[0])

    filename=f'{folderpath}/{path}'
    bucket = storage.bucket()
    blob=bucket.blob(filename)
    blob.upload_from_filename(filename)

#print(len(imglist)
#print(studentid)

def findencoding(imglist):
    encodelist=[]
    for img in imglist:
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
print("encoding started ...")
encodelistknown=findencoding(imglist)
encodelistknownwithid=[encodelistknown,studentid]
print("encoding completed ...")

file=open("EncodeFile.p","wb")
pickle.dump(encodelistknownwithid,file)
file.close()
print("file Saved")
