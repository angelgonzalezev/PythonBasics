# -*- coding:utf-8 -*-
import random #importamos la libreria para generar un numero aleatorio

def run():
    number_found = False
    random_number= random.randint(0,20)  #generamos un numeroaleatorio entre 0 y 20

    while not number_found:
        number= int(input('Intenta un número: '))

        if number==random_number:
            print('Felicidades, encontrastes el número!!')
            number_found= True
        elif number> random_number:
            print('El numero es más pequeño')
        else:
            print('El numero es más grande')


if __name__=='__main__':

    run()
