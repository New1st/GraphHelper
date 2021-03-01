import tkinter

import aboutwindow
import newgraphwindow
import settings
from classes import vertex

class Main(tkinter.Frame):
    """Класс главного окна"""

    def __init__(self, root):
        """Конструктор главного окна

        Вызывает метод инициализации из родительского класса, передавая root.
        Первично устанавливает режим работы приложения.
        Вызвает методы построения условных блоков графики.

        """
        super().__init__(root)
        self.current_graph = None
        self.mode = 0
        self._create_menu()
        self._create_toolbar()
        self._create_objectbar()
        self._create_bottombar()
        self._create_canvas()

    def _create_menu(self):
        """ Построение главного меню"""
        self.menu = tkinter.Menu(self, relief="flat")
        root.config(menu=self.menu)

        file_menu = tkinter.Menu(self.menu, tearoff=0, relief="flat")
        file_menu.add_command(label="Создать граф", command=self.create_new_graph)
        file_menu.add_command(label="Выход", command=root.destroy)

        help_menu = tkinter.Menu(self.menu, tearoff=0, relief="flat")
        # help_menu.add_command(label="Локальная справка")
        help_menu.add_command(label="О программе", command=self.open_about_window)

        self.menu.add_cascade(label="Файл", menu=file_menu)
        self.menu.add_cascade(label="Справка", menu=help_menu)

    def _create_toolbar(self):
        """ Построение панели инструментов"""
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
                highlightthickness=0, state=tkinter.DISABLED)
            self.tool_button.pack(side=dict["side"])
            self.tools.append(self.tool_button)
            self.tool_button.bind('<Button-1>', self.set_mode)
            i+=1

    def _create_objectbar(self):
        """ Построение панели объектов"""
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

    def _create_bottombar(self):
        """ Построение панели состояния"""
        bottombar = tkinter.Frame(bg="#EBEBEB", bd=0, width = 26)
        bottombar.pack(side = tkinter.BOTTOM, fill = tkinter.X, anchor = tkinter.SW)

        message = tkinter.Label(bottombar, text = "Сообщение: ", width = 10, bg = "#EBEBEB")
        message.pack(side = tkinter.LEFT)
        self.message = tkinter.Label(bottombar, fg = "#000000", justify = tkinter.LEFT, bg = "#EBEBEB")
        self.message.pack(side = tkinter.LEFT, fill = tkinter.BOTH)
        self.print_message(settings.MESSAGES["GREETING"])

    def _create_canvas(self):
        """Построение холста"""
        self.canvas = tkinter.Canvas(
            root, bg="#f2f2f2", width=screen_width - 184,
            height = screen_height - 14, state=tkinter.DISABLED)
        self.canvas.pack(side = tkinter.TOP, fill = tkinter.BOTH)
		# self.canvas.bind('<Motion>', self.create_tip_line)
        self.canvas.bind('<Button-1>', self.canvas_click_left)

    def config_scroll_objectbar(self, event):
        """Конфигуратор скролла"""
        self.scroll_obj_canvas.configure(
            scrollregion=self.scroll_obj_canvas.bbox("all"))

    def print_message(self, string):
        """Вывод сообщения с соответствующее поле в панели состояния"""
        self.message["text"] = string
        root.after(2000, self._fading)
        self.fading_coefficient = 0

    def _fading(self):
        """Плавное затухание текста сообщения"""
        arr_1 = ["#1a1a1a", "#585858", "#939393", "#cecece", "#ebebeb"]
        self.message["fg"] = arr_1[self.fading_coefficient]
        self.fading_coefficient+=1

        if self.fading_coefficient == 5:
            self.message["text"] = '\0'
            self.message["fg"] = "#000000"
            self.fading_coefficient=0
            return
        root.after(70, self._fading)

    def create_new_graph(self):
        """Вызов окна создания графа"""
        if self.current_graph == None:
            newgraphwindow.NewGraphWindow(self)
        else:
            self.print_message(settings.MESSAGES["WARNING_CREATE"])

    def open_about_window(self):
        """Вызов окна с информацией"""
        aboutwindow.AboutWindow(root)

    def set_mode(self, event):
        """Установка режима работы приложения"""
        for i in range(0, len(self.tools)):
            if (event.widget == self.tools[i]):
                self.current_graph.clear_select(None)
                self.mode = i+1

    def set_graph(self, graph):
        """Установка полученного из NewGraphWindow графа"""
        graph.canvas = self.canvas
        graph.objectbar = self.objectbar
        self.current_graph = graph
        self.current_graph.seted()
        self.current_graph.build()

        for tool in self.tools:
            tool["state"] = tkinter.NORMAL
        self.canvas["state"] = tkinter.NORMAL
        self.canvas["bg"] = "#ffffff"

    def canvas_click_left(self, event):
        """Обработка нажатия левой кнопкой мыши по области холста"""
        if self.mode == 1:
            if not self.current_graph.moved(event.x, event.y):
                self.print_message(settings.MESSAGES["WARNING_MOVE_LOOP"])
        elif self.mode == 2:
            if not self.current_graph.create_vertex(event.x, event.y):
                self.print_message(settings.MESSAGES["WARNING_TOO_CLOSE"])
        elif self.mode == 3 or self.mode == 4:
            self.current_graph.create_line(event.x, event.y,
                                           True if self.mode == 4 else False)
        elif self.mode == 5:
            self.current_graph.merging_vertices(event.x, event.y)


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
