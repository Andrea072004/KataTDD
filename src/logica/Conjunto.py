class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto=conjunto

    def promedio( self ):
        if len(self.__conjunto) > 0:
            return sum(self.__conjunto) / len(self.__conjunto)
        else:
            return None

class ConjuntoPonderado:
    def __init__(self, datos, pesos):
        self.__datos = datos
        self.__pesos = pesos

    def promedio_ponderado(self):
        if len(self.__datos) == 0 or len(self.__datos) != len(self.__pesos):
            return None
        else:
            total = sum(dato * peso for dato, peso in zip(self.__datos, self.__pesos))
            total_pesos = sum(self.__pesos)
            return total / total_pesos if total_pesos != 0 else None
