# Ejercicio 9 Parte 1 :

Algoritmo indice_palabra
  # Creamos un algoritmo que da una lista de palabras que empiezan por una letra dada. 
  # Como las palabrasd el diccionario están ordenadas alfabéticamente, el algoritmo solo tiene que recorrer la tabla hasta encontrar las palabras que comienzan con la inicial dada.

Entrada 
  inicial : CARACTER 
  # La inicial que se buca en el diccionario
  diccionario : TABLA[CADENA]
  # Objetivo de la búsqueda
  anterior, siguiente : TABLA[ENTERO]
    # Los índices de las palabras anteriores y siguientes
  inicio : ENTERO 
  # Índice de la primera celda

Resultado : ENTERO 

precondicion 
  es_alfabetico(incial)
  esta_definido(diccionario)
  indice_valido(diccionario, inicio)

constante
  I_MIN : ENTERO ← indice_min(diccionario)
  I_MAX : ENTERO ← indice_max(diccionario)
  AUSENTE : ENTERO ← ???

variable
  i, j : ENTERO

inicialización
    i ← inicio
        # Índice de la siguiente celda a observar
    j ← siguiente[i]
        # Índice de la palabra que sigue a la de índice i en orden
    Resultado ← AUSENTE # Todavía no ha encontrado nada

realización
  mientras que
    item(diccionario[i], 1) < inicial y entonces j ≠ I_MIN
    invariante
      se han observado las palabras de índice inicio siguiente[inicio], …,anterior[i]. 
      Resultado = AUSENTE
      j = siguiente[i]
    variante de control
      ???
  repetir
    afirmación
      se han observado las palabras de índice inicio, siguiente[inicio], …,anterior[i] e i.
      Resultado = AUSENTE

    i ← j
    afirmación
      se han observado las palabras de índice inicio, siguiente[inicio], …,anterior[i].
      Resultado = AUSENTE
      j = i

    j ← siguiente[i]
    afirmación
      se han observado las palabras de índice inicio, siguiente[inicio], …,anterior[i].
      Resultado = AUSENTE
      j = siguiente[i]
  fin repetir
# item(diccionario[i], 1) ≥ inicial o si no j = I_MIN
# item(diccionario[i], 1) > inicial o si no j = I_MIN => Resultado = AUSENTE
# item(diccionario[i], 1) = inicial => Resultado ≠ AUSENTE
  si
    item(diccionario[i], 1) = inicial
  entonces
    Resultado ← i
  fin si

postcondicion 
  # AUSENTE si no hay palabra con la inicial 'inicial' en sub_tabla(diccionario, inicio, índice_max(diccionario))
  
  Resultado = AUSENTE => (∀k ∈ ℤ)
    (
      inicio ≤ k ≤ indice_max(diccionario) => item(diccionario[k], 1) ≠ inicial
    )

  # Resultado es el índice de una palabra de inicial 'inicial' en sub_tabla(diccionario, inicio, índice_max(diccionario))

  Resultado ≠ AUSENTE =>
    (
      inicio ≤ Resultado ≤ indice_max(diccionario) y item(diccionario[Resultado], 1) = inicial
    )

fin indice_palabra 





# Ejercicio 9 Parte 2 :
# Definimos el tipo PALABRA y modificiamos el algoritmo anterior

tipo PALABRA estructura
  anterior : ENTERO
  # El índice de la palabra que precede a esta palabra
  siguiente : ENTERO
  # El índice de la palabra siguiente
  palabra : CADENA
fin PALABRA



Algoritmo indice_palabra

Entrada 
  inicial : CARACTER 
  diccionario : TABLA[CADENA]
  anterior, siguiente : TABLA[ENTERO]
  inicio : ENTERO 

Resultado : ENTERO 

precondicion 
  es_alfabetico(incial)
  esta_definido(diccionario)
  indice_valido(diccionario, inicio)

constante
  INFINITO : PALABRA # La mayor palabra de todas
  I_MIN : ENTERO ← 0
  I_MAX : ENTERO ← 1000
  AUSENTE : ENTERO ← ???

variable
  i, j : ENTERO
  diccionario : TABLA[PALABRA][I_MIN, I_MAX]

