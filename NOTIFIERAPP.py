from tkinter import *
from plyer import notification
from tkinter import messagebox
import time
from PIL import Image, ImageTk


t = Tk()
t.title('Notifier')
image = Image.open("bg.png")
t.geometry("503x300")
tkimage = ImageTk.PhotoImage(image)


def get_details():
    get_title = title.get()
    get_message = message.get()
    get_time = time1.get()
    get_time1 = time2.get()

    if get_title == "" or get_message == "" or get_time == "":
        messagebox.showerror("Alert", "All Fields Are Required To Fill")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        int_time1 = int(float(get_time1))
        min_to_hours = int_time1 * 60 * 60
        messagebox.showinfo("Confirmation", "Your Notification Is Set")
        t.destroy()
        time.sleep(min_to_sec)
        time.sleep(min_to_hours)

        notification.notify(title=get_title,
                            message=get_message,
                            app_name="Notifier",
                            app_icon="logo.ico",
                            toast=True,
                            timeout=60)


image_label = Label(t, image=tkimage).grid()

title_label = Label(t, text="Title to Notify", font=("poppins", 10))
title_label.place(x=12, y=70)

title = Entry(t, width="25", font=("poppins", 18))
title.place(x=123, y=70)

message_label = Label(t, text="Display Message", font=("poppins", 10))
message_label.place(x=12, y=120)

message = Entry(t, width="25", font=("poppins", 18))
message.place(x=123, height=35, y=120)

time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

time1 = Entry(t, width="5", font=("poppins", 18))
time1.place(x=230, y=175)

time_min_label = Label(t, text="Min", font=("poppins", 10))
time_min_label.place(x=303, y=180)

time2 = Entry(t, width="5", font=("poppins", 18))
time2.place(x=123, y=175)

time_hour_label = Label(t, text="Hour", font=("poppins", 10))
time_hour_label.place(x=195, y=180)

button = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised", command=get_details)
button.place(x=170, y=230)
t.resizable(0, 0)
t.mainloop()
