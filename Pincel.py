class Pincel:

    def __init__(self,x,y,cor,espessura):
        self.__x = x
        self.__y = y
        self.__cor = cor
        self.__espessura = espessura

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def espessura(self):
        return self.__espessura

    @espessura.setter
    def espessura(self, espessura):
        self.__espessura = espessura