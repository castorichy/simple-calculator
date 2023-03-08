from tkinter import *
from calc import Calculator as calc

root = Tk()
root.title("Simple Calculator")
root.geometry("225x400")
root.config(bg="light yellow")

ans = 0

def onclick_equal(text: str):
    operators = ["/", "x", "+", "-", "%"]
    num = ""

    for i in text:
        if i not in operators:
            num += i
        else:
            num += f" {i} "
    print(num)
    #return num



def onclick(text):
    match text:
        case "C":
            entry.delete(0, END)
        case "D":
            entry.delete(1, END)
            if len(entry.get()) == 1:
                entry.delete(0, END)
        case "/":
            entry.insert(entry.index(INSERT) + 1, text)
        case "%":
            entry.insert(entry.index(INSERT) + 1, text)
        case "7":
            entry.insert(entry.index(INSERT) + 1, text)
        case "8":
            entry.insert(entry.index(INSERT) + 1, text)
        case "9":
            entry.insert(entry.index(INSERT) + 1, text)
        case "X":
            entry.insert(entry.index(INSERT) + 1, text)

        case "4":
            entry.insert(entry.index(INSERT) + 1, text)
        case "5":
            entry.insert(entry.index(INSERT) + 1, text)
        case "6":
            entry.insert(entry.index(INSERT) + 1, text)
        case "+":
            entry.insert(entry.index(INSERT) + 1, text)

        case "1":
            entry.insert(entry.index(INSERT) + 1, text)
        case "2":
            entry.insert(entry.index(INSERT) + 1, text)
        case "3":
            entry.insert(entry.index(INSERT) + 1, text)
        case "-":
            entry.insert(entry.index(INSERT) + 1, text)

        case "0":
            entry.insert(entry.index(INSERT) + 1, text)
        case ".":
            entry.insert(entry.index(INSERT) + 1, text)
        case "ans":
            pass
        case "=":
            res = entry.get()
            onclick_equal(res)








#### Entry ####
entry = Entry(
   # bg="black",
   # fg="White",
    borderwidth=0,
   # border=0,
    width=11,
    font=("Ariel 20")
)
#### POSITIONING ENTRY ####
entry.index(INSERT)
entry.place(y=0, x=3)

#### Buttons 1 to 9 ####
bttn_c = Button(root, text="C", height=2, width=3, command= lambda: onclick("C"))
bttn_d = Button(root, text="D", height=2, width=3, command= lambda: onclick("D"))
bttn_div = Button(root, text="/", height=2, width=3, command=lambda: onclick("/"))
bttn_mod = Button(root, text="%", height=2, width=3, command=lambda: onclick("%"))


bttn_7 = Button(root, text="7", height=2, width=3, command=lambda: onclick("7"))
bttn_8 = Button(root, text="8", height=2, width=3, command=lambda: onclick("8"))
bttn_9 = Button(root, text="9", height=2, width=3, command=lambda: onclick("9"))
bttn_mul = Button(root, text="X", height=2, width=3, command=lambda: onclick("X"))

bttn_4 = Button(root, text="4", height=2, width=3, command=lambda: onclick("4"))
bttn_5 = Button(root, text="5", height=2, width=3, command=lambda: onclick("5"))
bttn_6 = Button(root, text="6", height=2, width=3, command=lambda: onclick("6"))
bttn_add = Button(root, text="+", height=2, width=3, command=lambda: onclick("+"))

bttn_1 = Button(root, text="1", height=2, width=3, command=lambda: onclick("1"))
bttn_2 = Button(root, text="2", height=2, width=3, command=lambda: onclick("2"))
bttn_3 = Button(root, text="3", height=2, width=3, command=lambda: onclick("3"))
bttn_sub = Button(root, text="-", height=2, width=3, command=lambda: onclick("-"))

bttn_0 = Button(root, text="0", height=2, width=3, command=lambda: onclick("0"))
bttn_dot = Button(root, text=".", height=2, width=3, command=lambda: onclick("."))
bttn_ans = Button(root, text="ans", height=2, width=3, command=lambda: onclick("ans"))
bttn_equal = Button(root, text="=", height=2, width=3, command=lambda: onclick("="))

#### POSITIONING BUTTONS ####
bttn_c.place(y=50, x=0)
bttn_d.place(y=50, x=56)
bttn_div.place(y=50, x=112)
bttn_mod.place(y=50, x=168)

bttn_7.place(y=108, x=0)
bttn_8.place(y=108, x=56)
bttn_9.place(y=108, x=112)
bttn_mul.place(y=108, x=168)

bttn_4.place(y=166, x=0)
bttn_5.place(y=166, x=56)
bttn_6.place(y=166, x=112)
bttn_add.place(y=166, x=168)

bttn_1.place(y=224, x=0)
bttn_2.place(y=224, x=56)
bttn_3.place(y=224, x=112)
bttn_sub.place(y=224, x=168)

bttn_0.place(y=282, x=0)
bttn_dot.place(y=282, x=56)
bttn_ans.place(y=282, x=112)
bttn_equal.place(y=282, x=168)

root.mainloop()
