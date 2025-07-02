print("This is a demo To-Do List file.")
from tkinter import *
from PIL import Image,ImageTk
root = Tk()
#FRONTEND
root.title("Array based To-do list")
root.iconbitmap(r"C:\Users\Shreyankar Kanu\Downloads\8528d512787d83e744ba01e0e8dc2fcd.ico")
root.minsize(500,600)
root.config(bg="pink")
# Heading
text_label = Label(root, text='INBOX', fg='black', bg='pink',  justify='center')
text_label.pack(pady=(100,10))
text_label.config(font=('Helvetica', 70))
# Image
inbox_image = Image.open(r"C:\Users\Shreyankar Kanu\Downloads\inbox-email-icon-white_116137-5901-removebg-preview.png")
resize_inbox_image = inbox_image.resize((150,150))
inbox_image= ImageTk.PhotoImage(resize_inbox_image)
inbox_image_label = Label(root, image= inbox_image,  justify='center')
inbox_image_label.config(bg='pink')
inbox_image_label.pack(pady=(0,10))
# Subtext
inbox_text = Label(text='Jot now, plan later Inbox lets you offload tasks instantly — clarity now, structure later' , fg='black',bg='pink' ,justify='center')
inbox_text.config(font=('Helvetica', 10))
inbox_text.pack(pady=(0,0))
# Task input
input_task_add = Entry(root,width=40)
input_task_add.pack(pady=10)

# Frame to hold tasks dynamically
task_frame = Frame(root, bg='pink')
task_frame.pack(pady=10)

button_frame = Frame(root,bg='pink')
button_frame.pack(pady=20)


###################BACKEND############

to_do_list = []
status_list = []

def add_task_from_input(task_input):
    task_input = task_input.strip()
    if task_input == "":
        return
    
    task_list = task_input.split(",")
    for task in task_list:
        task = task.strip()
        if task != "":
            to_do_list.append(task)
            status_list.append(False)

def complete_and_delete_task(index):
    if 0 <= index <= len(to_do_list):
        to_do_list.pop(index)
        status_list.pop(index)
        refresh_task()


def refresh_task():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for i in range (len(to_do_list)):
        task = to_do_list[i]
        var = IntVar()

        def on_check(index=i , v=var):
            if v.get() == 1:
                complete_and_delete_task(index)

        check_box = Checkbutton(task_frame,text=task,variable=var,command=on_check,bg='pink',font=("verdana",12))
        check_box.pack(anchor='w',padx=20,pady=2)

def handel_button():
    task_test=input_task_add.get()
    add_task_from_input(task_test)
    input_task_add.delete(0,END )
    refresh_task()

add_task = Button(root, text='Add task', bg='black', fg='pink', width=20,height=2 ,command=handel_button) 
add_task.pack(padx=10)
add_task.config(font=('verdana',10))

view_task = Button(root,text='View Tasks',bg='black',fg='pink', width=20,height=2, font=('Verdana',10),command=refresh_task)
view_task.pack(padx=10)
root.mainloop()