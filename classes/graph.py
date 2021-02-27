import tkinter
from classes import vertex

class Graph:


    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix
        self.canvas = None
        self.objectbar = None
        self.current_vertex = 1
        self.current_edge = 1
        self.vertices = []
        self.edges = []

    def create_vertex(self, x, y):
        if self._check_coordinates(x, y) == False:
            return False

        name = "V"+str(self.current_vertex)
        circle = self.canvas.create_oval(x-5, y+5, x+5, y-5, fill = "#8b90f7")
        # if text_lock_vertices == False:
        # 	self.lable = canvas.create_text(self.x+15, self.y+15, text="V"+str(self.number))
        label = self.canvas.create_text(x+15, y+15, text=name)

        frame = tkinter.LabelFrame(self.objectbar, text="Вершина", bg="#EBEBEB",
                                   bd=2, width = 160, height = 40)
        # self.frame.bind('<Button-1>', self.treatment)
        frame.pack(anchor = tkinter.NW, side = tkinter.TOP, fill=tkinter.X)
        frame.pack_propagate(False)

        name_block = tkinter.Label(frame, justify = tkinter.LEFT, text = name,
                                   bg = "#EBEBEB")
        name_block.pack(side = tkinter.LEFT)
        comment_block = tkinter.Label(frame, justify=tkinter.LEFT,
                                      text="("+str(x)+";"+str(y)+")",
                                      width=15, bg="#EBEBEB")
        comment_block.pack(side = tkinter.RIGHT)

        new_vertex = vertex.Vertex(name, x, y, circle, label, frame)
        self.vertices.append(new_vertex)
        self.current_vertex += 1
        return True

    def _check_coordinates(self, x, y):
        for vertex in self.vertices:
            if (vertex.x >= x - 20 and vertex.x <= x + 20 and
                    vertex.y >= y - 20 and vertex.y <= y + 20):
                return False
        return True
