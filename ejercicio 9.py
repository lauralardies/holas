Algoritmo indice_palabra
  # Creamos un algoritmo que da una lista de palabras que empiezan por una letra dada. 
  # Como las palabrasd el diccionario están ordenadas alfabéticamente, el algoritmo solo tiene que recorrer la tabla hasta encontrar las palabras que comienzan con la inicial dada.

Entrada 
  inicial : CARACTER 
  # La inicial que se buca en el diccionario
  diccionario : TABLA[CADENA]
  # Objetivo de la búsqueda
  inicio : ENTERO 
  # Índice de la primera celda

Resultado : ENTERO 

precondicion 
  es_alfabetico(incial)
  esta_definido(diccionario)
  indice_valido(diccionario, inicio)

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
    ítem(diccionario[i], 1) < inicial y entonces j ≠ I_MIN
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
# ítem(diccionario[i], 1) ≥ inicial o si no j = I_MIN
# ítem(diccionario[i], 1) > inicial o si no j = I_MIN => Resultado = AUSENTE
# ítem(diccionario[i], 1) = inicial => Resultado ≠ AUSENTE
  si
    ítem(diccionario[i], 1) = inicial
  entonces
    Resultado ← i
  fin si

postcondicion 
  # AUSENTE si no hay palabra con la inicial 'inicial' en sub_tabla(diccionario, inicio, índice_max(diccionario))
  
  Resultado = AUSENTE => (∀k ∈ ℤ)
    (
      inicio ≤ k ≤ índice_max(diccionario) => ítem(diccionario[k], 1) ≠ inicial
    )

  # Resultado es el índice de una palabra de inicial 'inicial' en sub_tabla(diccionario, inicio, índice_max(diccionario))

  Resultado ≠ AUSENTE =>
    (
      inicio ≤ Resultado ≤ índice_max(diccionario) y ítem(diccionario[Resultado], 1) = inicial
    )
    
fin indice_palabra