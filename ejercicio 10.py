tipo PERSONA estructura	
    identificador : ENTERO	        
    edad : ENTERO	   
    identidad : IDENTIDAD	
    padre : ENTERO	
    madre : ENTERO
fin PERSONA
familias : TABLA[PERSONA][1, 1000]
# Copiar las familias[45 .. 72]

copia ← sub_tabla(familias, 45, 72)
# Con la convención «la primera celda de toda tabla lleva
# el número 1», tenemos:
afirmación	
  copia[1] = familias[45]	
  copia[1].identificador = 45