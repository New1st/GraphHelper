import tkinter

class Vertex:


    def __init__(self, name, x, y, tk_canvas_obj, tk_canvas_label, tk_obj_frame,
                 tk_button, tk_canvas):
        self.name = name
        self.x = x
        self.y = y
        self.obj = tk_canvas_obj
        self.label = tk_canvas_label
        self.frame = tk_obj_frame
        self.button = tk_button
        self.canvas = tk_canvas

    def update(self):
        self.canvas.delete(self.label)
        self.canvas.delete(self.obj)
        self.obj = self.canvas.create_oval(self.x-5, self.y+5, self.x+5,
                                           self.y-5, fill="#8b90f7")
        self.label = self.canvas.create_text(self.x+15, self.y+15,
                                             text=self.name)
