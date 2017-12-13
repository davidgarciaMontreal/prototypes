import turtle
import graphics
import tkinter


class DrawingApplication(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.graphicsCommands = graphics.PyList()


    def buildWindow(self):

        self.master.title("Draw")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)

        def newWindow():
            pass
        fileMenu.add_command(label="New", command=newWindow)

        def parse(filename):
            pass
        def loadFile():
            pass

        fileMenu.add_command(label="Load...", command=loadFile)

        def addToFile():
            pass

        fileMenu.add_command(label="Load Into...", command=addToFile)

        def write(filename):
            pass

        def saveFile():
            pass
        fileMenu.add_command(label="Save As...", command=saveFile)

        fileMenu.add_command(label="Exit", command=self.master.quit)

        bar.add_cascade(label="File", menu=fileMenu)

        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.shape("circle")
        screen = theTurtle.getscreen()

        screen.tracer(0)

        sideBar = tkinter.Frame(self, padx=5, pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        pointLabel = tkinter.Label(sideBar, text="Width")
        pointLabel.pack()

        widthSize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar, textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))

        radiusLabel = tkinter.Label(sideBar, text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar, textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()

        def circleHandler():
            pass

        circleButton = tkinter.Button(sideBar, text="Draw Circle", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)
        screen.colormode(255)
        penLabel = tkinter.Label(sideBar, text="Pen Color")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar, textvariable=penColor)
        penEntry.pack()
        penColor.set("#000000")

        def getPenColor():
            pass

        penColorButton = tkinter.Button(sideBar, text="Pick Pen Color", command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)
        fillLabel = tkinter.Label(sideBar, text="Fill Color")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar, textvariable=fillColor)
        fillEntry.pack()
        fillColor.set("#000000")

        def getFillColor():
            pass

        fillColorButton = \
            tkinter.Button(sideBar, text="Pick Fill Color", command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH)

        def beginFillHandler():
            pass

        beginFillButton = tkinter.Button(sideBar, text="Begin Fill", command=endFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH)
        def endFillHandler():
            pass
        endFillButton = tkinter.Button(sideBar, text="End Fill", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)

        penLabel = tkinter.Label(sideBar, text="Pen is Up")
        penLabel.pack()

        def penUpHandler():
            pass
        penUpButton = tkinter.Button(sideBar, text="Pen Up", command=penUpHandler)
        penUpButton.pack()

        def penDownHandler():
            pass
        penDownButton = tkinter.Button(sideBar, text="Pen Down", command=penDownHandler)
        penDownButton.pack()

        def clickHandler(x, y):
            pass

        screen.onclik(clickHandler)

        def dragHandler(x, y):
            pass

        theTurtle.ondrag(dragHandler)

        def undoHandler():
            pass
        screen.onkeypress(undoHandler, "u")
        screen.listen()


def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)
    drawingApp.mainloop()
    print("Program Execution Completed.")



def main1():
    filename = input("Please enter drawing instructions: ")
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.title("Welcome to the turtle zoo!")

    file = open(filename,"r")
    graphicsCommands = graphics.PyList()

    for line in file:
        text = line.strip()
        commandList = text.split(",")
        command = commandList[0]
        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            cmd = graphics.GoToCommand(x, y, width, color)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            cmd = graphics.CircleCommand(radius, width, color)
        elif command == "beginfill":
            color = commandList[1].strip()
            cmd = graphics.BeginFillCommand(color)
        elif command == "endfill":
            cmd = graphics.EndFillCommand()
        elif command == "penup":
            cmd = graphics.PenUpCommand()
        elif command == "pendown":
            cmd = graphics.PenUpCommand()
        else:
            print("Unknown command found in file: {}".format(command))
        graphicsCommands.appen(cmd)
    for cmd in graphicsCommands:
        cmd.draw(t)

    file.close()
    t.ht() # hide the turtle
    screen.exitonclick()
    print("Program Execution Completed")


if __name__ == "__main__":
    main()
