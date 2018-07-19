#Cok duzgun calisan bir algoritma degil.Gelistirilecek.
import cv2
import imageio

#cascade yuklemesi yaptik. parametre olarak xml dosyalari verdik.
face_cascade=cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade-eye.xml')

def detect(frame):
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #resmi siyah beyaza cevirdik
    faces=face_cascade.detectMultiScale(gray, 1.3, 5) #resimde yuz arama
    for(x, y, w, h) in faces: #buldugumuz yuzun etrafinda dikdortgen olusturma
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        gray_face=gray[y:y+h, x:x+w]   
        color_face=frame[y:y+h, x:x+w]
        eyes=eye_cascade.detectMultiScale(gray_face, 1.1, 3) #resimde goz arama
        for(ex,ey,ew,eh) in eyes: #buldugumuz gozun etrafina dikdortgen olusturma
            cv2.rectangle(color_face, (ex,ey), (ex+ew, ey+eh),(0,255,0), 2)

    return frame

reader=imageio.get_reader('1.mp4')
fps=reader.get_meta_data()['fps'] #saniyedeki resim karesine fps denir=video
writer=imageio.get_writer('output.mp4',fps=fps)
for i, frame in enumerate(reader):
    frame=detect(frame)
    writer.append_data(frame)
    print(i)
    

writer.close()
        
