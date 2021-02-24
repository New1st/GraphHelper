import tkinter

class Vertex:


    def __init__(self, name, tk_canvas_obj, tk_canvas_label, tk_obj_frame):
        self.name = name
        self.obj = tk_canvas_obj
        self.label = tk_canvas_label
        self.frame = tk_canvas_label
        print("New vertex")
