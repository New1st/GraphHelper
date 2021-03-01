import unittest
import tkinter
from classes import vertex
from classes import line
from classes import graph

class TestGUI(tkinter.Frame):
    def __init__(self, master, **kw):
        tkinter.Frame.__init__(self, master, **kw)
        self.canvas = tkinter.Canvas()
        self.canvas.pack()
        self.graph = self.create_graph()
        self.graph.canvas = self.canvas
        self.vertex = self.create_vertex()
        self.line = self.create_line(self.vertex)
        self.vertex.vertices = [self.line]

    def create_vertex(self):
        name = "V"
        x = 10
        y = 10
        circle = self.canvas.create_oval(x-5, y+5, x+5, y-5, fill = "#8b90f7")
        label = self.canvas.create_text(x+15, y+15, text=name)
        v = vertex.Vertex(name, x, y, circle, label, None, None, None)
        return v

    def create_line(self, vertex):
        name = "e"
        x = 10
        y = 10
        line_now = self.canvas.create_arc(x-15-5, y+15+5, x+15+5,
                                          y-15-5, start=125, extent=290)
        reference_point = [x, y-15, 0]
        label = self.canvas.create_text(reference_point[0], reference_point[1],
                                        text=name)

        e = line.Line(name, vertex, vertex, reference_point, True, line_now, label,
                      None, None, None)
        return(e)

    def create_graph(self):
        name = "G"
        matrix = []
        g = graph.Graph(name, matrix)
        return g

class TKinterTestCase(unittest.TestCase):
    def setUp(self):
        self.root = tkinter.Tk()
        self.window = TestGUI(self.root)

    def tearDown(self):
        if self.root:
            self.root.destroy()

    def test_is_loop(self):
        self.assertTrue(self.window.line.is_loop())

    def test_belong(self):
        self.assertTrue(self.window.line.belong(self.window.vertex))

    def test_neighborhood(self):
        for i in range(0,40):
            for j in range(0,40):
                self.assertTrue(self.window.graph._check_coordinates_vertex(i, j))



if __name__ == '__main__':
    unittest.main()
