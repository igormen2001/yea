import cv2
import numpy as np 
import os

main_dir = r'D:\\'
people = ['igor', 'karina']

faces = []
indexes = []

haar_cascade = cv2.CascadeClassifier('C:\\Users\\oksana\\Desktop\\face.xml')
      
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)



for person in people:
    path = os.path.join(main_dir, person)
    photos = os.listdir(path)
    person_index = people.index(person)
    for photo in photos:
       
        photo_path = os.path.join(path, photo)
        img = cv2.imread(photo_path)
        img = ResizeWithAspectRatio(img, height=900)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detect_face = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
        for (x,y,w,h) in detect_face:
            only_face = gray[y:y+h,x:x+w]
            faces.append(only_face)
            indexes.append(person_index)


faces = np.array(faces, dtype='object')
indexes = np.array(indexes)
path_faces = os.path.join(main_dir,'faces.npy')
path_indexes = os.path.join(main_dir,'indexes.npy')

np.save(r'C:\\Users\\oksana\\Desktop\\faces.npy', faces)
np.save(r'C:\\Users\\oksana\\Desktop\\indexes.npy', indexes)

print('training done')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, indexes)
face_recognizer.save(r'C:\\Users\\oksana\\Desktop\\face_model.yml')


########################test file



import numpy as np 
import cv2
import os


def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)



haar_cascade = cv2.CascadeClassifier('C:\\Users\\oksana\\Desktop\\face.xml')
people = ['igor', 'karina']

faces = np.load(r'C:\\Users\\oksana\\Desktop\\faces.npy')
indexes = np.load(r'C:\\Users\\oksana\\Desktop\\indexes.npy')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\\Users\\oksana\\Desktop\\face_model.yml')


capture = cv2.VideoCapture(0)
	
while True:
	success, img = capture.read()
	img = ResizeWithAspectRatio(img, height=200)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	detect_face = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
	for (x,y,w,h) in detect_face:
	    only_face = gray[y:y+h,x:x+w]
	    index, accuracy = face_recognizer.predict(only_face)
	    # print(f'predicted persons is {people[index]}, and accuracy is {accuracy}')
	    img = cv2.rectangle(img,(x,y),(x+w, y+h),(255,255,0),3)
	    cv2.putText(img, f'{people[index]}', (x, y+h), cv2.FONT_HERSHEY_COMPLEX, 3, (0,255,0), 3)
	cv2.imshow('img', img)
	cv2.waitKey(1)



