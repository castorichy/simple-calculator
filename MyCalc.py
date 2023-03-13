from tkinter import *
from calc import Calculator

root = Tk()
root.title("Simple Calculator")
root.geometry("225x342")
root.config(bg="light yellow")
root.resizable(True, True)


def checkExceptions(check_list: list):
    """ Dealing with Errors  """
    if check_list[0] == "" or check_list[-1] in "":
        print("Hello")
        return -1
    return 1


class CalculatorApp(Calculator):
    """ Graphical user interface App """
    ans_ret = ""
    total_results = "0"

    operators = ["/", "*", "+", "-", "%"]

    def __init__(self) -> None:
        super().__init__()
        self.ans_ret = CalculatorApp.ans_ret

    def onclick_equal(self, text: str, ans):
        num = ""
        # print(text)
        if len(text) == 1:
            if text in self.operators:
                entry.delete(0, END)
                entry.insert(0, "Syntax Error")
            else:
                self.total_results = text
                entry.delete(0, END)
                entry.insert(0, text)
        for i in text:
            if i not in self.operators:
                num += i
            else:
                num += f" {i} "

        num_l = num.split(" ")
        for i, n in enumerate(num_l):
            if n == "ans":
                num_l.remove("ans")
                num_l.insert(i, ans)

        if checkExceptions(num_l) < 0:
            entry.delete(0, END)
            entry.insert(0, "Syntax Error")
        else:
            return num_l

    def onclick(self, text):
        """"""
        if text == "C":
            entry.delete(0, END)
        elif text == "D":
            entry.delete(entry.index(INSERT) - 1, END)
        elif text == "/":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "%":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "7":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "8":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "9":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "*":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "4":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "5":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "6":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "+":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "1":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "2":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "3":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "-":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "0":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == ".":
            entry.insert(entry.index(INSERT) + 1, text)
        elif text == "ans":
            self.ans_ret = entry.get()
            if self.ans_ret == "":
                self.ans_ret = self.total_results
            entry.delete(0, END)
            entry.insert(entry.index(INSERT) + 1, "ans")
        elif text == "=":
            res = entry.get()
            print("i am: ", self.ans_ret)
            operation = self.onclick_equal(res, self.ans_ret)
            print("Hello 1: ", operation)
            # instance of calculator class
            results = str(self.calculate(operation))
            res_cal = ""
            if results[-2:] == ".0":
                for n in results:
                    if n == ".":
                        break
                    else:
                        res_cal += n
            self.total_results = res_cal
            print(res_cal)

            print("press: ", res_cal)
            ans = res_cal
            print("Hello: ", ans)

            entry.delete(0, END)
            entry.insert(0, res_cal)


# Creating an instance of CalculatorApp ####
cal = CalculatorApp()

# Entry ####
entry = Entry(
    # bg="black",
    # fg="White",
    borderwidth=0,
    # border=0,
    width=11,
    font="Ariel 20",
    justify=RIGHT)
# POSITIONING ENTRY
entry.index(INSERT)
entry.place(y=0, x=3)

# Buttons 1 to 9
button_c = Button(root, text="C", height=2, width=3, command=lambda: cal.onclick("C"))
button_d = Button(root, text="D", height=2, width=3, command=lambda: cal.onclick("D"))
bttn_div = Button(root, text="/", height=2, width=3, command=lambda: cal.onclick("/"))
bttn_mod = Button(root, text="%", height=2, width=3, command=lambda: cal.onclick("%"))

bttn_7 = Button(root, text="7", height=2, width=3, command=lambda: cal.onclick("7"))
bttn_8 = Button(root, text="8", height=2, width=3, command=lambda: cal.onclick("8"))
bttn_9 = Button(root, text="9", height=2, width=3, command=lambda: cal.onclick("9"))
bttn_mul = Button(root, text="x", height=2, width=3, command=lambda: cal.onclick("*"))

bttn_4 = Button(root, text="4", height=2, width=3, command=lambda: cal.onclick("4"))
bttn_5 = Button(root, text="5", height=2, width=3, command=lambda: cal.onclick("5"))
bttn_6 = Button(root, text="6", height=2, width=3, command=lambda: cal.onclick("6"))
bttn_add = Button(root, text="+", height=2, width=3, command=lambda: cal.onclick("+"))

bttn_1 = Button(root, text="1", height=2, width=3, command=lambda: cal.onclick("1"))
bttn_2 = Button(root, text="2", height=2, width=3, command=lambda: cal.onclick("2"))
bttn_3 = Button(root, text="3", height=2, width=3, command=lambda: cal.onclick("3"))
bttn_sub = Button(root, text="-", height=2, width=3, command=lambda: cal.onclick("-"))

bttn_0 = Button(root, text="0", height=2, width=3, command=lambda: cal.onclick("0"))
bttn_dot = Button(root, text=".", height=2, width=3, command=lambda: cal.onclick("."))
bttn_ans = Button(root, text="ans", height=2, width=3, command=lambda: cal.onclick("ans"))
bttn_equal = Button(root, text="=", height=2, width=3, command=lambda: cal.onclick("="))

# POSITIONING BUTTONS
button_c.place(y=50, x=0)
button_d.place(y=50, x=56)
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
