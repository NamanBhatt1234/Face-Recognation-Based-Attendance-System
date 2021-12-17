from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Student Management System")

        #_____________variables to keep student data______________
        #these variables keep data through Widget object call where they are value of argument textvariable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()

        #___radio button data variables________________
        #these variables keep data through Widget object call where they are value of argument textvariable   
        self.var_radiobtn1=StringVar()
        #self.var_radiobtn2=StringVar()

        
        #main window Description
        bckLabel_l=Label(self.root,text="Student Management System",font=("times new roman",35,"bold"),fg='black')
        bckLabel_l.pack()

        #Frame Window
        frame1=Frame(self.root,bd=4,bg='lightblue')
        frame1.place(x=8,y=65,height=680,width=1500)

        #left label frame
        l_frame1=LabelFrame(frame1,bg='red',text='Student Details')
        l_frame1.place(x=10,y=67,width=735,height=580)

        #current course frame
        c_frame1=LabelFrame(l_frame1,bg='green',text='Current course')
        c_frame1.place(x=10,y=50,width=710,height=150)
            #department selection and label 
        department_l=Label(c_frame1,text="Department")
        department_l.grid(row=0,column=0,padx=10)

        comboBox1=ttk.Combobox(c_frame1,textvariable=self.var_dep,state='readonly')
        comboBox1['values']=('Select Department','CSE','CIVIL','MECHANICAL')
        comboBox1.current(0)
        comboBox1.grid(row=0,column=1,padx=2,pady=10)
            #course selection and label
        course_l=Label(c_frame1,text="Course")
        course_l.grid(row=0,column=2,padx=10)

        comboBox2=ttk.Combobox(c_frame1,textvariable=self.var_course,state='readonly')
        comboBox2['values']=('Select Course','Btech','Bsc','Bcom')
        comboBox2.current(0)
        comboBox2.grid(row=0,column=3,padx=2,pady=10)
            #year selection and label
        year_l=Label(c_frame1,text="Year")
        year_l.grid(row=1,column=0,padx=10)

        comboBox3=ttk.Combobox(c_frame1,textvariable=self.var_year,state='readonly')
        comboBox3['values']=('Select Year','2019-2023','2020-2024','2021-2025')
        comboBox3.current(0)
        comboBox3.grid(row=1,column=1,padx=2,pady=10)
            #semester selection and label
        semester_l=Label(c_frame1,text="Semester")
        semester_l.grid(row=1,column=2,padx=10)

        comboBox4=ttk.Combobox(c_frame1,textvariable=self.var_semester,state='readonly')
        comboBox4['values']=('Current Semester','1','2','3','4','5','6','7','8')
        comboBox4.current(0)
        comboBox4.grid(row=1,column=3,padx=2,pady=10)

        #Class Student Data 
        c_student_frame1=LabelFrame(l_frame1,bg='green',text='Class Student Details')
        c_student_frame1.place(x=10,y=250,width=710,height=300)
            #studentid input and label 
        studentId_l=Label(c_student_frame1,text="StudentId")
        studentId_l.grid(row=0,column=0,padx=10)

        entryBox1=ttk.Entry(c_student_frame1,textvariable=self.var_id)
        entryBox1.grid(row=0,column=1,padx=2,pady=10)
            #student Name input and label 
        studentName_l=Label(c_student_frame1,text="Student Name")
        studentName_l.grid(row=0,column=2,padx=10)

        entryBox2=ttk.Entry(c_student_frame1,textvariable=self.var_name)
        entryBox2.grid(row=0,column=3,padx=2,pady=10)
            #class Division input and label 
        classDivision_l=Label(c_student_frame1,text="Class Division")
        classDivision_l.grid(row=1,column=0,padx=10)

        entryBox3=ttk.Entry(c_student_frame1,textvariable=self.var_div)
        entryBox3.grid(row=1,column=1,padx=2,pady=10)
            #class RollNo input and label 
        rollNo_l=Label(c_student_frame1,text="RollNo")
        rollNo_l.grid(row=1,column=2,padx=10)

        entryBox4=ttk.Entry(c_student_frame1,textvariable=self.var_roll)
        entryBox4.grid(row=1,column=3,padx=2,pady=10)
            #Gender input and label 
        gender_l=Label(c_student_frame1,text="Gender")
        gender_l.grid(row=2,column=0,padx=10)

        comboBox5=ttk.Combobox(c_student_frame1,textvariable=self.var_gender,state='readonly')
        comboBox5['values']=('Select','Male','Female')
        comboBox5.current(0)
        comboBox5.grid(row=2,column=1,padx=2,pady=10)
            #Date Of Birth input and label 
        dob_l=Label(c_student_frame1,text="DOB:")
        dob_l.grid(row=2,column=2,padx=10)

        entryBox6=ttk.Entry(c_student_frame1,textvariable=self.var_dob)
        entryBox6.grid(row=2,column=3,padx=2,pady=10)
            #Email input and label 
        email_l=Label(c_student_frame1,text="Email")
        email_l.grid(row=3,column=0,padx=10)

        entryBox7=ttk.Entry(c_student_frame1,textvariable=self.var_email)
        entryBox7.grid(row=3,column=1,padx=2,pady=10)
            #PhoneNo input and label 
        email_l=Label(c_student_frame1,text="PhoneNo:")
        email_l.grid(row=3,column=2,padx=10)

        entryBox8=ttk.Entry(c_student_frame1,textvariable=self.var_phone)
        entryBox8.grid(row=3,column=3,padx=2,pady=10)
            #radio buttons
        radiobtn1=ttk.Radiobutton(c_student_frame1,variable=self.var_radiobtn1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0)     

        radiobtn2=ttk.Radiobutton(c_student_frame1,variable=self.var_radiobtn1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4,column=1)
            #buttonsFrame
        btn_frame1=Frame(c_student_frame1,bd=2,bg='lightyellow')
        btn_frame1.place(x=10,y=190,width=690,height=80)

        save_btn=Button(btn_frame1,command=self.add_info,text="Save",width=22)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,command=self.update_database,text="Update",width=22)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame1,command=self.delete_database,text="Delete",width=22)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame1,command=self.reset_database,text="Reset",width=25)
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame1,command=self.generate_imgDataset,text="Take Photo Sample",width=20)
        take_photo_btn.grid(row=1,column=0)
        
        #right label frame
        r_frame2=LabelFrame(frame1,bg='red',text='Student Details')
        r_frame2.place(x=750,y=67,width=735,height=580)

        #____________searching Frame____________________
        search_frame2=LabelFrame(r_frame2,bg='green',text='Search System')
        search_frame2.place(x=10,y=50,width=710,height=150)

        searchBy_r=Label(search_frame2,text="Search By")
        searchBy_r.grid(row=0,column=0,padx=10)

        #____________search________________________

        self.var_searchSystem=StringVar( )
        comboBox6=ttk.Combobox(search_frame2,textvariable=self.var_searchSystem,state='readonly')
        comboBox6['values']=('Select','Roll','student_id')
        comboBox6.current(0)
        comboBox6.grid(row=0,column=1,padx=2,pady=10)
        
        self.var_searchSystem1=StringVar()
        entryBox9=ttk.Entry(search_frame2,textvariable=self.var_searchSystem1)
        entryBox9.grid(row=0,column=2,padx=2,pady=10)

        search_btn=Button(search_frame2,command=self.search_database,text="Search",width=20)
        search_btn.grid(row=0,column=3)

        showAll_btn=Button(search_frame2,command=self.fetch_database, text="ShowAll",width=20)
        showAll_btn.grid(row=0,column=4)

        #_____________________Table Frame______________________________
        table_frame2=Frame(r_frame2,bd=2,bg='green')
        table_frame2.place(x=10,y=220,width=710,height=340)

        scroll_x=ttk.Scrollbar(table_frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame2,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame2,column=('dep','course','year','sem','id','name','div','roll','gender','dob','email','phone','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #_____________________to display Headings in Treeview_____________
        self.student_table.heading('dep',text="Department")
        self.student_table.heading('course',text="Course")
        self.student_table.heading('year',text="Year")
        self.student_table.heading('sem',text="Semester")
        self.student_table.heading('id',text="Student Id")
        self.student_table.heading('name',text="Student Name")
        self.student_table.heading('div',text="Class Division")
        self.student_table.heading('roll',text="RollNo")
        self.student_table.heading('gender',text="Gender")
        self.student_table.heading('dob',text="DOB")
        self.student_table.heading('email',text="Email")
        self.student_table.heading('phone',text="Phone No")
        self.student_table.heading('photo',text="Photo Sample")

        self.student_table["show"]="headings"

        #__________________set width of each column_________________
        self.student_table.column('dep',width=150)
        self.student_table.column('course',width=150)
        self.student_table.column('year',width=150)
        self.student_table.column('sem',width=150)
        self.student_table.column('id',width=150)
        self.student_table.column('name',width=150)
        self.student_table.column('div',width=150)
        self.student_table.column('roll',width=150)
        self.student_table.column('email',width=150)
        self.student_table.column('phone',width=150)
        self.student_table.column('dob',width=150)
        self.student_table.column('gender',width=150)
        self.student_table.column('photo',width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_database()

        #___________to enable or bind get_cursor to table
        self.student_table.bind("<ButtonRelease>",self.get_cursor_data)

        
    #_______________function to add data to local database_________________
    #will be called in save_btn     
    def add_info(self):
        if self.var_dep.get()=='' or self.var_name.get()=='' or self.var_id=='':
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="1234",database="student_data")
                #The MySQLCursor class instantiates objects that can execute operations such as SQL statements. Cursor objects interact with the MySQL server using a MySQLConnection object.
                database_access=con.cursor()
                database_access.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                            self.var_dep.get(),
                                            self.var_course.get(),
                                            self.var_year.get(),
                                            self.var_semester.get(),
                                            self.var_id.get(),
                                            self.var_name.get(),
                                            self.var_div.get(),
                                            self.var_roll.get(),
                                            self.var_gender.get(),
                                            self.var_dob.get(),
                                            self.var_email.get(),
                                            self.var_phone.get(),
                                            self.var_radiobtn1.get()
                                        )
                                       )
                con.commit()
                self.fetch_database()
                con.close()
                messagebox.showinfo("Success","New Student Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #______________function to fetch data from database_______________________________
    def fetch_database(self):
        con=mysql.connector.connect(host="localhost",user="root",password="1234",database="student_data")
        #The MySQLCursor class instantiates objects that can execute operations such as SQL statements. Cursor objects interact with the MySQL server using a MySQLConnection object.
        database_access=con.cursor()
        database_access.execute("select *from students")
        table_data=database_access.fetchall()
        if len(table_data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            #_______adding data in student_table___________________
            for i in table_data:
                self.student_table.insert("",END,values=i)
            con.commit()
        con.close()


    #_______________function to update database____________
    def update_database(self):
        if self.var_dep.get()=='' or self.var_name.get()=='' or self.var_id=='':
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure to update",parent=self.root)
                if update>0:
                    con=mysql.connector.connect(host="localhost",user="root",password="1234",database="student_data")
                    #The MySQLCursor class instantiates objects that can execute operations such as SQL statements. Cursor objects interact with the MySQL server using a MySQLConnection object.
                    database_access=con.cursor()
                    database_access.execute("update students set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,PhotoSample=%s where student_id=%s",
                                               (
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                self.var_name.get(),
                                                self.var_div.get(),
                                                self.var_roll.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_radiobtn1.get(),
                                                self.var_id.get()
                                               )
                                           )
                else:
                    if not update:
                        return
                con.commit()
                self.fetch_database()
                con.close()

                messagebox.showinfo("Success","Student Upadtion Successfull",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #_________________function to delete a student record from database________________________
    def delete_database(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","All Fields Required")
        else:
            try:
                delete=messagebox.askyesno("Update","Are you sure to update",parent=self.root)
                if delete>0:
                    con=mysql.connector.connect(host="localhost",user="root",password="1234",database="student_data")
                    #The MySQLCursor class instantiates objects that can execute operations such as SQL statements. Cursor objects interact with the MySQL server using a MySQLConnection object.
                    database_access=con.cursor()
                    database_access.execute("delete from students where student_id =%s",(self.var_id.get(),))

                else:
                    if not delete:
                        return
                con.commit()
                self.fetch_database()
                con.close() 

                messagebox.showinfo("Delete","Student Data Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
    #________________function to reset data in entry fields_______________________
    def reset_database(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Current Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_dob.set("")
        self.var_gender.set("Select")
        self.var_radiobtn1.set("")

    #______________search System_____________________________________________
    def search_database(self):
        if self.var_searchSystem.get()=="" or self.var_searchSystem1.get()=="":
            messagebox.showerror("Error","Please Select a Option")
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="1234",database="student_data")
                #The MySQLCursor class instantiates objects that can execute operations such as SQL statements. Cursor objects interact with the MySQL server using a MySQLConnection object.
                database_access=con.cursor()
                database_access.execute("select * from students where "+str(self.var_searchSystem.get())+" LIKE '%s"+str(self.var_searchSystem1.get())+"%'")
                table_data=database_access.fetchall()
                if len(table_data)!=0:
                    #check tjis for error
                    self.student_table.delete(self.student_table.get_children())
                    for i in table_data:
                        self.student_table.insert("",END,values=i)
                    con.commit()
                con.close()    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #___________function to get cursor data______________________
    def get_cursor_data(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content['values']
        self.var_dep.set(rows[0])
        self.var_course.set(rows[1])
        self.var_year.set(rows[2])
        self.var_semester.set(rows[3])
        self.var_name.set(rows[4])
        self.var_id.set(rows[5])
        self.var_div.set(rows[6])
        self.var_roll.set(rows[7])
        self.var_gender.set(rows[8])
        self.var_dob.set(rows[9])
        self.var_email.set(rows[10])
        self.var_phone.set(rows[11])            
    
    #_________________photo________________________________
    def generate_imgDataset(self):
        if self.var_dep.get()=='Select ' or self.var_name.get()=='' or self.var_id=='':
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            try:
                
                con=mysql.connector.connect(host="localhost",user="root",password="1234",database="student_data")
                #The MySQLCursor class instantiates objects that can execute operations such as SQL statements. Cursor objects interact with the MySQL server using a MySQLConnection object.
                database_access=con.cursor()
                database_access.execute("select *from `students`")
                res=database_access.fetchall()
                id=0
                #check here
                for x in res:
                    id+=1
                database_access.execute("update `students` set `Dep`=%s,`course`=%s,`Year`=%s,`Semester`=%s,`Name`=%s,`Division`=%s,`Roll`=%s,`Gender`=%s,`Dob`=%s,`Email`=%s,`Phone`=%s,`PhotoSample`=%s where `student_id`=%s",
                                               (
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                self.var_name.get(),
                                                self.var_div.get(),
                                                self.var_roll.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_radiobtn1.get(),
                                                self.var_id.get()==id+1
                                               )
                                           )                         
                con.commit()
                self.fetch_database()
                self.reset_database()
                con.close()

                #____load frontal face detection algo from open cv_________________

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                                
                def face_cropping(img):
                    #_________________converting in grayscale_________________
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # Minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropping=img[y:y+h,x:x+w]
                        return face_cropping

                cam_capture=cv2.VideoCapture(0)
                # argumnrts of VideoCapture() is 0 for weCAM ,path to open a specfic image
                img_id=0 #This determines number of samples to be taken
                while True:
                    ret,my_frame=cam_capture.read()
                    if face_cropping(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropping(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        #image file names
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cam_capture.release()  
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                
if __name__=='__main__':
    root=Tk()
    obj=student_window(root)     
    root.mainloop()
