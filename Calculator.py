from tkinter import *
def fun(e):
  global x
  x=e.widget.message
  t1.insert("insert",x)
 
def plus(e):
  global opr,xx
  xx=int(t1.get(1.0,END))
  opr=e.widget.message
  t1.delete(1.0,END)
  
def sub(e):
    global opr,xx
    xx=int(t1.get(1.0,END))
    opr=e.widget.message
    t1.delete(1.0,END)
    
def mul(e):
    global opr,xx
    xx=int(t1.get(1.0,END))
    opr=e.widget.message
    t1.delete(1.0,END)

def div(e):
    global opr,xx
    xx=int(t1.get(1.0,END))
    opr=e.widget.message
    t1.delete(1.0,END)

def per(e):
    global opr,xx
    xx=int(t1.get(1.0,END))
    opr=e.widget.message
    t1.delete(1.0,END)


    

def equ(e):
  global opr,xx
  if(opr=="+"):
    xx=xx+int(t1.get(1.0,END))
    t1.delete(1.0,END)
    rr=str(xx)
    t1.insert("insert",rr)
  elif(opr=="-"):
    xx=xx-int(t1.get(1.0,END))
    t1.delete(1.0,END)
    rr=str(xx)
    t1.insert("insert",rr)
  elif(opr=="*"):
    xx=xx*int(t1.get(1.0,END))
    t1.delete(1.0,END)
    rr=str(xx)
    t1.insert("insert",rr)
  elif(opr=="/"):
    xx=xx/int(t1.get(1.0,END))
    t1.delete(1.0,END)
    rr=str(xx)
    t1.insert("insert",rr)
  elif(opr=="%"):
    xx=xx%int(t1.get(1.0,END))
    t1.delete(1.0,END)
    rr=str(xx)
    t1.insert("insert",rr)
  
      

a1=Tk()
t1=Text(a1)
t1.pack()
t1.place(x=100,y=100,width=300,height=50)
xx=0
yy=0
for i in range(10):
  bb=Button(a1,text=i)
  bb.pack()
  bb.place(x=100+xx,y=160+yy,width=60,height=60)
  bb.message=i
  bb.bind("<Button-1>",fun)
  xx+=70
  if(i%3==0):
    xx=0
    yy+=70
b1=Button(a1,text="+")
b2=Button(a1,text="=")
b3=Button(a1,text="-")
b4=Button(a1,text="*")
b5=Button(a1,text="/")
b6=Button(a1,text="%")

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()


b1.message="+"
b2.message="="
b3.message="-"
b4.message="*"
b5.message="/"
b6.message="%"

b1.bind("<Button-1>",plus)
b2.bind("<Button-1>",equ)
b3.bind("<Button-1>",sub)
b4.bind("<Button-1>",mul)
b5.bind("<Button-1>",div)
b6.bind("<Button-1>",per)



b1.place(x=170,y=160,width=60,height=60)
b2.place(x=240,y=160,width=60,height=60)
b3.place(x=320,y=160,width=60,height=60)
b4.place(x=320,y=230,width=60,height=60)
b5.place(x=320,y=300,width=60,height=60)
b6.place(x=320,y=370,width=60,height=60)
a1.mainloop()
