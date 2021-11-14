class Cor:

    def __init__(self,r,g,b):
        self.__r = r
        self.__g = g
        self.__b = b

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self,r):
        self.__r = r

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def g(self):
        return self.__g

    @g.setter
    def g(self, g):
        self.__g = g