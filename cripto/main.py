import functions as func

def main():

    texto = "MJCHEFPTUDRSOZQYNWBAXVKILG"
    saltos = "35"
    clave = "35768942"
    claveordenada = "23456789"
    patron = "IDI"

    # print("INVERTIR TEXTO")
    # xp = func.invertir_texto(texto)

    # print("ORGANIZAR TEXTO POR LETRA")
    # xp = func.reorganizar_texto_por_letra(texto, "R")

    # print("JULIO CESAR")
    # xp = func.julio_cesar(texto, saltos, False)

    # print("TRASPOSICION")
    # xp = func.trasposicion(texto, clave, claveordenada)

    # print("TRAMA")
    # xp = func.trama(texto, clave, claveordenada)

    print("IDI")
    xp = func.IDI(texto, saltos, patron)


    print(xp)




if __name__ == "__main__":
    main()