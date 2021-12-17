#from tkinter import *
#from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector
import cv2
import os
import numpy as np

class train_dataset:
    def train_classifier():
        #___________________TO access data of data directory_____________
        dataset_dir=("Data")
        #_________________list containg data from directory________________
        path=[os.path.join(dataset_dir,file) for file in os.listdir(dataset_dir)]
 
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grayScale Conversion
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


        #C:\USER Naman\Face Regonization System\Data\user.1.1.jpg
        #-----------------------0--------------------______1_____
        #                                            --0--1-2----
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids) #numpy increses the efficiency of project by 88%

        #_____________Train the classifier and save data_______________
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        #________after training,data is stored in this file_____________
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets complete")
        
         
