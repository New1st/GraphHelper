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
        self._create_buttons(["О программе", "Библиотеки", "Автор"])

        self.text_field = tkinter.Text(self, bg="#ffffff", height=10, highlightthickness=0)
        self.text_field.pack(side=tkinter.TOP, fill=tkinter.X, padx=10)

    def _create_buttons(self, list_):
        for i in list_:
            button = tkinter.Button(self.frame, text=i, bg="#f2f2f2", \
                relief="flat", highlightthickness=0)
            button.pack(side=tkinter.LEFT)
            button.bind('<Button-1>', self._button_activated)
            if i == "О программе":
                button["bg"]="#ececec"
            self.buttons.append(button)

    def _button_activated(self, event):
        for i in self.buttons:
            if i is event.widget:
                i["bg"]="#ececec"
            else:
                i["bg"]="#f2f2f2"

        # frame = tkinter.Frame(self, bg="#f2f2f2", bd=4)
        # frame.pack(side=tkinter.TOP, fill=tkinter.X, anchor=tkinter.NW)
        # image = tkinter.PhotoImage(file="GraphHelper.gif")
        #
        #
        #
        # logo = tkinter.Label(frame, text="Блять", image=image)
        # logo.pack(side=tkinter.LEFT)


def create(arg):
    global root
    root = arg
    Top = AboutWindow()
