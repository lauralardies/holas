Algoritmo tabla_de_los_cuadrados
    # La serie en `cuadrados' de los cuadrados perfectos inferiores	
    # en `límite'.
Entrada	
    cuadrados : TABLA[ENTERO]	# La tabla a inicializar	
    límite : ENTERO # El límite superior de los cuadrados a calcular
precondición	
    límite ≥ 0	
    # El lugar libre en `cuadrados' debe suficiente	
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
    cuadrados[k] ← cuadrado	cuadrados[índice_min(cuadrados)] ← k
postcondición	
    # el valor de `límite' no se modifica	
    antiguo(límite) = límite	
    # Cada celda de índice positivo contiene el cuadrado del	
    # índice	
    (∀k ∈ ℤ)(índice_min(cuadrados) < k et k2 ≥ límite =>			   
                                                cuadrados[k] = k2 )	
    # La primea celda de `cuadrados' está reservada al índice del último cuadrado perfecto guardado	
    cuadrados[índice_min(cuadrados)]2 = 					
                                cuadrados[cuadrados[índice_min(cuadrados)]]		
fin tabla_de_los_cuadrados



