from tkinter import *

root=Tk()
root.title("Simple Calculator")

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
# columnspan-makes sure that each covers all 3 below column size



def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    return

def button_Clear():
    e.delete(0,END)

def button_Add():
    first_no=e.get()
    global f_num #global variable
    global math
    math="addition"
    f_num =int(first_no)
    e.delete(0,END)

def button_Sub():
    first_no=e.get()
    global f_num #global variable
    global math
    math="subtraction"
    f_num =int(first_no)
    e.delete(0,END)

def button_Mul():
    first_no=e.get()
    global f_num #global variable
    global math
    math="multiplication"
    f_num =int(first_no)
    e.delete(0,END)

def button_Div():
    first_no=e.get()
    global f_num #global variable
    global math
    math="division"
    f_num =int(first_no)
    e.delete(0,END)

def button_Equal():
    sec_no=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(sec_no))
    elif math=="subtraction":
        e.insert(0,f_num-int(sec_no))
    elif math=="multiplication":
        e.insert(0,f_num*int(sec_no))
    elif math=="division":
        e.insert(0,f_num/int(sec_no))
    
    return
# define buttons
button1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add=Button(root,text="+",padx=39,pady=20,command=button_Add)
button_equal=Button(root,text="=",padx=91,pady=20,bg="grey",command=button_Equal)
button_clear=Button(root,text="Clear",padx=79,pady=20,command=button_Clear)

button_sub=Button(root,text="-",padx=41,pady=20,command=button_Sub)
button_mul=Button(root,text="x",padx=41,pady=20,command=button_Mul)
button_div=Button(root,text="/",padx=41,pady=20,command=button_Div)


# put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)

button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)



root.mainloop()