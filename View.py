from tkinter import ttk, Text, W, END, Scrollbar, EW


class View(ttk.Frame):  # Vaade on Frame mitte main window!
    def __init__(self, parent):
        super().__init__(parent)  # Frame jaoks

        # https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame
        # https://sites.google.com/view/paztronomer/blog/basic/python-colors
        # NB! self on Frame ise antud kontekstis
        self.style = ttk.Style()
        self.style.configure('TFrame', background='lemonchiffon')

        # Silt (Label)
        self.label = ttk.Label(self, text="Sisesta isikukood", background='lemonchiffon')
        self.label.grid(row=1, column=0)

        # Sisestuskast (Entry)
        # TODO Määra sisestuskastile fookus (et kohe saaks kirjutada isikukoodi)
        self.personal_code = ttk.Entry(self)
        self.personal_code.grid(row=1, column=1)

        # Nupp (Button)
        self.button = ttk.Button(self, text="Kontrolli", command=self.button_clicked)
        self.button.grid(row=1, column=2, padx=5, pady=5)

        # Veateade
        self.message_label = ttk.Label(self, text='', foreground='red', background='lemonchiffon')
        self.message_label.grid(row=3, column=0, padx=5, pady=5, columnspan=3, sticky=W)

        # Mitme realine tekstikast (Text) millel on allservas kerimise riba horisontaalis
        self.result = Text(self, width=40, wrap='none')

        # Järgnevad kolm rida on horisnotaalse kerimisriba jaoks "kasti" all servas
        self.vsb = Scrollbar(self, orient='horizontal', command=self.result.xview)
        self.result.configure(xscrollcommand=self.vsb.set)
        self.vsb.grid(row=3, column=0, columnspan=3, sticky=EW)

        self.result.grid(row=2, column=0, columnspan=3, padx=5, pady=5)  # Paneb tekstikasti framele

        # Vaikimisi kohe controllerit pole
        self.controller = None

    def set_controller(self, controller):
        """
        Meetod kontrolleri tegemiseks/loomiseks
        :param controller:
        :return:
        """
        self.controller = controller

    def button_clicked(self):
        """
        Halda nupu klikkimise sündmust. Handle button click event.
        :return:
        """
        if self.controller:
            self.controller.check(self.personal_code.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''

    def show_result(self, pc):
        """
        Siin näitab õige isikukoodi korral infot. Kaasa on antud isikukoodi objekt, kust saab vajalikud info kätte
        :param pc:
        :return:
        """
        self.result.delete('1.0', END)  # Tühjenda tulemuse kast
        self.result.insert(END, pc.personal_code)  # Lisa isikukood tulemus kasti
        # TODO Siia ülejäänud asjad

        self.personal_code.delete(0, END)  # Tühjenda isikukoodi SISESTUS kast
