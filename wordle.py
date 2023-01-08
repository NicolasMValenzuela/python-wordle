from base64 import encode
from random import randint 

def verde(palabra):
    verde = '\033[1;42m'
    nocolor = '\033[1;0m'
    return verde + palabra + nocolor

def amarillo(palabra):
    amarillo = '\033[1;43m'
    nocolor = '\033[1;0m'
    return amarillo + palabra + nocolor

def blanco(palabra):
    blanco = '\33[1;47m'
    nocolor ='\33[1;0m'
    return blanco + palabra + nocolor


def filtro_de_palabra(palabra):

    '''Con esta función leemos la palabra seleccionada y le sacamos las tildes.
    ejemplo: palabra = comisión --> return nueva == comision. 
    '''

    contilde = 'áéíóú'
    sintilde= 'aeiou'
    nueva = ''
    for letra in palabra:
        if letra in contilde:
            posicion = contilde.index(letra)
            nueva= nueva + sintilde[posicion]
        else:
            nueva = nueva + letra
    return nueva



def seleccionador(lista):
    '''Esta función sirve para eliminar elementos repetidos de la lista con las palabras seleccionadas por dificultad
    y elegir de esta lista nueva una palabra random que tenemos que encontrar.
    Recibe lista_juego y devuelve palabra que será pasado como argumento para filtro_de_palabra'''
    lista2 = lista.copy()
    for elemento in lista2:
        while lista2.count(elemento) > 1:
            lista2.remove(elemento)

    palabra = lista2[randint(0, len(lista2))].lower()

    return palabra

def limpiar(texto):
    '''Función que logra quitar los caracteres extraños de las palabras. Ejemplo: texto = hola$ --> newCad == hola.
    recibe las líneas del archivo de texto (linea) y devuelve las palabras crudas'''
    caracteres = '.,?/:;"[]}{=+-_!`><()*&%^#@$'
    newCad = ''
    for i, c in enumerate(texto):
        if c not in caracteres:
            newCad += texto[i]
        elif c in caracteres:
            newCad +=' '

    return newCad

def mostrar_matriz(matriz):
    '''muestra la matriz formateada'''
    for fila in matriz:
        for e in fila:
            print(e, end='')
        print()

def matriz(dificultades):
    filas = 6
    columnas = dificultades
    matriz=[['_'] * columnas for i in range(filas)]
    return matriz

def palabra_ingresada(dificultades):
    '''Acá validamos la palabra que escribe el usuario, para que no contenga errores de tipeo o de caracteres. 
    Ejemplo: ingresa 12345 y no lo deja pasar, al igual que meter una palabra con mas o menos caracteres de los requeridos.
    Se usa en comparador, para ver contra la palabra seleccionada en filtro_de_palabra '''
    while True:  
        try:
            valor = input(f'ingrese la palabra a buscar con {dificultades} letras: ').lower()
            assert len(valor) == dificultades and valor.isalpha()
            break
        except AssertionError:
            print(f'La palabra ingresada debe ser de {dificultades} letras: ')
    return valor


def estado(encontrada):
    '''Devuelve una frase dependiendo de si la palabra se encontró o no'''
    if encontrada == False:
        mensaje = 'Has perdido!'
    else:
        mensaje = 'Has ganado!'
    return mensaje

def letras(valor, palabra, cadena):

    cadena = list(cadena)
    nueva =''
    for i,letra in enumerate(valor):
        if letra == palabra[i]:
            cadena = list(cadena)
            posicion = cadena.index(letra)
            cadena.pop(posicion)
            nueva = verde(valor[i])
            cadena.insert(posicion, nueva)
            cadena = ''.join(cadena)
        elif (letra in palabra) and letra != palabra[i]:
            cadena = list(cadena)
            posicion = cadena.index(letra)
            cadena.pop(posicion)
            nueva = amarillo(valor[i])
            cadena.insert(posicion, nueva)
            cadena = ''.join(cadena)
        elif (letra not in palabra):
            cadena = list(cadena)
            posicion = cadena.index(letra)
            cadena.pop(posicion)
            nueva = blanco(valor[i])
            cadena.insert(posicion, nueva)
            cadena = ''.join(cadena)
    
    return cadena



