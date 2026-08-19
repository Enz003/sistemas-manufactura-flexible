# Sistemas de Manufactura Flexible

Algoritmo de eliminación de filas/columnas sobre una matriz de flujos (from-to chart)
para determinar la secuencia de máquinas/estaciones, usado en el diseño de sistemas
de manufactura flexible.

## Descripción

En cada iteración se suman los flujos de cada fila/columna, se elimina la de menor
suma, y se registra su índice **original** en la secuencia de salida. El índice
original se preserva aunque la matriz se vaya reduciendo en cada paso, mediante una
lista de índices que se actualiza en paralelo a la matriz.

## Uso

```bash
python src/main.py
```

## Estructura

```
.
├── src/
│   └── main.py   # algoritmo y matriz de ejemplo
└── README.md
```
