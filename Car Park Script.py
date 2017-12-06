import tkinter
from tkinter import *
import csv
from time import sleep

val = 0
inti = 'nil'
aaa = 0
localreg = 'nil'

def sendreg():
    global localreg
    temp = regget.get()
    localreg = temp
    main()
    reg.Destroy()

reg = tkinter.Tk()
reg.title("Please enter your reg")
reg.geometry("350x100")

welcome = tkinter.Label(reg, text="Welcome to the Loughborough Car park!")
welcome.pack()

asd = tkinter.Label(reg, text="Please enter your Registration Number")
asd.pack()

regget = Entry(reg)
regget.pack()

regget.delete(0, END)
regget.insert(0, "Please enter reg.")

btn = tkinter.Button(reg, text="Enter",command = sendreg)
btn.pack()

def main():

    def getSpace():
        list = open("ParkingData.txt","r")
        line = list.readline()
        spacedisplay.configure(text=line)
        list.close()
     
    def getPph():
        list = open("ParkingData.txt","r")
        line = list.readline()
        line = list.readline()
        pphdisplay.configure(text=line)
        list.close()
    
    def getCoin():
        global val
        val = val + float(coinentry.get())
        currentvalue.configure(text=val)
    
    window = tkinter.Tk()
    window.title("Loughborough Car Park System")
    window.geometry("400x800")

    gaf = tkinter.Label(window, text="Welcome to Loughborough Car Park!")
    gaf.pack()

    spacer = tkinter.Label(window, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    spacer.pack()

    spaces = tkinter.Label(window, text="Free spaces:")
    spaces.pack()

    spacedisplay = tkinter.Label(window, text="nil")
    spacedisplay.pack()

    spacer2 = tkinter.Label(window, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    spacer2.pack()

    pph = tkinter.Label(window, text="Price per hour:")
    pph.pack()

    pphdisplay = tkinter.Label(window, text="nil")
    pphdisplay.pack()

    spacer3 = tkinter.Label(window, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    spacer3.pack()

    currentvalue = tkinter.Label(window, text="nil")
    currentvalue.pack()

    coinentry = Entry(window)
    coinentry.pack()

    coinentry.delete(0, END)
    coinentry.insert(0, "Please Enter currency")

    btn1 = tkinter.Button(window, text="Give Currency...", command=getCoin)
    btn1.pack()

    btn2 = tkinter.Button(window, text="Control Window Login", command=engineerLogin)
    btn2.pack()
    
    window.mainloop

    getSpace()
    getPph()

def engineer():

    global inti

    sleep(0.1)
    engineer = tkinter.Tk()
    engineer.title("Engineer GUI")
    engineer.geometry("600x300")

    welcome = tkinter.Label(engineer, text=("Welcome,",inti))
    welcome.pack()

    appendone = Entry(engineer)
    appendone.pack()

    appendone.delete(0, END)
    appendone.insert(0, "Please enter new per minuite rate")

    def appendPPM():
        aaaaaaaaaaa = float(appenddone.get())
        list = open("ParkingData.txt","a")
        list.write()
        list.write(aaaaaaaaaaa)


    btn1 = tkinter.Button(engineer,text="Update Value", command = appendPPM)
    btn1.pack()
    
    engineer.mainloop



def engineerLogin():
    def checkLogin():
        global inti
        
        user2 = user.get()
        passw2 = passw.get()
        
        with open("Admins.csv", newline='') as admins:
            temp = csv.reader(admins)
            for row in temp:                
                data = row
                if user2 == data[0]:
                    if passw2 == data[1]:
                        inti = (user2,passw2)
                        engineer()
                        login.destroy()
                        

    login = tkinter.Tk()
    login.title("Engineer Login")
    login.geometry("600x200")

    label1 = tkinter.Label(login, text="Please enter credentials, Operator.")
    label1.pack()
    
    user = Entry(login)
    user.pack()

    user.delete(0, END)
    user.insert(0, "Please Enter Username")

    passw = Entry(login)
    passw.pack()

    passw.delete(0, END)
    passw.insert(0, "Please Enter Password")

    btn1 = tkinter.Button(login, text="Login", command=checkLogin)
    btn1.pack()
    
    login.mainloop

