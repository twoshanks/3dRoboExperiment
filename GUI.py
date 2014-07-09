from Tkinter import *
import tkMessageBox
import Tkinter

#orange - #d9892e
#black - #231f20
top = Tkinter.Tk()
top.configure(background = "#231f20" )

def LaunchSimCallBack():
   tkMessageBox.showinfo( "Running Simulation", "This will launch the simulation")

launch = Tkinter.Button(top, text ="Run Simulation", command = LaunchSimCallBack, bg="#d9892e",fg= "#231f20",
                activebackground = "#ffffff",relief = FLAT, bd =2)
launch.config(highlightthickness=0)
launch.pack()
launch.place(bordermode=OUTSIDE, height=100, width=100,relx = 0.2, rely=0.6)


def SimOptionsCallBack():
   tkMessageBox.showinfo( "Simulation Options", "This will launch options for sim")

SimOptions = Tkinter.Button(top, text ="Run Simulation", command = SimOptionsCallBack, bg="#d9892e",fg= "#231f20",
                activebackground = "#ffffff",relief = FLAT, bd =2)
SimOptions.config(highlightthickness=0)
SimOptions.pack()
SimOptions.place(bordermode=OUTSIDE, height=100, width=100,relx = 0.8, rely=0.6)








top.mainloop()