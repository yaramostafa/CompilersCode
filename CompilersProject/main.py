import tkinter as tk
from PIL import Image, ImageTk
import re

ID = re.compile(r"[A-Za-z]+")
NUM = re.compile(r"[0-9]+")
Compare_OPS = re.compile(r"[>|<|=|>=|<=]")
assignment = re.compile(":=")
semi_col = re.compile(";")
tokensID = (':=', ';')
tokensLoop = ('repeat', 'Until')
rep = "repeat"
repeat = re.compile(rep)
Unt = "Until"
Until = re.compile(Unt)


def statment_accept(code_in):
    code_in = code_in.split()

    if code_in[0] == tokensLoop[0]:  # if it starts with until
        i = 1
        while code_in[i] != tokensLoop[1] and i < len(code_in):
            if (len(code_in) - 1) % 4 == 0 and (re.fullmatch(ID, code_in[i])) and (
            re.fullmatch(assignment, code_in[i + 1])) and (
                    re.fullmatch(ID, code_in[i + 2]) or re.fullmatch(NUM, code_in[i + 2])) and (
                    code_in[i + 3] == tokensID[1]):
                i += 4

            else:
                print("Invalid statement")
                return 0
        if i > len(code_in):
            print("Invalid statement")
            return 0
        if (code_in[i] == tokensLoop[1]) and (re.fullmatch(ID, code_in[i + 1])) and (
        re.fullmatch(Compare_OPS, code_in[i + 2])) and (
                re.fullmatch(NUM, code_in[i + 3]) or re.fullmatch(ID, code_in[i + 3])) and i + 4 == len(code_in):
            print("VALID")

        else:

            print("Invalid statement")
            return 0

    else:

        print("Invalid statement at state 1")
        return 0

    tokens = []
    for tok in code_in:
        if code_in is None:
            print("Invalid repeat statement")
            return None
        else:
            if re.fullmatch(Unt, tok):
                print("Keyword :", tok)
                tokens.append(["Keyword", tok])
            elif re.fullmatch(rep, tok):
                print("keyword :", tok)
                tokens.append(["Keyword", tok])
            elif re.fullmatch(ID, tok):
                print("ID :", tok)
                tokens.append(['ID', tok])
            elif re.fullmatch(NUM, tok):
                print("Num :", tok)
                tokens.append(['NUM', tok])
            elif re.fullmatch(assignment, tok):
                print("Assignment:", tok)
                tokens.append(['Assignment', tok])
            elif re.fullmatch(Compare_OPS, tok) and (tok != "=="):
                print("Comparison:", tok)
                tokens.append(['Comparison', tok])
            elif re.fullmatch(semi_col, tok):
                print("semi_col:", tok)
                tokens.append(['semi_col', tok])
            else:
                print("invalid token", tok)
                return 0

    return tokens


def main():
    root = tk.Tk()
    root.title("Tokenization")

    img = ImageTk.PhotoImage(Image.open("Dfa.jpg"))
    l = tk.Label(image=img).grid(row=0, column=4)

    tk.Label(root, text="Please enter a sentence: ").grid(row=0)
    user_input = tk.Entry(root)
    user_input.grid(row=0, column=1)
    result = tk.Label(root, text='')
    result.grid(row=2, column=0, columnspan=2)
    btn = tk.Button(root, text='Tokenize')
    btn.config(command=lambda: result.config(text=statment_accept(user_input.get())))
    btn.grid(row=1, column=1, sticky=tk.W, pady=4)

    root.mainloop()


if __name__ == "__main__":
    main()