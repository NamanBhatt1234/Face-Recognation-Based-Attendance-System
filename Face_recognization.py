#from tkinter import *
#from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

#____for date and time
from time import strftime
from datetime import datetime

import cv2
import os
import numpy as np
from train import train_dataset 

class Face_Recognition:
    #______________to mark attendance in database after recognization______________________________
    def mark_attendance(i,r,n,d):
        with open("studentdata.csv","r+",newline="\n") as f:
            my_file_data=f.readlines()
            name_list=[]
            for line in my_file_data:
                entry=line.split((","))
                name_list.append(entry[0])
            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                 
                
                

    
    #__________________to recognize face ______________________________
    def recognize_face():
        def draw_boundary(img,classifier,scaleFactor,miniNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features_classifier=classifier.detectMultiScale(gray_image,scaleFactor,miniNeighbors)  
            
            coord=[]

            for (x,y,w,h) in features_classifier:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                con=mysql.connector.connect(host="localhost",user="root",password="",database="student_data")
                #The MySQLCursor class instantiates objects that can execute operations such as SQL statements. Cursor objects interact with the MySQL server using a MySQLConnection object.
                database_access=con.cursor()

                database_access.execute("select `Name` from `students` where `student_id`="+str(id))
                n=database_access.fetchone()
                n="+".join(n)
                

                database_access.execute("select `Roll` from `students` where `student_id`="+str(id))
                r=database_access.fetchone()
                r="+".join(r)

                database_access.execute("select `Dep` from `students` where `student_id`="+str(id))
                d=database_access.fetchone()
                d="+".join(d)

                database_access.execute("select `student_id` from `students` where `student_id`="+str(id))
                i=database_access.fetchone()
                i="+".join(i)

                 
                
                if confidence>75:
                    cv2.putText(img,f"Id:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    Face_Recognition.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognization",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
    
            
