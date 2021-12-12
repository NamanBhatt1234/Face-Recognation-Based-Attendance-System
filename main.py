from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import student_window

#importing train file
from train import train_dataset

#importing face recognition file
from Face_recognization import Face_Recognition

#importing attendance file
from attendance import attendance_window

class main_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        #main window Description
        bckLabel_l=Label(self.root,text="Face Regonition System",font=("times new roman",35,"bold"),fg='black')
        bckLabel_l.pack()

        #button1
        b1=Button(self.root,text='Student Corner',command=self.student_corner,bg='white') 
        b1.place(x=200,y=100,height=220,width=200) 

        #button2
        b2=Button(self.root,command=Face_Recognition.recognize_face,text='Detect Face',bg='white') 
        b2.place(x=600,y=100,height=220,width=200)

        #button3
        b3=Button(self.root,text='Show Attendance',command=self.attendance_corner,bg='white') 
        b3.place(x=1000,y=100,height=220,width=200)

        #button4
        b4=Button(self.root,text='Train Data',command=train_dataset.train_classifier,bg='white') 
        b4.place(x=600,y=400,height=220,width=200)
        
    #________________buttons events_________________
    def student_corner(self):
        self.new_window=Toplevel(self.root)
        self.app=student_window(self.new_window)

    def attendance_corner(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance_window(self.new_window)
if __name__=='__main__':
    root=Tk()
    obj=main_window(root)
    root.mainloop()
