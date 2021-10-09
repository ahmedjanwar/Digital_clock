from time import strftime
from tkinter import Label,Tk, font
#the window
clock = Tk()
clock.title("Digital_Clock")
clock.geometry("200x100")
clock.configure(bg ="black")
clock.resizable(False,False)
#the label
clock_label=Label(clock,bg="black",fg="white", font= ("Times", 30, 'bold'),relief='flat')
clock_label.place(x =20, y = 20)
#function
def updating_Label():
    current_time =strftime('%H: %M: %S')
    clock_label.configure(text =current_time)
    clock_label.after(80, updating_Label)
#calling the function
updating_Label()
clock.mainloop()
