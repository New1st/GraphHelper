import tkinter

class Main(tkinter.Frame):
    def __init__(self,root):
		super().__init__(root)
        self.create_window()

    def create_window(self):
        self.menu = Menu(self)
        
        toolbar = tkinter.Frame(bg="#f2f2f2", bd=2)
		toolbar.pack(side = tkinter.TOP, fill = tkinter.X, anchor = tkinter.NW)


if __name__ == "__main__":
	root  = tkinter.Tk()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()

	strVar = tkinter.StringVar()

	app = Main(root)
	app.pack()

	root.title("GraphHelper")
	root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file="GraphHelper.gif"))
	root.geometry(str(screen_width//2)+"x"+str(screen_height//2))
	root.minsize(screen_width//2, screen_height//2)

	root.mainloop()
