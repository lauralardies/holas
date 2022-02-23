algoritmo cifra
	# La cifra que representa el número entero 'n' en base ≥ 2.

Entrada
	n : ENTERO	# El número entero a convertir

Resultado: CARACTER

precondición
	n ≥ 2

postcondición
	n < 10 => Resultado = carácter(código('0') + n)
	n ≥ 10 => Resultado = carácter(código('A') + n – 10)

fin cifra