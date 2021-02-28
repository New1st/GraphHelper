import tkinter
from classes import vertex

class Line:


    def __init__(self, name, first_vertex, second_vertex,
                 tk_canvas_obj, tk_canvas_label, tk_obj_frame):
        self.name = name
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        self.obj = tk_canvas_obj
        self.label = tk_canvas_label
        self.frame = tk_canvas_label

    def belong(self, vertex):
        if self.first_vertex == vertex or self.second_vertex == vertex:
            return True
        return False
