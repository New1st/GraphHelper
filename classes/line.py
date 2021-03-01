import tkinter
from classes import vertex

class Line:


    def __init__(self, name, first_vertex, second_vertex, reference_point,
                 directed, tk_canvas_obj, tk_canvas_label,
                 tk_obj_frame, tk_button, tk_canvas):
        self.name = name
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        self.directed = directed
        self.obj = tk_canvas_obj
        self.label = tk_canvas_label
        self.frame = tk_obj_frame
        self.canvas = tk_canvas
        self.button = tk_button
        self.reference_point = reference_point

    def is_loop(self):
        if self.first_vertex == self.second_vertex:
            return True
        return False

    def belong(self, vertex):
        if self.first_vertex == vertex or self.second_vertex == vertex:
            return True
        return False

    def update(self, count=0):
        self.canvas.delete(self.label)
        self.canvas.delete(self.obj)

        if self.first_vertex != self.second_vertex:
            self.obj = self.canvas.create_line(
                self.first_vertex.x, self.first_vertex.y,
                self.reference_point[0], self.reference_point[1],
                self.second_vertex.x, self.second_vertex.y, smooth="true",
                arrow=tkinter.LAST if self.directed else tkinter.NONE,
                arrowshape=(15,20,3))
        else:
            self.obj = self.canvas.create_arc(
                self.first_vertex.x-15-5*self.reference_point[2],
                self.first_vertex.y+15+5*self.reference_point[2],
                self.first_vertex.x+15+5*self.reference_point[2],
                self.first_vertex.y-15-5*self.reference_point[2],
                start=125, extent=290)
            self.reference_point = [
                self.first_vertex.x,
                self.first_vertex.y-15-11*self.reference_point[2],
                self.reference_point[2]]

        self.canvas.tag_lower(self.obj)
        self.label = self.canvas.create_text(self.reference_point[0],
                                             self.reference_point[1],
                                             text=self.name)
