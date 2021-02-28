import tkinter
from classes import vertex
from classes import line

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
        self.select_point_2 = None
        self.select_vertex_2 = None
        self.current_vertex = 1
        self.tip_line = None
        self.current_line= 1
        self.vertices = []
        self.lines = []

    def seted(self):
        """Устанавливает обработку нажатия правой кнопкой мыши"""
        self.canvas.bind('<Button-3>', self._clear_select)
        self.canvas.bind('<Motion>', self._show_line)

    def create_vertex(self, x, y):
        """Создание вершиины

        Проверяется близость нажатия к какой-либо вершине. При подходящей
        удаеленности формируется имя новой вершины, и объекты tkinter.
        Создается объект класса Вернишина, добавляется в список.

        """
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

        self.vertices.append(vertex.Vertex(name, x, y, circle, label, frame))
        self.current_vertex += 1
        return True

    def create_line(self, x, y, directed=False):
        """Создание линии

        Методом self._check_coordinates(x, y, "self") проверяется попадание
        по вершине. Если это первое нажатие(self.select_point == None и
        self.select_vertex == None) - устанавличается точка поверх выбранной
        вершины.Иначе - на основе двух точек(self.select_vertex и vertex)
        строится линия. Входной аргумент directed определяет тип линии.
        Создается объект класса Линия, добавляется в список.

        """
        vertex = self._check_coordinates(x, y, "self")
        name = "e"+str(self.current_line)
        if vertex:
            x = vertex.x
            y = vertex.y

            if self.select_vertex == None and self.select_point == None:
                self.select_vertex = vertex
                self.select_point = self.canvas.create_oval(x-2, y+2, x+2, y-2,
                                                            fill= "#000000")
            else:
                if vertex == self.select_vertex:
                    count = self.count_lines(vertex, vertex)
                    new_line = self.canvas.create_arc(
                        x-15-5*count, y+15+5*count, x+15+5*count,
                        y-15-5*count, start=125, extent=290)

                    lable = self.canvas.create_text(x, y-15-11*count,
                                                    text=name)
                    frame = tkinter.LabelFrame(
                        self.objectbar, text="Петля",
                        bg="#EBEBEB", bd=2, width=160, height=40)
        			# self.frame.bind('<Button-1>', self.delete)
                    frame.pack(anchor = tkinter.NW, side = tkinter.TOP,
                        fill = tkinter.X)

                else:
                    count = self.count_lines(vertex, self.select_vertex)
                    if count == 0:
                        new_line = self.canvas.create_line(
                            self.select_vertex.x, self.select_vertex.y, x, y,
                            arrow=tkinter.LAST if directed else tkinter.NONE,
                            arrowshape=(15,20,3))

                        lable = self.canvas.create_text(
                            (self.select_vertex.x + x)//2,
        					(self.select_vertex.y + y)//2,
                            text=name)
                    elif (self.select_vertex_2 == None and
                            self.select_point_2 == None):
                        self.select_vertex_2 = vertex
                        self.select_point_2 = self.canvas.create_oval(
                            x-2, y+2, x+2, y-2, fill= "#000000")
                        return

                    frame = tkinter.LabelFrame(
                        self.objectbar, text="Дуга" if directed else "Ребро",
                        bg="#EBEBEB", bd=2, width=160, height=40)
        			# self.frame.bind('<Button-1>', self.delete)
                    frame.pack(anchor = tkinter.NW, side = tkinter.TOP,
                        fill = tkinter.X)

                label = tkinter.Label(
                    frame,
                    text=name+" = {"+self.select_vertex.name+", "+vertex.name+"}",
                    justify = tkinter.LEFT, bg = "#EBEBEB")
                label.pack(side = tkinter.LEFT)

                self.current_line += 1
                self.canvas.lift(vertex.obj)
                self.canvas.lift(self.select_vertex.obj)
                self.lines.append(line.Line(name, self.select_vertex, vertex, new_line, label, frame))
                self._clear_select(None)

        elif self.select_vertex != None and self.select_vertex_2 != None:
            new_line = self.canvas.create_line(
                self.select_vertex.x, self.select_vertex.y,
                x, y,
                self.select_vertex_2.x, self.select_vertex_2.y, smooth="true",
                arrow=tkinter.LAST if directed else tkinter.NONE,
                arrowshape=(15,20,3))
            lable = self.canvas.create_text(x, y, text=name)
            frame = tkinter.LabelFrame(
                self.objectbar, text="Дуга" if directed else "Ребро",
                bg="#EBEBEB", bd=2, width=160, height=40)
            frame.pack(anchor = tkinter.NW, side = tkinter.TOP,
                fill = tkinter.X)

            label = tkinter.Label(
                frame,
                text=name+" = {"+self.select_vertex.name+", "+ \
                    self.select_vertex_2.name+"}",
                justify = tkinter.LEFT, bg = "#EBEBEB")
            label.pack(side = tkinter.LEFT)

            self.current_line += 1
            self.canvas.lift(self.select_vertex_2.obj)
            self.canvas.lift(self.select_vertex.obj)
            self.lines.append(line.Line(
                name, self.select_vertex, self.select_vertex_2,
                new_line, label, frame))
            self._clear_select(None)

    def _clear_select(self, event):
        """Очищает выделение вершины"""
        if self.select_point != None:
            self.canvas.delete(self.select_point)
            self.select_point = None
            self.select_vertex = None
        if self.select_point_2 != None:
            self.canvas.delete(self.select_point_2)
            self.select_point_2 = None
            self.select_vertex_2 = None
        if self.tip_line != None:
            self.canvas.delete(self.tip_line)

    def _check_coordinates(self, x, y, mode="neighborhood"):
        """Проверяет соседство(или прямое попадание) с вершиной"""
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

    def count_lines(self, first, second):
        count = 0
        for now in self.lines:
            if (now.first_vertex == first and now.second_vertex == second or
                    now.first_vertex == second and now.second_vertex == first):
                count += 1
        return(count)

    def _show_line(self, event):
        if (self.select_vertex != None and self.select_vertex_2 != None):
            x = self.canvas.canvasx(event.x)
            y = self.canvas.canvasy(event.y)

            if self.tip_line != None:
                self.canvas.delete(self.tip_line)
            self.tip_line = self.canvas.create_line(
                self.select_vertex.x, self.select_vertex.y,
                x, y,
                self.select_vertex_2.x, self.select_vertex_2.y, smooth="true", fill="#808080")
