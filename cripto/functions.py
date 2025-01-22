
def invertir_texto(texto):
    return texto[::-1]

# Ejemplo de uso
# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# invertido = invertir_texto(texto)



def reorganizar_texto_por_letra(texto, letra_inicio):
   
    letras = list(texto)
    try:
        indice = letras.index(letra_inicio)
    except ValueError:
        return texto
    
    letras_reorganizadas = letras[indice:] + letras[:indice]
    resultado = ''.join(letras_reorganizadas)
    return resultado

# Ejemplo de uso
# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# letra_inicio = "R"
# reorganizado = reorganizar_texto_por_letra(texto, letra_inicio)



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

# Ejemplo de uso
# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# desplazamiento = 35
# cifrado = julio_cesar(texto, desplazamiento)



def trasposicion(texto, clave, claveordenada):

    letras = list(texto)
    claveO = list(map(int, clave))
    claveorarray = list(map(int, claveordenada))

    fila_letras = []
    fila_clave = []
    for i, letra in enumerate(letras):
        fila_letras.append(letra) 
        fila_clave.append(claveO[i % len(claveO)])  

    matriz = [fila_letras, fila_clave]
   
    longitud_clave = len(claveO)
    resultado = []

    for i in range(0, len(fila_letras), longitud_clave):
  
        temp_letras = fila_letras[i:i + longitud_clave]
        temp_clave = fila_clave[i:i + longitud_clave]
        temp_claveor = claveorarray
 
        emparejados = list(zip(temp_claveor, temp_letras ))
        mapa_reemplazo = dict(emparejados)
        temp_clave_reemplazado = [mapa_reemplazo[num] for num in temp_clave]

        resultado.extend(temp_clave_reemplazado)

    return resultado

# Ejemplo de uso
# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# clave = "8256"
# claveordenada = "2658"
# trasposicion = trasposicion(texto, clave, claveordenada)



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

# Ejemplo de uso
# texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# clave = "8256"
# claveordenada = "82645"
# trama = trama(texto, clave, claveordenada)



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

# Ejemplo de uso
# texto = "RQPOÑNMLKJIHGFEDCBAZYXWVUTS"
# clave = "695472"
# patron = "IDI"
# IDI = IDI(texto, clave, patron)






