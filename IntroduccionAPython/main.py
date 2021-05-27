from modules.Calculadora import Calculadora
from modules.CalculadoraPro import CalculadoraPro

if __name__ == '__main__':
    print('Pueba Calculadora'.center(50, '-'))
    a = 20
    b = 0

    calc = Calculadora()

    print(calc.suma(a, b))
    print(calc.resta(a, b))
    print(calc.multiplicacion(a, b))
    print(calc.division(a, b))  # Ojo acá!

    print('Pueba CalculadoraPro'.center(50, '-'))
    calc2 = CalculadoraPro()

    print(calc2.suma(a, b))
    print(calc2.resta(a, b))
    print(calc2.multiplicacion(a, b))
    print(calc2.division(a, b))
    print(calc2.raiz_cuadrada(a))
    print(calc2.logaritmo_natural(a))
    print(calc2.potencia(a, 3))

    print('Lectura de txt'.center(50, '-'))


    def read_text(path):
        lines = []
        with open(path) as f:
            lines = f.readlines()
        return lines


    file_dir = 'the-zen-of-python.txt'
    lineas = read_text(file_dir)

    nro = 1
    for linea in lineas:
        print(f'Linea {nro}: {linea}')
        nro += 1

    print('\n', 'Abriendo el txt sin formato'.center(50, '-'))
    print('\n', open(file_dir).readlines())
