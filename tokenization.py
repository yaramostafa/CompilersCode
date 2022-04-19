#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
def tokenization(code_in):
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
    code_in = code_in.split()

    if code_in[0] == tokensLoop[0]:  # if it starts with until
        i = 1
        while code_in[i] != tokensLoop[1] and i< len(code_in):
            if (re.fullmatch(ID, code_in[i])) and (re.fullmatch(assignment, code_in[i+1])) and (re.fullmatch(ID, code_in[i+2]) or re.fullmatch(NUM, code_in[i+2])) and (code_in[i + 3] == tokensID[1]):
                i+= 4

            else:
                print("Invalid statement")
                return 0
        if i > len(code_in):
            print("Invalid statement")
            return 0
        if(code_in[i] == tokensLoop[1]) and (re.fullmatch(ID, code_in[i+1])) and (re.fullmatch(Compare_OPS, code_in[i+2])) and (re.fullmatch(NUM, code_in[i+3]) or re.fullmatch(ID, code_in[i+3])) and i + 4 == len(code_in):
            print("VALID")

        else:

            print("Invalid statement")
            return 0

    else:

        print("Invalid statement")
        return 0

    tokens = []
    for tok in code_in:
        if code_in is None:
            print("Invalid repeat statement")
            return None
        else:
            if re.fullmatch(Unt, tok):
                print("LoopToken :", tok)
                tokens.append(tok)
            elif re.fullmatch(rep, tok):
                print("LoopToken :", tok)
                tokens.append(tok)
            elif re.fullmatch(ID, tok):
                print("ID :", tok)
                tokens.append(tok)
            elif re.fullmatch(NUM, tok):
                print("Num :", tok)
                tokens.append(tok)
            elif re.fullmatch(assignment, tok):
                print("Assignment:", tok)
                tokens.append(tok)
            elif re.fullmatch(Compare_OPS,tok) and (tok != "=="):
                print("Comparison:", tok)
                tokens.append(tok)
            elif re.fullmatch(semi_col, tok):
                print("semi_col:", tok)
                tokens.append(tok)
            else:
                print("invalid token", tok)
                return 0

    return tokens

def main():
    see = input("enter the statement: ")
    tokenization(see)
main()


# In[ ]:




