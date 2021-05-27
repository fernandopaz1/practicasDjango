from modules.Calculadora import Calculadora
import numpy as np


class CalculadoraPro(Calculadora):
    def __init__(self):
        pass

    @staticmethod
    def raiz_cuadrada(a):
        return np.sqrt(a)

    @staticmethod
    def logaritmo_natural(a):
        return np.log(a)

    @staticmethod
    def potencia(a, n):
        return a ** n
