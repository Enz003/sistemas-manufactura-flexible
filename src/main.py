def limpiarMatriz(matriz: list,indice: int):
    matriz.pop(indice)
    for element in matriz:
        element.pop(indice)
    return len(matriz)

def layout_algoritmo(matriz):
    indices = list(range(len(matriz)))
    secuencia = []
    while len(matriz) > 1:
        suma = [0]*len(matriz)
        for elemento in matriz:
            for i in range(len(matriz)):
                suma[i] += elemento[i]
        pos = suma.index(min(suma))
        secuencia.append(indices[pos])
        limpiarMatriz(matriz, pos)
        indices.pop(pos)

    secuencia.append(indices[0])
    respuesta=list()
    for elemento in secuencia:
        respuesta.append(int(elemento)+1)
    return respuesta


matriz = [
    [0,24,0,0,0,0],
    [0,0,64,0,0,0],
    [14,24,0,0,0,0],
    [10,0,0,0,10,0],
    [40,0,40,0,0,50],
    [0,16,14,20,0,0]
]

respuesta = layout_algoritmo(matriz)

print(respuesta)

