import tkinter

import aboutwindow
import settings

class Main(tkinter.Frame):


    def __init__(self, root):
        super().__init__(root)
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
        help_menu.add_command(label="О программе", command=self.open_about_window)

        self.menu.add_cascade(label="Файл", menu=file_menu)
        self.menu.add_cascade(label="Справка", menu=help_menu)

    def create_toolbar(self):
        toolbar = tkinter.Frame(bg="#f2f2f2", bd=2)
        toolbar.pack(side = tkinter.TOP, fill=tkinter.X, anchor=tkinter.NW)

        self.tools = []
        for dict in settings.TOOLS_SETTINGS_ARRAY:
            self.icon = tkinter.PhotoImage(file=dict["icon"])
            self.tool_button = tkinter.Button(toolbar, bg="#f2f2f2", bd=0, \
                compound=tkinter.TOP, image=self.icon)
            self.tool_button.pack(side=dict["side"])
            self.tools.append(self.tool_button)
		    #self.btn_vertex_mode.bind('<Button-1>', self.set_mode)

    def open_about_window(self):
        global root
        aboutwindow.create(root)

if __name__ == "__main__":
    root = tkinter.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    strVar = tkinter.StringVar()

    app = Main(root)
    app.pack()

    root.title("GraphHelper")
    logo = tkinter.PhotoImage(file="GraphHelper.gif")
    root.tk.call('wm', 'iconphoto', root._w, logo)
    root.geometry(str(screen_width//2) + "x" + str(screen_height//2))
    root.minsize(screen_width//2, screen_height//2)

    root.mainloop()
