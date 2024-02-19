# https://www.pythontutorial.net/tkinter/tkinter-mvc/
import tkinter as tk

from Controller import Controller
from Model import Model
from View import View


class App(tk.Tk):  # App klass on tkinter main window
    def __init__(self):
        super().__init__()  # Tk jaoks
        self.title('Isikukoodi kontroll')

        # Loome mudeli
        model = Model()

        # Loome vaate
        view = View(self)
        view.grid(row=0, column=0, padx=5, pady=5)

        # Loome controlleri (enne peab model ja view olemas olema)
        controller = Controller(model, view)
        # Seadistame controlleri views
        view.set_controller(controller)


# Siin käivitatakse rakendus
if __name__ == '__main__':
    app = App()  # Loo rakendus (tkinter main window)
    app.mainloop()  # Main window (tkinter) vajab lõpus mainloop'i
