import tkinter
import settings


class AboutWindow(tkinter.Toplevel):


    def __init__(self):
        super().__init__(root)
        self["bg"] = "#f2f2f2"
        self.minsize(400, 300)
        self.geometry("400x300")
        self.resizable(False, False)
        self._create_window()

    def _create_window(self):
        frame = tkinter.Frame(self, bg="#f2f2f2", bd=10)
        frame.pack(side=tkinter.TOP, fill=tkinter.X)

        self.image = tkinter.PhotoImage(file="GraphHelper.png")
        logo = tkinter.Label(frame, bg="#f2f2f2", justify=tkinter.LEFT, \
            height=50, width=50, image=self.image)
        logo.pack(side=tkinter.LEFT)

        lable = tkinter.Label(frame, text="GraphHelper", justify=tkinter.LEFT, \
            font="14", bg="#f2f2f2")
        lable.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=5, pady=(5,0))
        lable = tkinter.Label(frame, text="Версия: "+settings.VERSION, \
            justify=tkinter.LEFT, bg="#f2f2f2")
        lable.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=5)

        self.frame = tkinter.Frame(self, bg="#f2f2f2")
        self.frame.pack(side=tkinter.TOP, fill=tkinter.X, padx=10)

        self.buttons = []
        self.keys = ["О программе", "Библиотеки", "Автор"]
        self.dictionary = {self.keys[0]: "Приложение для работы с графами, их построения и выполнения ряда операций над ними.", \
            self.keys[1]: "При создании использовались:\n•tkinter", self.keys[2]: "Сергей Звягин"}
        self._create_buttons(self.keys)

        self.text_field = tkinter.Text(self, bg="#ffffff", height=10, highlightthickness=0)
        self.text_field.pack(side=tkinter.TOP, fill=tkinter.X, padx=10)
        self.text_field.insert("%d.%d" % (1,0), self.dictionary[self.keys[0]])

    def _create_buttons(self, list_):
        for i in list_:
            button = tkinter.Button(self.frame, text=i, bg="#f2f2f2", \
                relief="flat", highlightthickness=0)
            button.pack(side=tkinter.LEFT)
            button.bind('<Button-1>', self._button_activated)
            if i == self.keys[0]:
                button["bg"]="#ececec"
            self.buttons.append(button)

    def _button_activated(self, event):
        for i in self.buttons:
            if i is event.widget:
                i["bg"]="#ececec"
            else:
                i["bg"]="#f2f2f2"

        self.text_field.delete("%d.%d" % (1,0), tkinter.END)
        self.text_field.insert("%d.%d" % (1,0), self.dictionary[event.widget["text"]])

def create(arg):
    global root
    root = arg
    Top = AboutWindow()
