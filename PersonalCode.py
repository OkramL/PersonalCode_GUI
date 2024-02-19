"""
Isikukoodi klass (model)
"""


class PersonalCode:
    def __init__(self, personal_code):
        if len(personal_code) == 0:  # Kui isikukoodi pole sisestatud
            raise ValueError('Isikukoodi pole sisestatud.')
        else:  # On sisestatud
            self.__personal_code = personal_code

    # GETTERS
    @property
    def personal_code(self):
        return self.__personal_code
