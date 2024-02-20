"""
Isikukoodi klass (model)
"""
from Hospital import Hospital


class PersonalCode:
    def __init__(self, personal_code):
        # TODO Siia defineeri vajalikud klassisisesed muutujad hiljem ka GETTERID!
        self.__personal_code = None  # Algselt isikukoodi pole

        if len(personal_code) == 0:  # Kui isikukoodi pole sisestatud
            raise ValueError('Isikukoodi pole sisestatud.')
        else:  # On sisestatud
            self.__personal_code = personal_code  # Siit saadakse midagi isikukoodiks

    # GETTERS
    @property
    def personal_code(self):
        return self.__personal_code

    @staticmethod
    def get_hospitals():
        result = [Hospital('001-010', 'Kuressaare haiga'),
                  Hospital('011-019', 'Tartu Ülikooli Naistekliinik'),
                  Hospital('021-150', 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'),
                  Hospital('151-160', 'Keila haigla'),
                  Hospital('161-220', 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'),
                  Hospital('221-270', 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'),
                  Hospital('271-370', 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'),
                  Hospital('371-420', 'Narva haigla'),
                  Hospital('421-470', 'Pärnu haigla'),
                  Hospital('471-490', 'Haapsalu haigla'),
                  Hospital('491-520', 'Järvamaa haigla (Paide)'),
                  Hospital('521-570', 'Rakvere haigla, Tapa haigla'),
                  Hospital('571-600', 'Valga haigla'),
                  Hospital('601-650', 'Viljandi haigla'),
                  Hospital('651-700', 'Lõuna-Eesti haigla (Võru), Põlva haigla'),
                  Hospital('701-990', 'Välismaalane')]

        return result
