import tkinter
from tkinter import *


def gui_window(w=500, h=300):
    ws = root.winfo_screenwidth()
    hs=root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry("%dx%d+%d+%d" %(w,h,x,y))
root = tkinter.Tk(className='welcome gui')
gui_window(800,500)
list_li=['a','b','c','d']
listb=Listbox(root)
listb.pack(fill=BOTH, expand=1)
for k in range(50):
    listb.insert(END,k)

root.mainloop()