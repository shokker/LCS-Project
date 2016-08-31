import tkinter
from tkinter import *
from tkinter.ttk import *
import vizual
import semestral



class Lcs_check:
    def __init__(self,first,second):
        self.first = first
        self.second = second
        self.check = [[0 for x in range(len(second))]for y in range(len(first))]
        
    def table(self):
        for i in range(len(self.first)):
            for j in range(len(self.second)):
                if i>1 and j>1:
                    if self.first[i]==self.second[j]:
                        self.check[i][j] = self.check[i-1][j-1]+1
                    else:
                        self.check[i][j] = max(self.check[i-1][j],self.check[i][j-1])
        return self.check

    def check_t(self):
        self.table()
        solv = ""
        first = self.first[1:]
        second = self.second[1:]
        i , j = len(first),len(second)
        while self.check[i][j]>0:
            if first[i-1] == second[j-1]:
                solv =first[i-1] + solv
                i-=1
                j-=1
            elif self.check[i-1][j]>= self.check[i][j-1]:
                i-=1
            else:
                j-=1
        
        return solv 




class Main:
    def __init__(self,first,second):
        self.first = "  "+first
        self.second = "  "+second
        self.step =0
        self.counter = 0
        self.pole_sol=[]
        self.pole_array=[]
        self.pole_wrongs = [[0 for x in range(len(second)+2)] for y in range(len(first)+2)]
        self.pole = [[0 for x in range(len(second)+2)] for y in range(len(first)+2)]
        self.pole_entry = [[0 for x in range(len(second)+2)] for y in range(len(first)+2)]
        self.root = Tk()
        self.root.title("Longest common subsequence")
        self.root.configure(background='white')
        self.x = 720
        self.image = None
        self.root.bind('<Up>', self.up)
        self.root.bind('<Double-Button-1>', self.up)
        self.root.bind('<Down>', self.down)
        self.root.bind('<Button-3>', self.array)
        self.left = tkinter.PhotoImage(file='icon/left_min.png')
        self.up = tkinter.PhotoImage(file='icon/up_min.png')
        self.diag = tkinter.PhotoImage(file='icon/diag_min.png')
        self.wrong = tkinter.PhotoImage(file='icon/img3.png')
        self.good = tkinter.PhotoImage(file='icon/img4.png')
        self.root.minsize(900,550)
        l = Label(text = "LCS-TRY IT", font = "Calibri 12 bold",background = "white")
        l.place(x = 400 , y = 20)
        l3 = Label(text = "TRY YOUR SOLUTION", font = "Calibri 10 bold",background = "white")
        l3.place(x = 630 , y = 70)
        l1 =Label(text = "first-word: "+str(first), anchor = "w",font = "Calibri 12 bold",background = "white")
        l2 =Label(text = "second-word: "+str(second), anchor = "w",font = "Calibri 12 bold",background = "white")
        l1.place(x = 50 , y = 470)
        l2.place(x = 50 , y = 500)
        b = Button(self.root,text="done",command = self.done)
        b.place(height = 30 , width = 70 ,x =680, y =200)
        c = Button(self.root,text="add field",command = self.add)
        c.place(height = 30 , width = 70 ,x =680, y =100)
        check = Button(self.root,text="Check Table",command = self.check_table)
        check.place(height = 30 , width = 150 ,x =500, y =200)
        
        self.d = Button(self.root,text="VIZUALIZATION",command = self.vizual)
        self.l = Label(text="OK CONGRATULATION",font = "Calibri 15 bold",background = "white",foreground = "green",anchor = 'w')
        self.l1 = Label(text= "wrong solution try again or watch vizualization",font = "Calibri 13 bold",background = "white",foreground = "red",justify = 'right')
        self.menu()
        self.table()
        self.root.mainloop()
        

    def menu(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Help", command=self.help)
        filemenu.add_command(label="Back", command=self.back_w)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu= menubar)


    def table(self):
        styl = Style()
        styl.configure('My.TLabel', background="white",foreground="blue",)
        x ,y = 50 , 50
        lenx, leny = len(self.first), len(self.second)
        for i in range(lenx):
            if i!= 0:
                l = Label(self.root,text = self.first[i],style = 'My.TLabel',width = 30,anchor ="center")
                l.place(height=30,width = 30, x=x ,y=y)   
            for j in range(leny):
                if i==0 and j!=0:
                    l = Label(self.root,text = self.second[j],style = 'My.TLabel',width = 30,anchor ="center")
                    l.place(height=30,width = 30, x=x ,y=y)
                elif i>0 and j>0:
                    s= Entry(self.root,justify = "center",validate="key")
                    s['validatecommand'] = (s.register(self.testVal),'%P','%i','%d')
                    s.insert(0,0)
                    s.place(height=30,width = 30, x=x ,y=y)
                    self.pole_entry[i][j] = s
                x+=30
            y+=30
            x=50

    def array(self,event):
        change = False
        self.counter+=1
        x = event.widget.winfo_x() 
        y = event.widget.winfo_y() 
        x1 = x-50
        y1 = y-50
        if self.pole_array != []:
            for i in range(len(self.pole_array)):
                xi = self.pole_array[i][0] -50
                yi = self.pole_array[i][1] -50
                if x1//30 == xi//30 and y1//30 ==yi//30:
                   self.pole_array[i][2].place_forget()
                   self.pole_array.pop(i)
                   change = True
                   break
            if change ==False:
                self.counter = 1
        if self.counter%3==0:
            self.image = Label(self.root,image=self.diag,style = 'My.TLabel')
            self.image.place(height=10,width=10,x=x+2,y=y+2)
            self.pole_array.append([x,y,self.image])
        elif self.counter%3 == 2:
            self.image = Label(self.root,image=self.left,style = 'My.TLabel')
            self.image.place(height=10,width=5,x=x+2,y=y+15)
            self.pole_array.append([x,y,self.image])
        else:
            self.image = Label(self.root,image=self.up,style = 'My.TLabel')
            self.image.place(height=5,width=10,x= x+15,y=y+2)
            self.pole_array.append([x,y,self.image])
            

    def up(self,event):
        try:
            x = event.widget.winfo_x()-50
            y = event.widget.winfo_y()-50
            old = int(event.widget.get())
            event.widget.delete(0, END) 
            event.widget.insert(10, old + 1)            
        except:
            pass
       

    def down(self,event):
        try:
            x = event.widget.winfo_x()-50
            y = event.widget.winfo_y()-50
            old = int(event.widget.get())
            if old !=0:
                event.widget.delete(0, END) 
                event.widget.insert(10, old - 1)
        except:
            pass
    def done(self):
        my_sol = ""
        lcs = Lcs_check(self.first,self.second)
        sol = lcs.check_t()
        for i in self.pole_sol:
            my_sol = i.get() + my_sol
        if sol == my_sol:
            self.l1.place_forget()
            self.l.place(x = 560 , y =250)
            self.d.place_forget()   
        else:
            self.check_table()
            self.l.place_forget()
            self.l1.place(x = 420 , y =250)
            self.d.place(height = 30 , width = 100 ,x =550, y =300)

    def check_table(self):
        lcs = Lcs_check(self.first,self.second)
        pole_lcs = lcs.table()
        x= 50
        y = 50
        self.getTable()
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if i>0 and j>0:
                    if self.pole[i][j] != pole_lcs[i][j]:
                        wrong_l = Label(self.root,image = self.wrong,background = "white")
                        wrong_l.place(x = x+19 , y = y+19)
                        if self.pole_wrongs[i][j]==0:
                            self.pole_wrongs[i][j]= wrong_l
                        else:
                            self.pole_wrongs[i][j].place_forget()
                            self.pole_wrongs[i][j]= wrong_l
                        
                    else:
                        good_l = Label(self.root,image = self.good,background = "white")
                        good_l.place(x = x+19 , y = y+19)
                        if self.pole_wrongs[i][j] != 0:
                            self.pole_wrongs[i][j].place_forget()
                            self.pole_wrongs[i][j] = good_l
                        else:
                            self.pole_wrongs[i][j] = good_l       
                x+=30
            y+=30
            x=50
            
    def getTable(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if i>0 and j>0:
                    self.pole[i][j] = int(self.pole_entry[i][j].get())

    def add(self):
        if self.step<len(self.first)-2:
            s= Entry(self.root,textvariable="",justify = "center")
            s.place(height=30,width = 30, x=self.x ,y=150)
            self.pole_sol.append(s)
            self.x -=30
            self.step+=1

    def testVal(self,inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': 
            if not inStr[ind].isdigit():
                return False
        return True

    def back_w(self):
        self.root.destroy()
        semestral.Main()

    def quit(self):
        self.root.destroy()

    def vizual(self):
        self.root.destroy()
        vizual.Main(self.first[2:],self.second[2:])

    def help(self):
        tkhelp = Tk()
        tkhelp.minsize(550,450)
        l = Label(tkhelp,text = """\n        The longest common subsequence (LCS)\n
        problem is the problem of finding the longest subsequence common\n
        to all sequences in a set of sequences (often just two sequences).\n
        It differs from problems of finding common substrings: unlike substrings,\n
        subsequences are not required to occupy consecutive positions within the original sequences.\n
        TRY IT \n
        Put numbers into table and create longest common subsequence\n
        CONTROLS \n
        Double-klik: raise number in field \n
        UP: raise number in field \n
        DOWN : decrease number in field \n
        Right-klik: choose type of array \n
        add field button: create fields for your solution \n
        done button : check your solution""",anchor = "w")
        l.pack()
        
        


        
                    
                
        

    

    
