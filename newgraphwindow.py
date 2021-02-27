import tkinter
import tkinter.messagebox
import settings
from classes import graph

class NewGraphWindow(tkinter.Toplevel):

    def __init__(self, master):
        tkinter.Toplevel.__init__(self, master)
        self["bg"] = "#f2f2f2"
        self.minsize(200, 300)
        self.geometry("400x300")
        self.title("Создание графа")
        self.resizable(False, False)
        self._create_window()

    def _create_window(self):
        name_frame = tkinter.LabelFrame(
            self, bg="#f2f2f2", bd=5, text="Имя графа:",
            width=184, relief="flat")
        name_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        self.name = tkinter.StringVar()
        self.name.set("Новый граф")
        name_block = tkinter.Entry(name_frame, textvariable=self.name)
        name_block.pack(side=tkinter.TOP, fill=tkinter.X)

        text_frame = tkinter.LabelFrame(
            self, bg="#f2f2f2", bd=5,
            text="Матрица инцидентности:", relief="flat")
        text_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        self.text_field = tkinter.Text(
            text_frame, bg="#ffffff", height=13,
            highlightthickness=0, wrap="none")
        self.text_field.pack(side=tkinter.TOP, fill=tkinter.X)
        self.text_field.bind("<Key>", self._check_keys)

        bottom_frame = tkinter.Frame(self, bg="#f2f2f2", bd=10)
        bottom_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        button = tkinter.Button(
            bottom_frame, text="Ок", bg="#f2f2f2",
            relief="groove", highlightthickness=0, command=self._check_text)
        button.pack(side=tkinter.RIGHT)
        button = tkinter.Button(
            bottom_frame, text="Отмена", bg="#f2f2f2",
            relief="groove", highlightthickness=0, command=self.destroy)
        button.pack(side=tkinter.RIGHT)

    def _check_keys(self, event):
        if (event.char not in settings.ALLOWED_CHARACTERS and
                event.keysym != "BackSpace" and event.keysym != "Return"):
            return "break"

    def _check_text(self):
        text = self.text_field.get("%d.%d" % (1,0), tkinter.END)

        matrix = list(list())
        bufer = text.split("\n")
        for i in bufer:
            j = i.split(" ")
            list(filter(("").__ne__, j))
            matrix.append(j)

        list(filter(([" "]).__ne__, matrix))

        print("f")
        print(matrix)

        for i in range(1, len(matrix)):
            if len(matrix[i-1]) != len(matrix[i]):
                return self._error()
        try:
            if len(matrix) != 0:
                for i in range(0, len(matrix[0])):
                    count = 0
                    for j in range(0, len(matrix)):
                        count += abs(int(matrix[j][i]))
                    if count != 2:
                        return self._error()
        except ValueError:
            pass

        return self._accept(matrix)

    def _error(self):
        tkinter.messagebox.showerror("Ошибка",
                                     "В записи матрицы допущена ошибка.")

    def _accept(self, matrix):
        print("TUT")
        self.master.set_graph(graph.Graph(self.name.get(), matrix))
        self.destroy()
