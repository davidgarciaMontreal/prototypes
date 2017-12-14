class GoToCommand:

    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    def __str__(self):
        cmdstr = '<Command x="{}" y="{}" width="{}" color="{}" >Goto</Command>'
        return cmdstr.format(self.x, self.y, self.width, self.color)


class CircleCommand:

    def __init(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)

    def __str__(self):
        cmdstr = '<Command radius="{}" width="{}" color="{}" >Circle</Command>'
        return cmdstr.format(self.radius, self.width, self.color)


class BeginFillCommand:

    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        cmdstr = '<Command color="{}">BeginFill</Command>'
        return cmdstr.format(self.color)


class EndFillCommand:

    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()

    def __str__(self):
        cmdstr = '<Command>EndFill</Command>'
        return cmdstr


class PenUpCommand:

    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        cmdstr = '<Command>PenUp</Command>'
        return cmdstr


class PenDownCommand:

    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        cmdstr = '<Command>PenDown</Command>'
        return cmdstr


class PyList:

    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def __iter__(self):
        for c in self.items:
            yield c

    def removeLast(self):
        self.items = self.items[:-1]