inicialización
    i ← inicio
    j ← siguiente[i]
    Resultado ← AUSENTE

    # Inicialización de la palabra INFINITO 
    INFINITO.anterior ← I_MIN
    INFINITO.siguiente ← I_MIN
    INFINITO.palabra ← ???

    # Inicialización del diccionario sin ninguna palabra
    inicializar(diccionario)

realización
  mientras que
    item(diccionario[i], 1) < inicial y entonces j ≠ I_MIN
    invariante
      se han observado las palabras de índice inicio siguiente[inicio], …,anterior[i]. 
      Resultado = AUSENTE
      j = siguiente[i]
    variante de control
      ???
  repetir
    afirmación
      se han observado las palabras de índice inicio, siguiente[inicio], …,anterior[i] e i.
      Resultado = AUSENTE

    i ← j
    afirmación
      se han observado las palabras de índice inicio, siguiente[inicio], …,anterior[i].
      Resultado = AUSENTE
      j = i

    j ← siguiente[i]
    afirmación
      se han observado las palabras de índice inicio, siguiente[inicio], …,anterior[i].
      Resultado = AUSENTE
      j = siguiente[i]
  fin repetir
  si
    item(diccionario[i], 1) = inicial
  entonces
    Resultado ← i
  fin si

postcondicion 
  Resultado = AUSENTE => (∀k ∈ ℤ)
    (
      inicio ≤ k ≤ indice_max(diccionario) => item(diccionario[k], 1) ≠ inicial
    )

  Resultado ≠ AUSENTE =>
    (
      inicio ≤ Resultado ≤ indice_max(diccionario) y item(diccionario[Resultado], 1) = inicial
    )

fin indice_palabra 



# En nuestro nuevo algoritmo tenemos una función nueva que no está definida : inicializar(). Vamos a definirla

inicializar(diccionario : TABLA[PALABRA])
# Inicializa un 'diccionario' vacío.

precondición
  esta_definido(diccionario)

constante
  INFINITO : PALABRA  # La mayor palabra de todas
  I_MIN : ENTERO ← indice_min(diccionario)
  I_MAX : ENTERO ← indice_max(diccionario)

variable
  i : ENTERO # Índice de la siguiente celda a inicializar

inicialización
  i ← I_MIN # Índice de la siguiente celda a liberar

realización
  # La primera celda contiene «la mayor palabra»
  diccionario[I_MIN].palabra ← INFINITO

  # Todas las celdas se indexan por sí mismas: tabla vacía
  mientras que i ≤ I_MAX repetir
    diccionario[i].anterior ← i
    diccionario[i].siguiente ← i
    i ← i + 1
  fin repetir

postcondición
  # El diccionario está vacío
  esta_libre(diccionario)

fin inicializar



# Ahora estamos ante otra función nueva. esta_libre(). La definimos:

esta_libre(diccionario : TABLA[PALABRA])
# ¿'diccionario' está vacío de palabra?

Precondición
  esta_definido(diccionario)

constante
  I_MIN : ENTERO ← indice_min(diccionario)
  I_MAX : ENTERO ← indice_max(diccionario)

variable
  i : ENTERO # Índice de la siguiente celda a verificar

inicialización
  i ← I_MIN  # Índice de la siguiente celda a verificar
  Resultado ← VERDADERO

realización
  # ¿Todas las celdas se indexan a sí mismas?
  mientras que i ≤ I_MAX y entonces Resultado = VERDADERO repetir
    Resultado ← (diccionario[i].anterior = i y diccionario[i].siguiente = i)
    
    i ← i + 1
  fin repetir

postcondición
    # Ninguna palabra en la tabla : el diccionario está vacío
    está_vacío(diccionario)

    # Ninguna celda ocupada
    (∀k ∈ ℤ)(índice_min(diccionario) < k ≤ índice_max(diccionario) => diccionario[k].anterior = diccionario[k].siguiente = k)

Resultado ←  
  (
    diccionario[índice_min(diccionario)].anterior = diccionario[índice_min(diccionario)].siguiente = índice_min(diccionario)
  )

fin está_libre