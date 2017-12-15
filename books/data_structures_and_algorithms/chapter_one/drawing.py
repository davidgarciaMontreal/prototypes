import turtle
import graphics
import tkinter
import tkinter.filedialog
import xml


class DrawingApplication(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.graphicsCommands = graphics.PyList()
        self.master.title("Draw")
        self.bar = tkinter.Menu(self.master)
        self.fileMenu = tkinter.Menu(self.bar, tearoff=0)
        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)
        self.theTurtle = turtle.RawTurtle(canvas)
        self.screen = self.theTurtle.getscreen()
        self.buildWindow()

    def buildWindow(self):
        bar = self.bar
        fileMenu = self.fileMenu

        def newWindow():
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = graphics.PyList()

        fileMenu.add_command(label="New", command=newWindow)

        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)
            graphicsCommandsElement = xmldoc.\
                getElementsByTagName("GraphicsCommands")[0]
            graphicsCommands = graphicsCommandsElement.getElementsByTagName(
                "Command")

            for commandElement in graphicsCommands:
                print(type(commandElement))
                command = commandElement.firstChild.data.strip()
                attr = commandElement.attributes

                if command == "goto":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = graphics.GoToCommand(x, y, width, color)
                elif command == "circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = graphics.CircleCommand(radius, width, color)
                elif command == "beginfill":
                    color = attr["color"].value.strip()
                    cmd = graphics.BeginFillCommand(color)
                elif command == "endfill":
                    cmd = graphics.EndFillCommand()
                elif command == "penup":
                    cmd = graphics.PenUpCommand()
                elif command == "pendown":
                    cmd = graphics.PenUpCommand()
                else:
                    raise RuntimeError(
                        "Unknown command found in file: {}".format(command))
            self.graphicsCommands.append(cmd)

        def loadFile():
            filename = tkinter.filedialog.askopenfilename(
                title="Select a Graphics File")
            newWindow()
            self.graphicsCommands = graphics.PyList()
            parse(filename)
            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)
            screen.update()
        fileMenu.add_command(label="Load...", command=loadFile)

        def addToFile():
            filename = tkinter.filedialog.askopenfilename(
                title="Select a Graphics File")
            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            theTurtle.pencolor("#000000")
            theTurtle.fillcolor("#000000")
            cmd = graphics.PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = graphics.GoToCommand(0, 0, 1, "#000000")
            self.graphicsCommands.append(cmd)
            cmd = graphics.PenDownCommand()
            self.graphicsCommands.append(cmd)
            screen.update()
            parse(filename)
            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)
            screen.update()
        fileMenu.add_command(label="Load Into...", command=addToFile)

        def write(filename):
            if not filename:
                return
            file = open(filename, "w")
            msg = '< ?xml version = "1.0" encoding = ' \
                  '"UTF-8" standalone = "no" ? > \n'
            file.write(msg)
            file.write('<GraphicsCommands>\n')
            for cmd in self.graphicsCommands:
                file.write('    ' + str(cmd) + "\n")
            file.write('</GraphicsCommands>\n')
            file.close()

        def saveFile():
            filename = tkinter.filedialog.asksaveasfilename(
                title="Save Picture As...")
            write(filename)
        fileMenu.add_command(label="Save As...", command=saveFile)

        fileMenu.add_command(label="Exit", command=self.master.quit)

        bar.add_cascade(label="File", menu=fileMenu)

        self.master.config(menu=bar)
        theTurtle = self.theTurtle
        screen = self.screen

        screen.tracer(0)

        sideBar = tkinter.Frame(self, padx=5, pady=5)
        self.sideBar = sideBar
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
            cmd = graphics.CircleCommand(
                float(radiusSize.get()), float(widthSize.get()),
                penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()
        circleButton = tkinter.Button(
            sideBar, text="Draw Circle", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)

        screen.colormode(255)
        penLabel = tkinter.Label(sideBar, text="Pen Color")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar, textvariable=penColor)
        penEntry.pack()
        penColor.set("#000000")

        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color is not None:
                penColor.set(str(color)[-9:-2])

        penColorButton = tkinter.Button(
            sideBar, text="Pick Pen Color", command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)

        fillLabel = tkinter.Label(sideBar, text="Fill Color")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar, textvariable=fillColor)
        fillEntry.pack()
        fillColor.set("#000000")

        def getFillColor():
            color = tkinter.colorchooser.askcolor()
            if color is not None:
                fillColor.set(str(color)[-9:-2])
        fillColorButton = \
            tkinter.Button(sideBar, text="Pick Fill Color",
                           command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH)

        def beginFillHandler():
            cmd = graphics.BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        beginFillButton = tkinter.Button(
            sideBar, text="Begin Fill", command=beginFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH)

        def endFillHandler():
            cmd = graphics.EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
        endFillButton = tkinter.Button(
            sideBar, text="End Fill", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)

        penLabel = tkinter.Label(sideBar, text="Pen is Up")
        penLabel.pack()

        def penUpHandler():
            cmd = graphics.PenUpCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Up")
            self.graphicsCommands.append(cmd)
        penUpButton = tkinter.Button(
            sideBar, text="Pen Up", command=penUpHandler)
        penUpButton.pack()

        def penDownHandler():
            cmd = graphics.PenDownCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Down")
            self.graphicsCommands.append(cmd)
        penDownButton = tkinter.Button(
            sideBar, text="Pen Down", command=penDownHandler)
        penDownButton.pack()

        def clickHandler(x, y):
            cmd = graphics.GoToCommand(x, y, widthSize.get(), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()
        screen.onclick(clickHandler)

        def dragHandler(x, y):
            cmd = graphics.GoToCommand(x, y, widthSize.get(), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        theTurtle.ondrag(dragHandler)

        def undoHandler():
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0, 0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
        screen.onkeypress(undoHandler, "u")
        screen.listen()


def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)
    drawingApp.mainloop()
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
