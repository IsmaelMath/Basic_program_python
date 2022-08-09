def media(lista_numeros, periodo):
    x = 0
    media_dinamica = []
    for x in range(0, 100):
        calculo_media = sum(lista_numeros[x: x+periodo]) / periodo
        media_dinamica.append(calculo_media)

        if x+periodo >= len(lista_numeros):
            break

    print(f"A média de periodo {periodo} é:  {media_dinamica}")
    return media_dinamica

lista = [25, 35, 45, 77, 85, 78, 48, 36, 49, 100]
periodo = int(input("Informe o perido que deseja calcular na media: "))

w = media(lista, periodo) 