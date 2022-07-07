
def init():
    output = open("output.txt", "a")
    output.write("\\")
    output.write("begin{equation}\n")

def writeIn(a):
    output = open("output.txt", "a")
    output.write("  {}\n".format(a))

def finish():
    output = open("output.txt", "a")
    output.write("\end{equation}")