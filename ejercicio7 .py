Entrada	
  n : ENTERO		# El número entero a convertir	
  BASE : ENTERO		# La base de conversión
  
Resultado : CADENA
variable	
  dividendo : ENTERO ← abs(n)	
  q, r : ENTERO	
		# Generan las series de los cocientes y de los restos		
    # de `dividendo' por `BASE'	
  k : ENTERO		# El número de cocientes ya calculados
inicialización	
  Resultado ← CADENA_VACIA	# El resultado actual	
  k ← 0
realización	
  hasta que dividendo < BASE		
    invariante		
    #(H) : la siguiente división a realizar es 				#	la de `dividendo' por `BASE';
		#	el resultado parcial es Resultado		
    #	k es el número de divisiones realizadas			
          dividendo = abs(n) x BASE-k		
  variante de control			
          cociente(dividendo, BASE)