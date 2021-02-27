import tkinter

class Vertex:


    def __init__(self, name, x, y, tk_canvas_obj, tk_canvas_label, tk_obj_frame):
        self.name = name
        self.x = x
        self.y = y
        self.obj = tk_canvas_obj
        self.label = tk_canvas_label
        self.frame = tk_canvas_label
