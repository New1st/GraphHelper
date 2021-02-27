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
        name = "V"+str(self.current_vertex)
        circle = self.canvas.create_oval(x-5, y+5, x+5, y-5, fill = "#8b90f7")
        # if text_lock_vertices == False:
        # 	self.lable = canvas.create_text(self.x+15, self.y+15, text="V"+str(self.number))
        label = self.canvas.create_text(x+15, y+15, text=name)

        frame = tkinter.LabelFrame(self.objectbar, text = "Вершина", bg = "#EBEBEB", bd=2, width = 160, height = 40)
        # self.frame.bind('<Button-1>', self.treatment)
        frame.pack(anchor = tkinter.NW, side = tkinter.TOP, fill = tkinter.X)
        frame.pack_propagate(False)

        new_vertex = vertex.Vertex(name, x, y, circle, label, frame)
        self.vertices.append(new_vertex)
        self.current_vertex += 1
        # self.name_block = tkinter.Label(self.frame, justify = tkinter.LEFT, text = self.name, bg = "#EBEBEB")
        # self.name_block.pack(side = tkinter.LEFT)
        # self.name_block.bind('<Button-1>', self.treatment)
        # self.comment_block = tkinter.Label(self.frame, justify = tkinter.LEFT, text = self.comment ,width = 15, bg = "#EBEBEB")
        # self.comment_block.pack(side = tkinter.RIGHT)
