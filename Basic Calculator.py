from tkinter import *
import tkinter as tk
app = tk.Tk()
app.title('Basic Calculator')
app.geometry('600x600')

equation = StringVar()

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")
    
def equalpress():
    try:
        global expression
        total =str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""
        
result = tk.Variable(app)
expression_field = Entry(app,textvariable=equation,width=40).place(x=20,y=20)
    




tk.Button(app,text='1',font="Andalus",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(1)).place(x =20,y=190)
tk.Button(app,text='2',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(2)).place(x =140,y=190)
tk.Button(app,text='3',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(3)).place(x =260,y=190)
tk.Button(app,text='+',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press('+')).place(x =380,y=190)        
tk.Button(app,text='4',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(4)).place(x =20,y=270)
tk.Button(app,text='5',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(5)).place(x =140,y=270)
tk.Button(app,text='6',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(6)).place(x =260,y=270)
tk.Button(app,text='-',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press('-')).place(x =380,y=270)
tk.Button(app,text='7',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(7)).place(x =20,y=350)
tk.Button(app,text='8',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(8)).place(x =140,y=350)
tk.Button(app,text='9',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(9)).place(x =260,y=350)
tk.Button(app,text='x',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press('*')).place(x =380,y=350)
tk.Button(app,text='.',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press('.')).place(x =20,y=430)
tk.Button(app,text='0',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press(0)).place(x =140,y=430)
tk.Button(app,text='=',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :equalpress()).place(x =260,y=430)
tk.Button(app,text='/',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :press('/')).place(x =380,y=430)
tk.Button(app,text='clear',font="calibri",fg = 'yellow',bg = 'purple',highlightcolor="purple",width=10,height=2,command =lambda :clear()).place(x =380,y=110)

app.mainloop()
