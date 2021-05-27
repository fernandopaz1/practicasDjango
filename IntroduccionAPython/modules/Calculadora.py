class Calculadora:
    def __init__(self):
        pass

    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b
        pass

    @staticmethod
    def multiplicacion(a, b):
        return a * b
        pass

    @staticmethod
    def division(a, b):
        return a/b if b != 0 else float('nan')
