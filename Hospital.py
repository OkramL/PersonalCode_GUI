"""
Haigla mudel. 421-470', 'Pärnu haigla' saada kse kätte nii algus kui lõpp number ning haigla nime
"""


class Hospital:
    def __init__(self, codes, name):
        self.__codes = codes
        self.__name = name
        self.__start = int(codes.split('-')[0])
        self.__end = int(codes.split('-')[1])

    @property
    def get_codes(self):
        return self.__codes

    @property
    def get_name(self):
        return self.__name

    @property
    def get_start(self):
        return self.__start

    @property
    def get_end(self):
        return self.__end
