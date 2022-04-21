import tkinter as tk
from PIL import Image, ImageTk
import re

ID = re.compile(r"[A-Za-z]+")
NUM = re.compile(r"[0-9]+")
Compare_OPS = re.compile(r">|<|=|>=|<=")
assignment = re.compile(":=")
semi_col = re.compile(";")
tokensID = (':=', ';')
tokensLoop = ('repeat', 'until')
rep = "repeat"
repeat = re.compile(rep)
Unt = "until"
until = re.compile(Unt)
root = tk.Tk()


def statment_accept(code_in):
    code_in = code_in.split()

    if code_in[0] == tokensLoop[0] and len(code_in)>1: # if it starts with until
        var=0
        l=tk.Label(root,text="Keyword : repeat at state 2 ").grid(row=4,column=1)
        i = 1
        while code_in[i] != tokensLoop[1] and i < len(code_in):
            if (re.fullmatch(ID, code_in[i])):
                l=tk.Label(root,text="ID at state 3 :"+code_in[i]).grid(row=5,column=1+var)
                if (i+1)>= len(code_in):
                    l = tk.Label(root, text="invalid transition to state 4 ",bg='red').grid(row=4,column=1)
                    return
                if re.fullmatch(assignment, code_in[i + 1]):
                    l = tk.Label(root, text="assignment at state 4 :  " + code_in[i + 1]).grid(row=6,column=1+var)
                    if (i + 2) >= len(code_in):
                        l = tk.Label(root, text="invalid transition to state 5 ", bg='red').grid(row=4,column=1)
                        return
                    if re.fullmatch(ID, code_in[i + 2]) or re.fullmatch(NUM, code_in[i + 2]):
                        l = tk.Label(root, text=" state 5 : " + code_in[i + 2] ).grid(row=7,column=1+var)
                        if (i + 3) >= len(code_in):
                            l = tk.Label(root, text="invalid transition to state 6 ", bg='red').grid(row=4,column=1)
                            return
                        if (code_in[i + 3] == tokensID[1]):
                            l = tk.Label(root, text="semi colon at state 6 : " + code_in[i+3]).grid(row=8,column=1+var)

                        else:
                            l = tk.Label(root, text="invalid transition to state 6",bg='red').grid(row=4,column=1)
                            return
                    else:
                        l = tk.Label(root, text="invalid transition to state 5", bg='red').grid(row=4,column=1)
                        return
                else:
                    l = tk.Label(root, text="invalid transition to state 4", bg='red').grid(row=4,column=1)
                    return

            else:
                l = tk.Label(root, text="invalid transition to state 3", bg='red').grid(row=4,column=1)
                return
            i = i + 4
            if (i >= len(code_in)):
                l = tk.Label(root, text="invalid transition to state 7", bg='red').grid(row=4,column=1)
                return
            var += 1
        if (code_in[i] == tokensLoop[1]):
            l = tk.Label(root, text="Keyword : until at state 7 ").grid(row=9,column=1)
            if (i + 1) >= len(code_in):
                l = tk.Label(root, text="invalid transition to state 8", bg='red').grid(row=4,column=1)
                return
            if (re.fullmatch(ID, code_in[i + 1])) or (re.fullmatch(NUM, code_in[i + 1])) :
                l = tk.Label(root, text="TRANSITION TO STATE 8 : "+ code_in[i+1]).grid(row=10,column=1)
                if (i + 2) >= len(code_in):
                    l = tk.Label(root, text="invalid transition to state 9",bg='red').grid(row=4,column=1)
                    return
                if (re.fullmatch(Compare_OPS, code_in[i + 2])):
                    l = tk.Label(root, text="TRANSITION TO STATE 9 : " + code_in[i + 2]).grid(row=11,column=1)
                    if (i + 3) >= len(code_in):
                        l = tk.Label(root, text="invalid transition to state 10",bg='red').grid(row=4,column=1)
                        return
                    if re.fullmatch(NUM, code_in[i + 3]) or re.fullmatch(ID, code_in[i + 3]):
                        l = tk.Label(root, text="TRANSITION TO STATE 10 : " + code_in[i + 3]).grid(row=12,column=1)
                    else:
                        l = tk.Label(root, text="invalid transition to state 10" + code_in[i+3],bg='red').grid(row=4,column=1)
                        return

                else:
                    l = tk.Label(root, text="invalid transition to state 9" + code_in[i+2],bg='red').grid(row=4,column=1)
                    return

            else:
                l=tk.Label(root, text="inValid token at state 8" + code_in[i+1], bg='red').grid(row=4,column=1)
                return

        else:
            l = tk.Label(root, text=" invalid token at state 7" + code_in[i], bg='red').grid(row=4, column=1)
            return

        if ((i + 4) < len(code_in)):
            l = tk.Label(root, text="inValid tranition to extra state", bg='red').grid(row=4, column=1)
            return

    else:

        l = tk.Label(root, text=" inValid token at state 2", bg='red').grid(row=4, column=1)




def main():

    root.title("Tokenization")
    root.configure(bg='light blue')
    root.geometry("1200x700")
    img = ImageTk.PhotoImage(Image.open("Dfa.jpg"))
    l = tk.Label(image=img).grid(row=0, column=4)
    tk.Label(root, text="Please enter Statements: ", font=('Times', 20), fg="Purple",bg='sky blue').grid(row=0)
    user_input = tk.Entry(root)
    user_input.place(x=10, y=370, width=300, height=40)
    result = tk.Label(root,bg='light blue')
    result.place(x=50, y=550)
    btn = tk.Button(root, text='Tokenize', font=('Times', 12), bg='blue violet')
    btn.config(command=lambda: result.config(text=statment_accept(user_input.get())))
    btn.grid(row=3, column=1, sticky=tk.W, pady=4)

    root.mainloop()

if __name__ == "__main__":
    main()
