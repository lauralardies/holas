Algoritmo descomponer
# Descompone `ca' en `componentes' en `dimensión' cadenas    
# separadas por `separador'.
Entrada    
  ca          : CADENA    # La cadena a descomponer    
  separador  : CARACTER # El carácter que separa las cadenas
  componentes : TABLA[CADENA] # Los componentes de `ca'    
  dimensión   : ENTERO    # La cantidad de componentes
precondición    
  ca ≠ NULO    
  separador ≠ NULO    
  está_definido(componentes)
variable    
  L : ENTERO # La longitud de `ca'    
  k : ENTERO # Última ocurrencia del `separador' encontrada    
  i : ENTERO # Índice del siguiente componente a registrar    
  r : ENTERO # Posición siguiente ocurrencia del `separador'

inicialización    
  L ← longitud(ca)   # Índice del último carácter    
  k ← 0      # Índice de la última ocurrencia del `separador'                   
              # encontrada    
  i ← 1      # Índice del siguiente componente a registrar    
  r ← posición(ca, 1, L)
       # Búsqueda de la primera ocurrencia de `separador'
mientras que    
  k < L y r ≠ AUSENTE    
  invariante        
      (H)    
    variante de control        
      L - k
    repetir    
      afirmación        
        ítem(ca, k) = separador y ítem(ca, r) = separador    
      # Se copia la cadena `ca' entre los caracteres    
      # de índices k+1 y r-1    
      componentes[i] ← sub_cadena(ca, k+1, r-1)
      dimensión ← i    
      afirmación      
        componer(componentes, 1, i, separador) =                                          
                                                  sub_cadena(ca, 1, r–1)        
        # componentes[1..i] contiene descomposición de ca[1..r-1]  
        dimensión = i      
        ítem(ca, k) = separador         
          # es la penúltima ocurrencia de `separador'      ítem(ca,
        r) = separador         
          # es la última ocurrencia de `separador'    
        # Ajusta la cantidad de componentes    
        i ← i+1
        afirmación      
          componer(componentes, 1, i-1, separador) =    sub_cadena(ca, 1, r–1)       
            # componentes[1..i-1] contiene descomposición de ca[1..r-1]      
          dimensión = i-1    
        # La última ocurrencia encontrada de `separador' en el índice k    
        k ← r    
        afirmación      
          componer(componentes, 1, i-1, separador) =  sub_cadena(ca, 1, k–1)        
            # componentes[1..i-1] contiene descomposición de ca[1..k-1]      
          dimensión = i-1      
          ítem(ca, k) = separador y ítem(ca, r) = separador        
            # es la última ocurrencia de `separador'    
          r ← posición(ca, k+1, L)    
          afirmación      componer(componentes, 1, i-1, separador) =      sub_cadena(ca, 1, k–1)        
            # componentes[1..i-1] contiene descomposición de ca[1..k-1]      
          dimensión = i-1      
          ítem(ca, k) = separador      
          r = posición(ca, k+1, L, separador)
fin mientras que
si    
  k < L
entonces    
  afirmación        
    r = AUSENTE    
    componentes[i] ← sub_cadena(ca, k+1, L)    
    
    dimensión ← i
fin si

