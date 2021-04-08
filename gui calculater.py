from tkinter import *

def bclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def bclearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def bqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


root = Tk()
root.title("calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(root, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue",  justify='right').grid(columnspan=4)

b7 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7",command=lambda: bclick(7)).grid(row=1, column=0)
b8 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", command=lambda: bclick(8)).grid(row=1, column=1)
b9 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", command=lambda: bclick(9)).grid(row=1, column=2)
add = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", command=lambda: bclick('+')).grid(row=1, column=3)
b4 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4",  command=lambda: bclick(4)).grid(row=2, column=0)
b5 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5",command=lambda: bclick(5)).grid(row=2, column=1)
b6 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", command=lambda: bclick(6)).grid(row=2, column=2)
sub = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", command=lambda: bclick('-')).grid(row=2, column=3)
b1 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", command=lambda: bclick(1)).grid(row=3, column=0)
b2 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2",  command=lambda: bclick(2)).grid(row=3, column=1)
b3 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3",command=lambda: bclick(3)).grid(row=3, column=2)
mul = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", command=lambda: bclick('*')).grid(row=3, column=3)
b0 = Button(root, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0",command=lambda: bclick(0)).grid(row=4, column=0)
clear=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial', 20 ,'bold'),text="C",command=bclearDisplay).grid(row=4,column=1)
equals=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial', 20 ,'bold'),text="=",command=bqualsInput).grid(row=4,column=2)
div=Button(root,padx=16,pady=16,bd=8,fg="black",font=('arial', 20 ,'bold'),text="/",command=lambda:bclick('/')).grid(row=4,column=3)

root=mainloop()
