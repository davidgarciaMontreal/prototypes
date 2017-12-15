from drawing import DrawingApplication
import tkinter
import graphics

class MyDrawingApplication(DrawingApplication):

    def __init__(self, master=None):
        super().__init__(master)
        self.addNewShape()

    def addNewShape(self):
        sideBar = self.sideBar
        theTurtle = self.theTurtle
        screen = self.screen
        radiusLabel = tkinter.Label(sideBar, text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar, textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()

        def circleHandler():
            cmd = graphics.CircleCommand(float(radiusSize.get()), float(1), 'black')
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()
        circleButton = tkinter.Button(sideBar, text="Draw Circle2", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)
def main():
    root = tkinter.Tk()
    drawingApp = MyDrawingApplication(root)
    drawingApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()