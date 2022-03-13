#def imprimir_mensaje():
#    print('Mensaje especial: ')
#    print('¡Estoy aprendiendo a usar funciones!')


#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

#PARAMETROS

def conversacion(mensaje):
    print('hola')
    print('como estas')
    print(mensaje)
    print('adios')


opcion = int(input('Elige una opcion (1, 2, 3): '))
if opcion == 1:
    conversacion('Elegistes la opcion 1')
elif opcion == 2:
    conversacion('Elegistes la opcion 2')
elif opcion == 3:
    conversacion('Elegistes la opcion 3')
else:
    print('Escribe la opcion correcta')