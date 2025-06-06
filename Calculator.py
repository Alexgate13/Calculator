from tkinter import *


screen = Tk()
screen.geometry('264x242')
screen.configure(background="black")
screen.title("Calculator")
screen.resizable(height=False, width=False)

def clear():
    e.delete(0, END)

def press(num):
    e.insert(END, num)

def calculate():
    try:
        a = e.get()
        result = eval(a)
        e.delete(0, END)
        e.insert(END, result)
    except:
        e.delete(0, END)
        e.insert(END, "Errror")




e = Entry(screen)

btn = Button(screen, text="7", width=8, height=3, background="black", foreground="white", command=lambda: press("7"))
btn.grid(row=2, column=1)
btn = Button(screen, text="4", width=8, height=3, background="black", foreground="white", command=lambda: press("4"))
btn.grid(row=3, column=1)
btn = Button(screen, text="1", width=8, height=3, background="black", foreground="white", command=lambda: press("1"))
btn.grid(row=4, column=1)
btn = Button(screen, text="C", width=8, height=3, foreground="black", background="red", command=clear)
btn.grid(row=5, column=1)
btn = Button(screen, text="8", width=8, height=3, background="black", foreground="white", command=lambda: press("8"))
btn.grid(row=2, column=2)
btn = Button(screen, text="5", width=8, height=3, background="black", foreground="white", command=lambda: press("5"))
btn.grid(row=3, column=2)
btn = Button(screen, text="2", width=8, height=3, background="black", foreground="white", command=lambda: press("2"))
btn.grid(row=4, column=2)
btn = Button(screen, text="0", width=8, height=3, background="black", foreground="white", command=lambda: press("0"))
btn.grid(row=5, column=2)
btn = Button(screen, text="9", width=8, height=3, background="black", foreground="white", command=lambda: press("9"))
btn.grid(row=2, column=3)
btn = Button(screen, text="6", width=8, height=3, background="black", foreground="white", command=lambda: press("6"))
btn.grid(row=3, column=3)
btn = Button(screen, text="3", width=8, height=3, background="black", foreground="white", command=lambda: press("3"))
btn.grid(row=4, column=3)
btn = Button(screen, text="=", width=8, height=3, foreground="black", background="green", command=calculate)
btn.grid(row=5, column=3)
btn = Button(screen, text="/", width=8, height=3, background="black", foreground="white", command=lambda: press("/"))
btn.grid(row=2, column=4)
btn = Button(screen, text="*", width=8, height=3, background="black", foreground="white", command=lambda: press("*"))
btn.grid(row=3, column=4)
btn = Button(screen, text="-", width=8, height=3, background="black", foreground="white", command=lambda: press("-"))
btn.grid(row=4, column=4)
btn = Button(screen, text="+", width=8, height=3, background="black", foreground="white", command=lambda: press("+"))
btn.grid(row=5, column=4)



e.grid(row=0, column=2, columnspan=2)


screen.mainloop()