import tkinter

class NewGraphWindow(tkinter.Toplevel):

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
            relief="flat", highlightthickness=0, command=self.destroy)
        button.pack(side=tkinter.RIGHT)
