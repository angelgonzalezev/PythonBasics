seguir = True
while seguir==True:
    nomUsuario_1=input('Bienvenido, ¿Cómo te llamas?: ')
    edadUsuario_1=int(input('¿Cuantos años tienes?: '))

    nomUsuario_2 = input('¿Cómo se llama tu compa?: ')
    edadUsuario_2 = int(input('¿Cuantos años tiene?: '))

    print('¿Qué quieres comparar?')
    option = int(input('Longitud nombre = 1 ,Edades = 2 '))

    if(option == 1):
        if(len(nomUsuario_1) > len(nomUsuario_2)):
            print(nomUsuario_1 + ' Tiene el nombre más largo')
        elif(len(nomUsuario_1) < len(nomUsuario_2)):
            print(nomUsuario_2 + ' Tiene el nombre más largo')
        else:
            print('Tienen la misma longitud en el nombre')
    elif (option == 2):
        if(edadUsuario_1 > edadUsuario_2):
            print(nomUsuario_1 + ' es mayor')
        elif(edadUsuario_1 < edadUsuario_2):
            print(nomUsuario_2 + ' es mayor')
        else:
            print('Tienen la misma edad')

    continuar = input('¿Quieres seguir jugando?: ')
    if (continuar == 'Y'):
        seguir = True
    else:
        seguir = False
        print('!Hasta pronto!')
