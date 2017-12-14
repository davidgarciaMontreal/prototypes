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


class CircleCommand:

    def __init(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)


class BeginFillCommand:

    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()


class EndFillCommand:

    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()


class PenUpCommand:

    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()


class PenDownCommand:

    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()


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