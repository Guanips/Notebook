import time


print('que deseas hacer? ')
print('1 crear un archivo')
print('2 editar un archivo')
print('3 ver un archivo')
OP = int(input('ingrese su eleccion a continuacion: '))

if OP == 1:
    nomar = str(input('muy bien cual sera el nombre del archivo? ')) #nomar = nombre archivo
    ext = str(input('y que tipo de archivo sera? '))                #ext = extension
    fultype = nomar + ext                                          #fultype = el nombre del archivo completo que se va a usar
    file = open(fultype, 'w+')
    OP2 = str(input('archivo creado, desea editar este archivo? s/n'))
    if OP2 == 's':
        text = input('ingrese a continuacion lo que desea almacenar: ')
        file.write(text)
        print('operacion exitosa adios....')
        time.sleep(0.75)
        print('.')
        time.sleep(0.75)
        print('.')
        time.sleep(0.75)
        print('.')
        time.sleep(0.75)
    elif OP2 == 'n':
        print('bueno......hasta luego')
        time.sleep(0.75)
        print('.')
        time.sleep(0.75)
        print('.')
        time.sleep(0.75)
        print('.')
        time.sleep(0.75)
else:
    if OP == 2:
        print('OJO se reemplazara todo el contenido del documento eh asi que ojo..... seguro que quieres continuar? s/n')
        des = str(input())                  #des = desicion (es una fiesta de variables pero bueno)
        if des == 's':
            time.sleep(1)
            nomar = str(input('muy bien, cual es el nombre del archivo?: '))
            text = str(input('y que desea agregar al documento: '))
            file = open(nomar, 'w+')
            file.write(text)
            print('muy bien ya esta hecho')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
        else:
            print('muy bien no hay problema adios!')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
    else:
        if OP == 3:
            nomar = str(input('cual es el nombre del archivo que deseas abrir?: '))
            file = open(nomar, "r")
            content = file.read()
            print('el archivo dice lo siguiente')
            time.sleep(0.5)
            print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
            print('')
            print(content)
            print('')
            print('↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑')
            time.sleep(2)
            print('listo adios!')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)

        else:
            print('/ERROR/ opcion no valida, cerrando programa')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)
            print('.')
            time.sleep(0.75)

print('fin del programa')