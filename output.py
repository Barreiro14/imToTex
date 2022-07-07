'''
For the '\' chars at the begining of every LaTex command
we need a second one in order to not confuse Python.
'''
def init():
    output = open("output.tex", "a")
    output.write("\\begin{align*}\n")

def writeIn(a):
    output = open("output.tex", "a")
    output.write("  {}\n".format(a))

def finish():
    output = open("output.tex", "a")
    output.write("\\end{align*}")


    