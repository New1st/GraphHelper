import tkinter

class Main(tkinter.Frame):


    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        self.menu = tkinter.Menu(self, relief="flat")
        root.config(menu=self.menu)

        file_menu = tkinter.Menu(self.menu, tearoff=0, relief="flat")
        file_menu.add_command(label="Создать")
        file_menu.add_command(label="Открыть...")
        file_menu.add_command(label="Сохранить...")
        file_menu.add_command(label="Выход")

        help_menu = tkinter.Menu(self.menu, tearoff=0, relief="flat")
        help_menu.add_command(label="Локальная справка")
        help_menu.add_command(label="О программе")

        self.menu.add_cascade(label="Файл", menu=file_menu)
        self.menu.add_cascade(label="Справка", menu=help_menu)

    def create_toolbar(self):
        toolbar = tkinter.Frame(bg="#f2f2f2", bd=2)
        toolbar.pack(side = tkinter.TOP, fill = tkinter.X, anchor = tkinter.NW)

        self.icon_vertex_mode = tkinter.PhotoImage(file='resources/icons/add_vertex.png')
        self.btn_vertex_mode = tkinter.Button(toolbar, bg="#f2f2f2", bd=0, \
            compound=tkinter.TOP, image = self.icon_vertex_mode)

        self.btn_vertex_mode.pack(side = tkinter.LEFT)
		#self.btn_vertex_mode.bind('<Button-1>', self.set_mode)

if __name__ == "__main__":
	root = tkinter.Tk()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()

	strVar = tkinter.StringVar()

	app = Main(root)
	app.pack()

	root.title("GraphHelper")
	root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file="GraphHelper.gif"))
	root.geometry(str(screen_width//2) + "x" + str(screen_height//2))
	root.minsize(screen_width//2, screen_height//2)

	root.mainloop()
