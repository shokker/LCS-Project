from tkinter import *
from tkinter.ttk import *
import vizual
import tryit


class Main():
    def __init__(self):
        self.can=Tk()
        self.can.title("Longest common subsequence")
        self.can.configure(background="white")
        self.can.minsize(500,300)
        self.menu()
        self.gui_elements()
        self.can.mainloop()
        
    def menu(self):
        menu = Menu(self.can)
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label="Help", command=self.helptk)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=filemenu)
        self.can.config(menu= menu)

    def gui_elements(self):
        styl=Style()
        self.word1 = StringVar()
        self.word2 = StringVar()
        self.max_len = 10
        styl.configure('My.TButton',background="white")
        styl.configure('My.TLabel', background="white",foreground="blue")
        styl.configure('Top.TLabel', background="white",foreground="red",font = "Calibri 15")
        
        lab0 = Label(self.can,text="Longest common subsequence",style = "Top.TLabel")
        lab0.place(height=25, width=500, x=120, y=10)
        
        lab1 = Label(self.can,text="insert first word",style = "My.TLabel")
        lab1.place(height=20, width=150, x=50, y=60)
        
        lab2 = Label(self.can,text="insert second word",style = "My.TLabel")
        lab2.place(height=20, width=150, x=50, y=100)

        self.word1.trace_variable("w",self.check_1)
        self.word2.trace_variable("w",self.check_2)
        self.a = Entry(self.can, textvariable = self.word1)
        self.a.place(height=20, width=90, x=210, y=60)
        
        self.b =  Entry(self.can, textvariable = self.word2)
        self.b.place(height=20, width=90, x=210, y=100)
        
        button1=Button(self.can,text="vizualization",command=self.vizualization,style = "My.TButton")
        button1.place(height=30, width=150, x=80, y=150)
        button2=Button(self.can,text="try it yourself",command=self.try_it,style = "My.TButton")
        button2.place(height=30, width=150, x=270, y=150)
        

    def check_1(self,*args):
        w = self.word1.get()
        if len(w) > self.max_len:
            self.word1.set(w[:self.max_len])

    def check_2(self,*args):
        w = self.word2.get()
        if len(w) > self.max_len:
            self.word2.set(w[:self.max_len])

    def vizualization(self):
        first = self.a.get()
        second = self.b.get()
        self.can.destroy()
        vizual.Main(first,second)
        
    def try_it(self):
        first = self.a.get()
        second = self.b.get()
        self.can.destroy()
        tryit.Main(first,second)
    def helptk(self):
        tkhelp = Tk()
        tkhelp.minsize(550,250)
        l = Label(tkhelp,text = """\n        The longest common subsequence (LCS)\n
        problem is the problem of finding the longest subsequence common\n
        to all sequences in a set of sequences (often just two sequences).\n
        It differs from problems of finding common substrings: unlike substrings,\n
        subsequences are not required to occupy consecutive positions within the original sequences.\n
        Add your words into fields and \n
        you can watch vizualization how algoritm work or try it yourself""",anchor = "w")
        l.pack()

    def quit(self):
        self.can.destroy()
        
        
        

               
if __name__ == '__main__':
    main = Main()
        


    
