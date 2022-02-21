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

constante 
  I_MIN : ENTERO ← indice_min(diccionario)
  I_MAX : ENTERO ← indice_max(diccionario)
  AUSENTE : ENTERO ← ???

variable 
  i : ENTERO # Indice de la siguiente celda a observar 

inicializacion 
  i ← I_MIN 
  Resultado = AUSENTE # Todavía no se ha encontrado nada

realizacion 
  mientras que 
    i ≤ I_MAX et Resultado = AUSENTE
    invariante 
      (∀k ∈ ℤ)(I_MIN ≤ k < i => Resultado = AUSENTE <=> (∀k ∈ ℤ)(I_MIN ≤ k < i => ítem(diccionario[k], 1) ≠ inicial)
    variante 
      I_MAX – i + 1
  repetir 
    si 
      ítem(diccionario[i], 1) = inicial
    entonces 
      afirmacion
      i ≤ I_MAX (∀k ∈ ℤ)(I_MIN ≤ k < i => Resultado = AUSENTE) et ítem(diccionario[i], 1) = inicial
      Resultado ← i
      afirmacion 
        i ≤ I_MAX
        Resultado = i ≠ AUSENTE
    fin si
  fin repetir

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