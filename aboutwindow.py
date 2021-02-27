import tkinter
import settings


class AboutWindow(tkinter.Toplevel):


    def __init__(self, master):
        tkinter.Toplevel.__init__(self, master)
        self["bg"] = "#f2f2f2"
        self.minsize(400, 300)
        self.geometry("400x300")
        self.resizable(False, False)
        self._create_window()

    def _create_window(self):
        header_frame = tkinter.Frame(self, bg="#f2f2f2", bd=10)
        header_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        self.image = tkinter.PhotoImage(file="GraphHelper.png")
        logo = tkinter.Label(
            header_frame, bg="#f2f2f2", justify=tkinter.LEFT,
            height=50, width=50, image=self.image)
        logo.pack(side=tkinter.LEFT)

        lable = tkinter.Label(
            header_frame, text="GraphHelper",
            justify=tkinter.LEFT, font="14", bg="#f2f2f2")
        lable.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=5, pady=(5,0))
        lable = tkinter.Label(
            header_frame, text="Версия: "+settings.VERSION,
            justify=tkinter.LEFT, bg="#f2f2f2")
        lable.pack(side=tkinter.TOP, anchor=tkinter.NW, padx=5)

        self.buttons_frame = tkinter.Frame(self, bg="#f2f2f2")
        self.buttons_frame.pack(side=tkinter.TOP, fill=tkinter.X, padx=10)

        self.buttons = []
        self.keys = ["О программе", "Библиотеки", "Автор"]
        self.dictionary = {
            self.keys[0]: settings.ABOUT_STRINGS[0],
            self.keys[1]: settings.ABOUT_STRINGS[1],
            self.keys[2]: settings.ABOUT_STRINGS[2]
            }
        self._create_buttons(self.keys)

        self.text_field = tkinter.Text(
            self, bg="#ffffff", height=10,
            highlightthickness=0)
        self.text_field.pack(side=tkinter.TOP, fill=tkinter.X, padx=10)
        self.text_field.insert("%d.%d" % (1,0), self.dictionary[self.keys[0]])
        self.text_field.config(state=tkinter.DISABLED)

        bottom_frame = tkinter.Frame(self, bg="#f2f2f2", bd=10)
        bottom_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        button = tkinter.Button(
            bottom_frame, text="Закрыть", bg="#f2f2f2",
            relief="groove", highlightthickness=0, command=self.destroy)
        button.pack(side=tkinter.RIGHT)

    def _create_buttons(self, list_):
        for i in list_:
            button = tkinter.Button(
                self.buttons_frame, text=i, bg="#f2f2f2",
                relief="groove", highlightthickness=0)
            button.pack(side=tkinter.LEFT)
            button.bind('<Button-1>', self._button_activated)
            if i == self.keys[0]:
                button["bg"] = "#ececec"
            self.buttons.append(button)

    def _button_activated(self, event):
        for i in self.buttons:
            if i is event.widget:
                i["bg"] = "#ececec"
            else:
                i["bg"] = "#f2f2f2"

        self.text_field.config(state=tkinter.NORMAL)
        self.text_field.delete("%d.%d" % (1,0), tkinter.END)
        self.text_field.insert("%d.%d" % (1,0), self.dictionary[event.widget["text"]])
        self.text_field.config(state=tkinter.DISABLED)
