import tkinter

import aboutwindow
import settings


class Main(tkinter.Frame):


    def __init__(self, root):
        super().__init__(root)
        self.create_menu()
        self.create_toolbar()
        self.create_objectbar()
        self.create_canvas()

    def create_menu(self):
        self.menu = tkinter.Menu(self, relief="flat")
        root.config(menu=self.menu)

        file_menu = tkinter.Menu(self.menu, tearoff=0, relief="flat")
        file_menu.add_command(label="Открыть...")
        file_menu.add_command(label="Сохранить...")
        file_menu.add_command(label="Выход")

        help_menu = tkinter.Menu(self.menu, tearoff=0, relief="flat")
        #help_menu.add_command(label="Локальная справка")
        help_menu.add_command(label="О программе", command=self.open_about_window)

        self.menu.add_cascade(label="Файл", menu=file_menu)
        self.menu.add_cascade(label="Справка", menu=help_menu)

    def create_toolbar(self):
        toolbar = tkinter.Frame(bg="#f2f2f2", bd=3)
        toolbar.pack(side = tkinter.TOP, fill=tkinter.X, anchor=tkinter.NW)

        self.tools = []
        self.icons= []
        i = 0
        for dict in settings.TOOLS_SETTINGS_ARRAY:
            icon = tkinter.PhotoImage(file=dict["icon"])
            self.icons.append(icon)
            self.tool_button = tkinter.Button(
                toolbar, bg="#f2f2f2", bd=0,
                compound=tkinter.TOP, image=self.icons[i],
                highlightthickness=0)
            self.tool_button.pack(side=dict["side"])
            self.tools.append(self.tool_button)
            self.tool_button.bind('<Button-1>', self.gg)
            i+=1

    def create_objectbar(self):
        objectbar = tkinter.LabelFrame(
            text="Объекты:", bg="#EBEBEB", bd=2,
            width=184, relief="flat")
        objectbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        objectbar.pack_propagate(False)

        self.scroll_obj_canvas = tkinter.Canvas(
            objectbar, width=184,
            bg="#EBEBEB", highlightthickness=0)
        self.objectbar = tkinter.Frame(self.scroll_obj_canvas, bg="#EBEBEB", width = 180)

        scrollbar = tkinter.Scrollbar(
            objectbar, orient="vertical",command=self.scroll_obj_canvas.yview,
            relief = "flat")
        self.scroll_obj_canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side = tkinter.RIGHT,fill = tkinter.Y)

        self.scroll_obj_canvas.create_window((0,0),window=self.objectbar, anchor='n')
        self.scroll_obj_canvas.pack_propagate(False)
        self.scroll_obj_canvas.pack(side = tkinter.RIGHT, fill=tkinter.Y)

        self.objectbar.bind("<Configure>", self.config_scroll_objectbar)
		#self.objectbar.bind('<Button-1>', self.update_type)

    def create_canvas(self):
        canvas = tkinter.Canvas(
            root, bg="#ffffff", width=screen_width - 184,
            height = screen_height - 14)
        canvas.pack(side = tkinter.TOP, fill = tkinter.BOTH)

		# self.canvas.bind('<Motion>', self.create_tip_line)
		# self.canvas.bind('<Button-1>', self.canvas_click_left)
		# self.canvas.bind('<Button-3>', self.canvas_click_right)

    def config_scroll_objectbar(self, event):
        self.scroll_obj_canvas.configure(
            scrollregion=self.scroll_obj_canvas.bbox("all"),
            width=200,height=200)

    def open_about_window(self):
        global root
        aboutwindow.create(root)

    def gg(self, event):
        print("aa")

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
    root.geometry(str(screen_width) + "x" + str(screen_height))
    root.minsize(screen_width//2, screen_height//2)

    root.mainloop()
