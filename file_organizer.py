import shutil
import os
from datetime import datetime,timedelta
import time
from tkinter import *
from tkinter import filedialog
import pathlib

root = Tk()

root.geometry('500x300')

entry_1 = Entry(root,width=20)

entry_1.grid(row=0,column=1)

entry_2 = Entry(root, width=20)

entry_2.grid(row=1,column=1,pady=5)

def organizer_gui():

    

    button_1 = Button(root, text="Browse..", command=file_path_A)

    button_1.grid(row=0,column=0)

    button_2 = Button(root, text="Browse..", command=file_path_B)

    button_2.grid(row=1,column=0)

    start_button = Button(root, text="Start", command= daily_files)

    start_button.grid(row=2,column=0)

    

def file_path_A():
    global file_path1

    file_path1 = filedialog.askdirectory() + '/'

    entry_1.insert(0,file_path1)


def file_path_B():
    global file_path2
    
    file_path2 = filedialog.askdirectory() + '/'

    entry_2.insert(0,file_path2)


def daily_files():

    source = file_path1

    destination = file_path2
    

    files = os.listdir(source)

    now = datetime.now()


    time_3 = now+timedelta(hours=24)

    time_4 = now-timedelta(hours=24)



    for file in files:
        if file.endswith(".txt"):
            time_1 = os.path.getmtime(source+file)
            time_2 = datetime.fromtimestamp(time_1).strftime('%Y-%m-%d %H:%M:%S')
            date_time_final = datetime.strptime(time_2, '%Y-%m-%d %H:%M:%S')
            print(date_time_final)
            print(time_2)
            if time_4 <= date_time_final and date_time_final <= time_3:
                shutil.move(source+file,destination)

    


if __name__ == '__main__':
    organizer_gui()
    
    
    
        
       

        





