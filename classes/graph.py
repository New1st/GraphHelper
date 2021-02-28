import tkinter
from classes import vertex

class Graph:
    """Класс графа"""

    def __init__(self, name, matrix):
        """Конструктор графа """
        self.name = name
        self.matrix = matrix
        self.canvas = None
        self.objectbar = None
        self.select_point = None
        self.select_vertex = None
        self.current_vertex = 1
        self.current_edge = 1
        self.vertices = []
        self.edges = []

    def seted(self):
        """Устанавливает обработку нажатия правой кнопкой мыши"""
        self.canvas.bind('<Button-3>', self._clear_select)

    def create_vertex(self, x, y):
        """Создаёт вершину"""
        if not self._check_coordinates(x, y):
            return False

        name = "V"+str(self.current_vertex)
        circle = self.canvas.create_oval(x-5, y+5, x+5, y-5, fill = "#8b90f7")
        # if text_lock_vertices == False:
        # 	self.lable = canvas.create_text(self.x+15, self.y+15, text=name)
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

    def create_edge(self, x, y, mode):
        """Создание линии"""
        vertex = self._check_coordinates(x, y, "self")
        if self.select_vertex == None and self.select_point == None:
            # Обработка первого нажатия
            if vertex:
                self.select_vertex = vertex
                x = self.select_vertex.x
                y = self.select_vertex.y
                self.select_point = self.canvas.create_oval(x-2, y+2, x+2, y-2, fill = "#000000")
        else:
            if vertex:
                name = "l"+str(self.current_edge)
                if vertex == self.select_vertex:
                    line = self.canvas.create_arc(
                        vertex.x-15, vertex.y+15, vertex.x+15,
                        vertex.y-15, start=125, extent=290)

        			# if text_lock_lines == False:
        			# 	self.lable = canvas.create_text(self.vertex_f.x, self.vertex_f.y-15, text="e"+str(name))
                    self.lable = self.canvas.create_text(vertex.x, vertex.y-15,
                                                    text=name)
                    self.frame = tkinter.LabelFrame(
                        self.objectbar, text = "Петля",
                        bg = "#EBEBEB", bd=2, width = 160, height = 40)
        			# self.frame.bind('<Button-1>', self.delete)
                    self.frame.pack(anchor = tkinter.NW, side = tkinter.TOP,
                        fill = tkinter.X)
                    self._clear_select(None)
                    self.current_edge += 1

    def _clear_select(self, event):
        """Очищает выделение вершины"""
        if self.select_point != None:
            self.canvas.delete(self.select_point)
            self.select_point = None
            self.select_vertex = None

    def _check_coordinates(self, x, y, mode="neighborhood"):
        """Проверяет соседство(прямое попадание) по вершине"""
        if mode == "neighborhood":
            for vertex in self.vertices:
                if (vertex.x >= x - 20 and vertex.x <= x + 20 and
                        vertex.y >= y - 20 and vertex.y <= y + 20):
                    return False
            return True
        elif mode == "self":
            for vertex in self.vertices:
                if (vertex.x >= x - 7 and vertex.x <= x + 7 and
                        vertex.y >= y - 7 and vertex.y <= y + 7):
                    return vertex
            return False
