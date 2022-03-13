import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('elige un numero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequeño')
        numero_elegido = int(input('elige otro numero: '))
    print('¡GANASTES!')


if __name__ == '__main__':
    run()