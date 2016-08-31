import tkinter
from tkinter import *
from tkinter.ttk import *
import time
import semestral
import tryit


class Main:
    def __init__(self,first,second):
        self.first = "  "+first
        self.second = "  "+second
        self.can = Tk()
        self.step = 0
        self.boolen = True
        self.a = None
        self.b = None
        self.pole_b= []
        self.pole_label = []
        self.left = tkinter.PhotoImage(file='icon/left.png')
        self.up = tkinter.PhotoImage(file='icon/up.png')
        self.diag = tkinter.PhotoImage(file='icon/diag.png')
        self.img1 = tkinter.PhotoImage(file='icon/img1.png')
        self.img2 = tkinter.PhotoImage(file='icon/img2.png')
        self.can.title("Longest common subsequence")
        self.can.configure(background="white")
        self.can.minsize(900,550)
        self.menu()
        self.g = Canvas(bg = "white")
        self.g.place(height = 500, width = 900 , x =0 ,y = 0)
        self.g.create_text(400,25 ,text = "LCS-VIZUALIZATION", font = "Calibri 12 bold")
        self.g.create_text(50,440 ,text = "first-word: "+str(first), anchor = "w",font = "Calibri 12 bold")
        self.g.create_text(50,470 ,text = "second-word: "+str(second),anchor = "w", font = "Calibri 12 bold")
        self.buttons()
        self.table()
        self.pole = [[[0,"n",False] for x in range(len(second)+2)] for y in range(len(first)+2)]
        self.can.mainloop()
       
        

    def menu(self):
        menubar = Menu(self.can)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Help", command=self.help)
        filemenu.add_command(label="Back", command=self.back_w)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.can.config(menu= menubar)

    def buttons(self):
        styl=Style()
        styl.configure('My.TButton',background="white")
        self.button1=Button(self.can,text="PREVIOUS",command=self.back,style = "My.TButton")
        self.button1.place(height=30, width=150, x=50, y=510)
        self.button1.config(state = "disabled")
        self.button2=Button(self.can,text="NEXT",command=self.next,style = "My.TButton")
        self.button2.place(height=30, width=150, x=650, y=510)
        self.button3=Button(self.can,text="TRY IT!",command=self.tryit,style = "My.TButton")

        
    def next(self):
        self.step+=1
        [self.g.delete(x) for x in self.pole_label]
        self.pole_label=[]
        self.g.delete(self.b)
        self.g.update()
        if len(self.first)-1>=self.step:
            self.button1.config(state = "disabled")
            self.button2.config(state = "disabled")
            self.table()
            self.button2.config(state = "normal")
            if self.step <=1:
                self.button1.config(state = "disabled")
            else:
                self.button1.config(state = "normal")
            
        else:
            self.button1.config(state = "disabled")
            self.button2.config(state = "disabled")
            self.g.move(self.a,6000,0)
            self.solve()
        

    def back(self):
        self.step-=1
        if self.step <=1:
            self.button1.config(state = "disabled")
        else:
            self.button1.config(state = "normal")
        [self.g.delete(x) for x in self.pole_label]
        self.pole_label=[]
        for x in range(len(self.second)-2):
            a = self.pole_b.pop()
            self.g.delete(a[0])
            self.g.delete(a[1])
        self.g.move(self.a,0,-30)
        self.g.update()
    
    def table_cell(self,x,y):
        self.g.create_rectangle(x,y,x+30,y+30)
        
    def table_circle(self,x,y,color):
        c = self.g.create_oval(x,y,x+30,y+30,outline=color)
        return c 

    def table_text(self,x,y,text,color = "black"):
        t= self.g.create_text(x,y,text =text,fill = color)
        return t 
    def arrow(self,x,y,draw):
        if draw =="n":
            return
        elif draw=="l":
            image = self.g.create_image(x,y+15,image=self.left)
        elif draw=="u":
            image = self.g.create_image(x+15,y,image=self.up)
        elif draw=="d":
            image = self.g.create_image(x,y,image=self.diag)
        return image

    def table_img(self,x,y,draw):
        if draw == "1":
            image = self.g.create_image(x,y+15,image=self.img1)
        else:
            image = self.g.create_image(x,y+15,image=self.img2)
            
            

        

    def table(self):
        x,y = 50 , 50
        dy = 0
        lenx,leny = len(self.first), len(self.second)
        booly =True
        for i in range(lenx):
            indexA = self.first[i]
            if i!=0 and self.step==0:
                self.table_text(x+15,y+15,self.first[i])
            if self.step>1 and self.step==i:
                if self.boolen:
                    self.a = self.table_circle(x,y,"red")
                    self.boolen = False   
                else:
                    self.g.move(self.a,0,30)
            for j in range(leny):
                indexB = self.second[j]
                if self.step==0:
                    self.table_cell(x,y)
                if i==0 and j!=0 and self.step==0:
                    self.table_text(x+15,y+15,self.second[j])
                if self.step>1 and j>1 and i==self.step:
                    if booly:
                       self.b = self.table_circle(x,50,"blue")
                       booly = False
                    else:
                       self.g.move(self.b,30,0)
                if self.step>=1 and ((j==1 and i!=0) or (i==1 and j!=0)) and self.pole[i][j][2]==False:
                    self.table_text(x+15,y+15,str(self.pole[i][j][0]))
                    self.pole[i][j][2]=True
                if i<self.step and i>1 and j>1 and self.pole[i][j][2]==False:
                    self.table_text(x+15,y+15,str(self.pole[i][j][0]))
                    self.arrow(x,y,self.pole[i][j][1])
                    self.pole[i][j][2]=True
                if self.step==i and i>1 and j>1:
                    if indexA==indexB:
                        self.pole[i][j][0] = self.pole[i-1][j-1][0] +1
                        self.pole[i][j][1]="d"
                        self.pole_label.append(self.table_text(650,80+40*dy,"\""+indexA.upper()+"\" is match with \""+ indexB.upper() + "\" then \""+ indexA.upper() + "\" is appended to he upper left sequence","#de00ff"))
                        self.pole_label.append(self.table_text(650,95+40*dy,"LCS(i,j)=LCS(i-1,j-1)+1"))                   
                        dy+=1
                    elif self.pole[i-1][j][0]<self.pole[i][j-1][0]:
                        self.pole[i][j][0] = self.pole[i][j-1][0]
                        self.pole[i][j][1]="l"
                        self.pole_label.append(self.table_text(650,80+40*dy,"\""+indexA.upper()+"\" is not match with \""+ indexB.upper() + "\" and left sequence is higher then upper seguence","#00ff0c"))
                        self.pole_label.append(self.table_text(650,95+40*dy,"LCS(i,j)=LCS(i,j-1)")) 
                        dy+=1
                    else:
                        self.pole[i][j][0] = self.pole[i-1][j][0]
                        self.pole[i][j][1]="u"
                        self.pole_label.append(self.table_text(650,80+40*dy,"\""+indexA.upper()+"\" is not match with \""+ indexB.upper() + "\" and upper sequence is higher then left seguence or same","#ffa200"))
                        self.pole_label.append(self.table_text(650,95+40*dy,"LCS(i,j)=LCS(i-1,j)")) 
                        dy+=1
                    self.pole_b.append((self.table_text(x+15,y+15,str(self.pole[i][j][0])),self.arrow(x,y,self.pole[i][j][1])))
                    self.pole[i][j][2]=True
                    self.g.update()
                    time.sleep(0.5)
                
                x+=30
            booly = True
            y+=30
            x = 50
        


    def solve(self):
        self.g.create_text(795,200,text ="RESULT OF LCS",font = "Calibri 12 bold",anchor = 'e')
        solv = ""
        x ,y = 65,50
        first = self.first[1:]
        second = self.second[1:]
        w = 0
        i , j = len(first),len(second)
        while self.pole[i][j][0]>0:
            if first[i-1] == second[j-1]:
                self.table_img(x+30*(j),y+30*(i),"1")
                self.table_cell(765-30*w,235)
                self.table_text(780-30*w,250,first[i-1])
                solv =first[i-1] + solv
                i-=1
                j-=1
                w+=1
            elif self.pole[i-1][j][0]>= self.pole[i][j-1][0]:
                self.table_img(x+30*(j),y+30*(i),"0")
                i-=1
            else:
                self.table_img(x+30*(j),y+30*(i),"0")
                j-=1
            self.g.update()
            time.sleep(0.2)
        self.button3.place(height=30, width=200, x=796, y=300,anchor ='e')

    def help(self):
        tkhelp = Tk()
        tkhelp.minsize(550,350)
        l = Label(tkhelp,text = """\n        The longest common subsequence (LCS)\n
        problem is the problem of finding the longest subsequence common\n
        to all sequences in a set of sequences (often just two sequences).\n
        It differs from problems of finding common substrings: unlike substrings,\n
        subsequences are not required to occupy consecutive positions within the original sequences.\n
        VIZUALIZATION \n
        Watch and learn how algoritm works \n
        CONTROLS \n
        NEXT button : make next step \n
        PREVIOUS button: make previous step \n
        """,anchor = "w")
        l.pack()

    def back_w(self):
        self.can.destroy()
        semestral.Main()

    def quit(self):
        self.can.destroy()

    def tryit(self):
        self.can.destroy()
        tryit.Main(self.first[2:],self.second[2:])
        
                
                
        
        

    
                
        





    
    
        

    
        
