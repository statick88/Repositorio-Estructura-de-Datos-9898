## Inserción de un vértice:

**Descripción:** Para insertar un nuevo vértice en un grafo, simplemente se agrega un nuevo elemento al conjunto de vértices del grafo.

Código en R:

```{R}
#Crear un grafo vacío
grafo <- graph()
```
**Insertar un vértice con identificador "A"**
grafo <- add.vertices(grafo, "A")

## Eliminación de un vértice:

**Descripción:** Para eliminar un vértice de un grafo, se elimina el elemento correspondiente del conjunto de vértices y se eliminan todas las aristas que estén conectadas a ese vértice.

Código en R:

```{R}
# Eliminar el vértice con identificador "A"
grafo <- delete.vertices(grafo, "A")
```
## Inserción de una arista:

**Descripción:** Para insertar una nueva arista en un grafo, se agrega un nuevo par de vértices conectados mediante la arista al conjunto de aristas del grafo.

Código en R:

```{R}
# Crear un grafo vacío
grafo <- graph()

#Insertar una arista entre los vértices "A" y "B"
grafo <- add.edges(grafo, c("A", "B"))
```
## Eliminación de una arista:

**Descripción:** Para eliminar una arista de un grafo, se elimina el par de vértices conectados mediante la arista del conjunto de aristas del grafo.

Código en R:

```{R}
# Eliminar la arista entre los vértices "A" y "B"
grafo <- delete.edges(grafo, c("A", "B"))
```

En base a los ejemplos anteriores, por favor desarrolla estos ejercicios:

1. Crea un grafo vacío.
```{r}
library(igraph)

grafo <- graph.empty()
```
2. Inserta los vértices A, B, C y D en el grafo.
```{r}
vertices <- c("A", "B", "C", "D")
grafo <- add.vertices(grafo, vertices)
```
3. Elimina el vértice C del grafo.
```{r}
grafo <- delete.vertices(grafo, "C")
```
4. Inserta una arista entre los vértices A y B.
```{r}
grafo <- add.edges(grafo, c("A", "B"))
```
5. Elimina la arista entre los vértices A y B.
```{r}
grafo <- delete.edges(grafo, c("A", "B"))
```
6. Inserta aristas entre todos los pares de vértices en el grafo.
7. Elimina todas las aristas del grafo.
8. Inserta los vértices 1, 2, 3 y 4 en el grafo.
9.  Inserta una arista entre los vértices 1 y 2.
10. Inserta una arista entre los vértices 2 y 3.
11. Inserta una arista entre los vértices 3 y 4.
12. Elimina el vértice 3 del grafo.
13. Inserta una arista entre los vértices 1 y 4.
14. Inserta una arista entre los vértices 2 y 4.
15. Elimina todas las aristas del grafo.
16. Inserta los vértices A, B, C y D en el grafo.
17. Inserta una arista dirigida desde el vértice A al vértice B.
18. Inserta una arista dirigida desde el vértice B al vértice C.
19. Inserta una arista dirigida desde el vértice C al vértice D.
20. Elimina todas las aristas del grafo.

Recuerda utilizar las funciones add.vertices(), delete.vertices(), add.edges() y delete.edges() de la librería igraph para realizar estas operaciones. Puedes combinar diferentes operaciones para realizar ejercicios más complejos y variados.