def comparador(matriz, palabra):
    '''Acá se comparan la palabra ingresada por el usuario con la seleccionada por la máquina 
    Si la ingresada y la buscada coinciden, rompe el bucle y devuelve true (será usado en la función estado), si no y se agotan los valors, devolvera false  '''
    
    encontrada = False
    intentos = 0
    cadena1 = 'abcdefghijklmnñopqrstuvwxyz'
    

    while intentos < 6 and encontrada != True:
        
        valor = filtro_de_palabra(palabra_ingresada(dificultades))
        if valor == palabra: 
            encontrada = True
            break
        
        colored = []
        

        lista_palabra = [palabra[i] for i in range (len(valor))]


        for i in range (len(palabra)):

            colored += ['_']
            if valor[i] == palabra[i]:
                colored[i] = verde(valor[i])
                lista_palabra.remove(valor[i])
    
        for i in range (len(palabra)):

            if valor[i] in palabra and valor[i] in lista_palabra:
                colored[i] = amarillo(valor[i])
                lista_palabra.remove(valor[i])

            elif valor[i] != palabra[i] and valor[i] not in lista_palabra:
                colored[i] = blanco(valor[i])

        for i in range (len(colored)):
            matriz[intentos][i] = colored[i]
            
        print()
        mostrar_matriz(matriz) #--> muestro la matriz renovada con las coincidencias por cada iteración (valor)
        print()
        cadena1= letras(valor, palabra, cadena1)
        print(cadena1)

        intentos +=1
    
    return encontrada


def choice():
    while True:
        try:
            choice = input('Desea volver a jugar? (S/N): ').upper()
            assert choice == 'S' or choice == 'N'
            break
        except AssertionError:
            print('Opción no válida, debe ser S or N')

    return choice


def dificultad(valor = 'seleccione dificultad: "F" para fácil, "M" para medio o "D" para dificil: '):
    '''Devuelve un número entero que representa la cantidad de columnas que tendrá la matriz '''
    while True:
        try:
            valor = input(valor)
            dificultades = 9
            assert valor.upper() == 'F' or valor.upper() =='M' or valor.upper() == 'D'
            if valor.upper() =='F':
                dificultades = randint(5,6)
                break
            if valor.upper() =='M':
                dificultades = randint(7,8)
                break
            if valor.upper() == 'D':
                dificultades == 9
                break
        except AssertionError:
            print('EL valor ingresado debe F para fácil, M para medio o D para dificil, intente nuevamente: ')
    return dificultades

def starter(dificultades):
    lista_juego = []
    for linea in texto:
        linea = linea.rstrip('\n')
        linea = limpiar(linea)
        lista_de_palabras= linea.split()
        for palabra in lista_de_palabras:
            if len(palabra) == dificultades:
                lista_juego.append(palabra)
    
    return lista_juego

def victorias(win,victorias):
    if win =='Has ganado!':
        victorias +=1
        return victorias
    else:
        victorias +=0
        return victorias

def acumulador (win, racha_victorias ):
    if win == 'Has ganado!':
        racha_victorias +=1
        return racha_victorias  
    else:
        racha_victorias  = 0
        return racha_victorias  
    
def racha(maximo_victorias,racha_victorias ):
    
    if maximo_victorias < racha_victorias :
        maximo_victorias = racha_victorias 
        return maximo_victorias
    else:
        return maximo_victorias

def records(victorias, intentos, racha_actual, mejor_racha):
    stats = {
        'Porcentaje de victorias': (victorias/intentos)*100,
        'intentos': intentos,
        'Racha actual': racha_actual,
        'Mejor racha':mejor_racha
    }

    return stats 


try:
    '''Abrimos el texto y la pc elige la palabra '''

    texto = open("texto.txt","rt", encoding = 'utf_8')
    victoria = 0
    racha_victorias  = 0
    maximo_victorias = 0
    intentos = 0
    cadena = 'abcdefghijklmnñopqrstuvwxyz'
    mensaje='Bienvenido a Wordle. \n Las reglas de juego son simples: al ingresar una palabra por teclado, será comparada con una elegida por la pc. \n Cuando la letra se ponga verde, quiere decir que está en la palabra y en la posición correcta. \n Si la letra sale en amarillo, quiere decir que está en la palabra, pero no en la posición. \n Si sale en blanco quiere decir que no existe la letra en la palabra. Tienes hasta 6 valors para adivinar la palabra del día. \n GLHF! \n'


    print(mensaje)

    while True:
        

        dificultades = dificultad()

        palabra = (seleccionador(starter(dificultades)))

        palabra_final = filtro_de_palabra(palabra)

        win = comparador(matriz(dificultades), palabra_final)

        print(estado(win),'\n')

        print('La palabra era :', palabra_final,'\n')

        victoria = victorias(estado(win), victoria)

        racha_victorias  = acumulador (estado(win), racha_victorias )

        maximo_victorias = racha(maximo_victorias, racha_victorias )
        
        intentos +=1

        replay = choice()
        if replay == 'S':
            texto.seek(0)
        else:
            break

    stats = records(victoria, intentos, racha_victorias, maximo_victorias)

    print(stats)

except FileNotFoundError as mensaje:
    print('No se puede abrir el archivo:', mensaje)
except OSError as mensaje:
    print('no se puede leer el archvio: ', mensaje)
finally:
    try:
        texto.close()
    except NameError:
        pass






