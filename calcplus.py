from tkinter import *
class Calculator(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.firstNum = Entry(self)
        self.firstNum.pack()
        self.addLabel=Label(self,text='+')
        self.addLabel.pack()
        self.secondNum = Entry(self)
        self.secondNum.pack()
        self.equalLabel=Label(self,text='=')
        self.equalLabel.pack()
        self.countButton = Button(self,text='Go',command=self.count)
        self.countButton.pack()
        self.resultLabel = Label(self,text='0')
        self.resultLabel.pack()
        self.cleanButton = Button(self,text = 'C',command = self.clean)
        self.cleanButton.pack()

    def count(self):
        try:
            if '.' in self.firstNum.get():
                first = float(self.firstNum.get())
            else:
                first = int(self.firstNum.get())
        except ValueError:
            first = 0
        try:
            if '.' in self.secondNum.get():
                second = float(self.secondNum.get())
            else:
                second =int(self.secondNum.get())
        except ValueError:
            second = 0
        self.resultLabel['text'] = str(first+second)

    def clean(self):
        self.firstNum.delete(0,END)
        self.secondNum.delete(0,END)
        self.resultLabel['text'] = '0'


#if name == 'main':
calc = Calculator()
calc.master.title('esay calculator')
calc.mainloop()