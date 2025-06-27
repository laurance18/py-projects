from tkinter import *
from tkinter import messagebox

def modifyclockvar(h,m,s):
    #Formatting clockvar strings
    if type(h) == int and type(m) == int and type(s) == int:
        pass
    else: 
        h = h.get()
        m = m.get()
        s = s.get()
    
    if int(h)<10:
        h = f"0{h}"
    else:
        h = f"{h}"
    if int(m)<10:
        m = f"0{m}"
    else:
        m = f"{m}"
    if int(s)<10:
        s = f"0{s}"
    else:
        s = f"{s}"

    clock = f"{h}:{m}:{s}"
    clockvar.set(clock)

def addtime(h,m,s): #Getting total amount of seconds
    global finished #Prevent stop() from getting finished bool in a True state
    finished = False
    return int(h.get())*3600 + int(m.get())*60 + int(s.get())

def splittime(total): #Splitting seconds into hours, minutes and seconds
    h = total // 3600
    m = (total % 3600) // 60
    s = ((total % 3600) % 60)
    return h, m, s

def countdown(sec): #Countdown function for the timer 
    if finished: #Stop timer if stop button is hit
        sec = -1

    if sec >= 0:
        root.after(1000,countdown,sec-1)
        modifyclockvar(*splittime(sec))
        if sec == 0:
            messagebox.showinfo("TIME'S UP","Timer has run out.") 
             

def stop():
    modifyclockvar(0,0,0)
    global finished
    finished = True

def main():
    #Mainwindow
    global root
    root = Tk()
    root.title("Countdown Timer")
    root.geometry("250x220")

    #Setting up vars
    hourvar = StringVar()
    minutevar = StringVar()
    secondvar = StringVar()
    
    global clockvar
    clockvar = StringVar()
    clockvar.set("00:00:00")

    global finished #Stop button controller
    finished = False

    #Setting up labels
    hourLabel = Label(root,text="Hour").grid(row=0,column=0)
    minuteLabel = Label(root,text="Minute").grid(row=0,column=1)
    secondLabel = Label(root,text="Second").grid(row=0,column=2)
    clockLabel = Label(root,textvariable=clockvar,font=20).grid(row=2,column=5)

    #Setting up scales
    hour = Scale(root, variable=hourvar, from_= 0, to=24).grid(row=2,column=0)
    minute = Scale(root, variable=minutevar, from_= 0, to=60).grid(row=2,column=1)
    second = Scale(root, variable=secondvar, from_= 0, to=60).grid(row=2,column=2)

    #Setting up buttons
    B1 = Button(root,text="SET TIME",command=lambda : modifyclockvar(hourvar,minutevar,secondvar))
    B1.grid(row=3,column=0,columnspan = 3) 

    B2 = Button(root,text="START",command=lambda : countdown(addtime(hourvar,minutevar,secondvar)))
    B2.grid(row=4,column=0,columnspan = 3) 

    B3 = Button(root,text="STOP",command=lambda : stop())
    B3.grid(row=5,column=0,columnspan = 3) 

    root.mainloop()

if __name__ == "__main__":
    main()
