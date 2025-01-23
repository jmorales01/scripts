# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
def invertir_texto(texto):
    return texto[::-1]



# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# letra_inicio = "R"
def reorganizar_texto_por_letra(texto, letra_inicio):
   
    letras = list(texto)
    try:
        indice = letras.index(letra_inicio)
    except ValueError:
        return texto
    
    letras_reorganizadas = letras[indice:] + letras[:indice]
    resultado = ''.join(letras_reorganizadas)
    return resultado



# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# desplazamiento = 35
# is_spaces = [False,True]  # False: no hay espacios en el texto, True: hay espacios en el texto
def julio_cesar(texto, desplazamientos, is_spaces=False):
    letras = list(texto)
    dplz = list(map(int, desplazamientos))
    resultado = []

    desplazamiento_index = 0
    es_primer_ciclo = True

    while letras:  # Continuar mientras queden letras en la lista
        desplazamiento = dplz[desplazamiento_index % len(dplz)]
        desplazamiento_index += 1

        if es_primer_ciclo:
            desplazamiento += 1
            es_primer_ciclo = False
        
        if is_spaces:
            posicion_actual = desplazamiento % len(letras)
        else:
            posicion_actual = (desplazamiento - 1) % len(letras)

        nueva_letra = letras.pop(posicion_actual)
        resultado.append(nueva_letra)

        letras = letras[posicion_actual:] + letras[:posicion_actual]

    return ''.join(resultado)



# texto = "MJCHEFPTUDRSOZQYNWBAXVKILG"
# clave = "35768942"
# claveordenada = "23456789234567892345678935"
def trasposicion(texto, clave, claveordenada):

    columnas = len(clave)
    filas = [texto[i:i + columnas] for i in range(0, len(texto), columnas)]

    # Crear la matriz
    matriz = []
    for fila in filas:
        objetos = [{"claveordenada": claveordenada[i], "texto": fila[i]} for i in range(len(fila))]
        matriz.append(objetos)
    
    resultado = []
    for fila in matriz:
        fila_ordenada = sorted(fila, key=lambda x: int(x["claveordenada"]))
        resultado.append("".join(obj["texto"] for obj in fila_ordenada))
    
    texto_cifrado = "".join(resultado)
    return texto_cifrado.strip()



# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# clave = "8256"
# claveordenada = "82645"
def trama(texto, clave, claveordenada):

    longitud_clave = len(clave)
    grupo_size, resto = divmod(len(texto), longitud_clave)
  
    diccionario = {}
    inicio = 0
    for i in range(longitud_clave):
        fin = inicio + grupo_size 
        diccionario[clave[i]] = texto[inicio:fin]
        inicio = fin

    resultado = "".join([diccionario[numero] for numero in claveordenada])
    resultado = resultado + texto[-resto:]
    return resultado



# texto = "RQPOÑNMLKJIHGFEDCBAZYXWVUTS"
# clave = "695472"
# patron = "IDI"
def IDI(texto, clave, patron):
 
    clave = list(map(int, clave))
    patron = list(patron)

    diccionario = []
    clave_idx = 0
    patron_idx = 0

    for letra in texto:
        fila = [letra, clave[clave_idx], patron[patron_idx]]
        diccionario.append(fila)

        clave_idx = (clave_idx + 1) % len(clave)
        patron_idx = (patron_idx + 1) % len(patron)

    nuevo_texto = ""
    posiciones_usadas = set()
    posicion_actual = 0

    for letra, numero, direccion in diccionario:

        if direccion == 'I':
            paso = -1
        elif direccion == 'D':
            paso = 1
        else:
            raise ValueError("El patrón solo puede contener 'I' o 'D'.")

        for _ in range(numero):
            posicion_actual = (posicion_actual + paso) % len(diccionario)
            while posicion_actual in posiciones_usadas:
                posicion_actual = (posicion_actual + paso) % len(diccionario)

        posiciones_usadas.add(posicion_actual)
        nuevo_texto += diccionario[posicion_actual][0] 
    return  nuevo_texto






