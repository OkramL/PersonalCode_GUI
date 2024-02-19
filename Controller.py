from PersonalCode import PersonalCode


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def check(self, personal_code):
        """
        Kontrollib isikukoodi
        :param personal_code:
        :return:
        """
        try:
            pc = PersonalCode(personal_code)  # Loo isikukoodi objekt
            # Kui õnnestus siis näitab teksti ekraani all servas roheliselt
            self.view.show_success(f'Isikukood {personal_code} olemas, algses variandis.')
            # Lisab isikukoodi (hiljem kogu vajaliku info) result aknasse
            self.view.show_result(pc)
        except ValueError as error:
            # Kui isikukoodi ei õnnestunud luua, siis näitab ekraani all servas punast veateadet
            self.view.show_error(error)
