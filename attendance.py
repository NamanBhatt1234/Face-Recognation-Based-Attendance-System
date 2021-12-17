from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

#import required to get data from.csv file
import os
import csv
from tkinter import filedialog

#list object to store data from csv file
data_csv=[]

class attendance_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Student Management System")

        #__________text variables to get data from entry fields__________
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #main window Description
        bckLabel_l=Label(self.root,text="Attendance Management System",font=("times new roman",35,"bold"),fg='black')
        bckLabel_l.pack()

        #Frame Window
        frame1=Frame(self.root,bd=4,bg='lightblue')
        frame1.place(x=8,y=65,height=680,width=1500)

        #left label frame
        l_frame1=LabelFrame(frame1,bg='red',text='Student Attendance Details')
        l_frame1.place(x=10,y=67,width=735,height=580)

        inside_l_frame1=Frame(l_frame1,bd=4,bg='green')
        inside_l_frame1.place(x=10,y=50,width=710,height=300)

        #attendance id input and label 
        attendanceId_l=Label(inside_l_frame1,text="AttendanceId")
        attendanceId_l.grid(row=0,column=0,padx=10)

        entryBox1=ttk.Entry(inside_l_frame1,textvariable=self.var_atten_id)
        entryBox1.grid(row=0,column=1,padx=2,pady=10)

        #student Name input and label 
        attendanceName_l=Label(inside_l_frame1,text="Student Name")
        attendanceName_l.grid(row=0,column=2,padx=10)

        entryBox2=ttk.Entry(inside_l_frame1,textvariable=self.var_atten_name)
        entryBox2.grid(row=0,column=3,padx=2,pady=10)

        #Date input and label 
        attendanceDate_l=Label(inside_l_frame1,text="Date")
        attendanceDate_l.grid(row=1,column=0,padx=10)

        entryBox3=ttk.Entry(inside_l_frame1,textvariable=self.var_atten_date)
        entryBox3.grid(row=1,column=1,padx=2,pady=10)

        #department selection and label 
        attendanceDepartment_l=Label(inside_l_frame1,text="Department")
        attendanceDepartment_l.grid(row=1,column=2,padx=10)
           
        entryBox4=ttk.Entry(inside_l_frame1,textvariable=self.var_atten_dep)
        entryBox4.grid(row=1,column=3,padx=2,pady=10)

        #Time selection and label 
        attendanceTime_l=Label(inside_l_frame1,text="Time")
        attendanceTime_l.grid(row=2,column=0,padx=10)
           
        entryBox5=ttk.Entry(inside_l_frame1,textvariable=self.var_atten_time)
        entryBox5.grid(row=2,column=1,padx=2,pady=10)

        #Attendance selection and label 
        attendance_l=Label(inside_l_frame1,text="Attendance")
        attendance_l.grid(row=2,column=2,padx=10)

        comboBox1=ttk.Combobox(inside_l_frame1,textvariable=self.var_atten_attendance,state='readonly')
        comboBox1['values']=('Status','Present','Absent')
        comboBox1.current(0)
        comboBox1.grid(row=2,column=3,padx=2,pady=10)

        #buttonsFrame
        btn_frame1=Frame(inside_l_frame1,bd=2,bg='lightyellow')
        btn_frame1.place(x=10,y=190,width=690,height=80)

        Icsv_btn=Button(btn_frame1,text="Import Csv",command=self.import_Csv,width=22)
        Icsv_btn.grid(row=0,column=0)

        Ecsv_btn=Button(btn_frame1,text="Export Csv",command=self.export_csv,width=22)
        Ecsv_btn.grid(row=0,column=1)

        Reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=25)
        Reset_btn.grid(row=0,column=2)

        #right label frame
        r_frame2=LabelFrame(frame1,bg='red',text='Attendance Details')
        r_frame2.place(x=750,y=67,width=735,height=580)

        #_____________________Table Frame______________________________
        table_frame2=Frame(r_frame2,bd=2,bg='green')
        table_frame2.place(x=10,y=220,width=710,height=340)

        #______________scroll bar______________________________________
        scroll_x=ttk.Scrollbar(table_frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame2,orient=VERTICAL)

        self.attendance_report_table=ttk.Treeview(table_frame2,column=('id','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendance_report_table.xview)
        scroll_y.config(command=self.attendance_report_table.yview)

        #_____________________to display Headings in Treeview_____________
        
        self.attendance_report_table.heading('id',text="Student Id")
        self.attendance_report_table.heading('name',text="Student Name")
        self.attendance_report_table.heading('department',text="Department")
        self.attendance_report_table.heading('time',text="Time")
        self.attendance_report_table.heading('date',text="Date")
        self.attendance_report_table.heading('attendance',text="Attendance")

        self.attendance_report_table["show"]="headings"

        #__________________set width of each column_________________
        self.attendance_report_table.column('id',width=150)
        self.attendance_report_table.column('name',width=150)
        self.attendance_report_table.column('department',width=150)
        self.attendance_report_table.column('time',width=150)
        self.attendance_report_table.column('date',width=150)
        self.attendance_report_table.column('attendance',width=150)

        self.attendance_report_table.pack(fill=BOTH,expand=1)

        #___________to enable or bind get_cursor to table
        self.attendance_report_table.bind("<ButtonRelease>",self.get_cursor_data)

    #_________________fetching data from database______________________
    def fetch_attendance(self,rows):
        self.attendance_report_table.delete(*self.attendance_report_table.get_children())
        for i in rows:
            self.attendance_report_table.insert("",END,values=i)
            
    #_________________importing Data From Csv File______________________________
    def import_Csv(self):
            global data_csv
            data_csv.clear()
            file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(file_name) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    data_csv.append(i)
                self.fetch_attendance(data_csv)
    #_______________exporting Data To Csv File_____________________________
    def export_csv(self):
        try:
            if len(data_csv)<1:
                messagebox.showerror("No Data","No Record Found to Export",parent=self.root)
                return False
            file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in data_csv:
                    exp_writerow(i)
                messagebox.showinfo("Data Export","Attendance Saved In"+os.path.basename(file_name))
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #___________function to get cursor data______________________
    def get_cursor_data(self,event=""):
        cursor_row=self.attendance_report_table.focus()
        content=self.attendance_report_table.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])
        
    #__________________Reset Data_______________________________________
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        

if __name__=='__main__':
    root=Tk()
    obj=attendance_window(root)     
    root.mainloop()
        
