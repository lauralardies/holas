# Ejercicio 12 Parte 1

Algoritmo tabla_de_los_cuadrados
  # La serie en 'cuadrados' de los cuadrados perfectos inferiores en 'límite'.

Entrada	
  cuadrados : TABLA[ENTERO]	# La tabla a inicializar	
  límite : ENTERO # El límite superior de los cuadrados a calcular

precondición	
  límite ≥ 0
  # El lugar libre en 'cuadrados' debe suficiente
  límite ≤ índice_max(cuadrados) x índice_max(cuadrados)

inicialización	     
  k ← 0	# el entero para el que se calcula el cuadrado	 
  cuadrado ← 0	# cuadrado  = k2	
  impar ← 1	# impar = 2xk + 1

realización	
  hasta que		
    cuadrado ≥ límite	
  repetir		
    afirmación			
      cuadrado < límite		
    cuadrados[k] ← cuadrado		
    cuadrado ← cuadrado + impar		
    impar ← impar + 2		
    k ← k +1
  fin repetir	

  afirmación		
    cuadrado ≥ límite		
    antiguo(límite) = cuadrados[índice_min(cuadrados)]	

  cuadrados[k] ← cuadrado	
  cuadrados[índice_min(cuadrados)] ← k

postcondición	
  # el valor de 'límite' no se modifica	
  antiguo(límite) = límite	
  # Cada celda de índice positivo contiene el cuadrado del índice	
  (∀k ∈ ℤ)(índice_min(cuadrados) < k et k2 ≥ límite => cuadrados[k] = k2 )	

  # La primea celda de `cuadrados' está reservada al índice del último cuadrado perfecto guardado	
  cuadrados[índice_min(cuadrados)]2 = cuadrados[cuadrados[índice_min(cuadrados)]]	

fin tabla_de_los_cuadrados




# Ejercicio 12 Parte 2

Algoritmo raiz_cuadrada_entera
# La raíz cuadrada entera del número entero 'n'

Entrada
  n : ENTERO # Calculo de entero 
  cuadrados : TABLA[ENTERO] # Tabla de los cuadrados perfectos
  raiz : ENTERO # ENTERO  

precondicion
  n ≥ 0

constante
  MIN : ENTERO ← índice_min(cuadrados) + 1
	# El índice de la primera celda útil de 'cuadrados' (la que contiene el primer cuadrado perfecto 0)
	MAX : ENTERO ← cuadrados[MIN – 1]
	# El índice del mayor cuadrado perfecto de 'cuadrados'

variable
  situación : ENTERO
	# posición del cuadrado perfecto inferior o igual a 'n'

realizacion 
  si n > cuadrados[MAX] entonces
	  # Copia de seguridad del antiguo valor de MAX
		MIN ← MAX
    # Ampliar la tabla de los cuadrados perfectos de cuadrados[MIN] hasta el cuadrado perfecto superior o igual a 'n'
		tabla_de_los_cuadrados(cuadrados, n)
		afirmación
      # Nuevo valor de MAX
			MAX = cuadrados[índice_min(cuadrados)]
			# Nuevos valores calculados
			cuadrados[MIN] < n ≤ cuadrados[MAX]
  fin si
  afirmación
    n ≤ cuadrados[MAX]
	si
		n = cuadrados[MAX]
	entonces
    # n es un cuadrado perfecto: su raíz es su índice en la tabla de los cuadrados
		raíz ← MAX
  si no
    afirmación
			n < cuadrados[MAX]
			# MIN = antiguo(MAX) ; MAX = nuevo MAX

		situación ← dicotomía(cuadrados, MIN, MAX, n)
		afirmación
			MIN ≤ situación ≤ MAX
			cuadrados[situación] ≤ n < cuadrados[situación + 1]
		raíz ← situación
  fin si

postcondicion
  # El número entero 'n' no se ha modificado
	antiguo(n) = n

	# Las celdas de la tabla inicial no se han modificado
	antiguo
    (
      sub_tabla(
        cuadrados,
				antiguo(índice_min(cuadrados)) + 1,
				antiguo(cuadrados[índice_min(cuadrados)])
		    )
    )
    =
    sub_tabla(
      cuadrados,
			índice_min(cuadrados) + 1, 
			antiguo(cuadrados[índice_min(cuadrados)])
      )

  # La tabla se amplía si es insuficiente
	cuadrados[antiguo(índice_min(cuadrados))] < n => cuadrados[índice_min(cuadrados)] ≥ n

  # Si no, no se modifican ni la tabla ni índice_min(cuadrados)
	cuadrados[antiguo(índice_min(cuadrados))] ≥ n => 
	antiguo(índice_min(cuadrados)) = índice_min(cuadrados)

  # 'raíz' es la raíz cuadrada entera de 'n'
	raíz2 ≤ n < (raíz + 1)2 <=> raíz = [√n] 

fin raiz_cuadrada_entera
