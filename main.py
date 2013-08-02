#coding: utf-8

#        |                    MateX Main                 |
#        |                      v 0.2                    |
#        |                Licencia GNU GPLv3             |
#        |              ©Guillemo Gómez Fonfría          |

#Módulos
import matexlib as lib
import helplib
import sys

def main():
	print("Interfaz MateX-0.2\nEscribe 'ayuda' para más información o 'comandos' para una lista completa con los comandos reconocidos.")

	while True:
		writen = raw_input(">>> ")
		if writen in ("salir", "exit"):
			break

		elif writen in ("ayuda"):
			helplib.ayuda2_es()

		elif writen in ("help"):
			helplib.help2_en()

		elif writen in ("iAyuda", "iayuda"):
			print("Función aun no implementada")

		elif writen in ("iHelp", "ihelp"):
			print("This has not yet been implemented")

		elif writen in ("instalar"):
			helplib.instalar_es()

		elif writen in ("install"):
			helplib.install_en()

		elif writen in ("comandos"):
			print("A continuación una lista con todos los comandos que acepta MateX y una breve descripción\n")
			for i in helplib.comandos:
				print i,helplib.comandos[i]

		elif writen in ("commands"):
			print("Full list with recognized internal commands and their description:")
			for i in helplib.commands:
				print i,helplib.commands[i]

		elif writen in ("debugging","debug"):
			x = lib.test()
			print(x)

		elif writen in ("aleatorio"):
			rango = input("Introcue el número más alto y el más bajo del rango en el que quieres que se genere el número separados por comas. Ej: 2,5\n >>> ")
			x = lib.aleatorio(rango)
			print("\nEl número generado es: " + str(x))

		elif writen in ("raiz"):
			n = input("Introduce el número del que quieras conocer su raíz cuadrada\n >>> ")
			try:
				x = lib.raiz(n)
				print("La raíz de " + str(n) + " es " + str(x))
			except lib.RaizExcpt:
				print("Has introducido un número negativo cuya raíz cuadrada no está definida")

		elif writen in ("mcd"):
			nums = input("Introduce los dos números de los que quieres hallar su MCD, siendo el pequeño el primero y separados por comas. Ej:3,6\n >>> ")
			x = lib.mcd(nums)
			print("MCD(" + str(nums[0]) + ", " + str(nums[1]) + ") = " + str(x))

		elif writen in ("mcm"):
			nums = input("Introduce los dos números de los que quieres hallar su MCM, siendo el pequeño el primero y separados por comas. Ej:3,6\n >>> ")
			x = lib.mcm(nums)
			print("MCM(" + str(nums[0]) + ", " + str(nums[1]) + ") = " + str(x))

		elif writen in ("sistema"):
			print("Para un sistema \"ax+by=c dx+ey=f\" escribe:")
			ecuacion1 = raw_input(" * La primera ecuación \"ax+by=c\": ")
			ecuacion2 = raw_input(" * La segunda ecuación \"dx+ey=f\": ")
			resultados = lib.sist(ecuacion1,ecuacion2)
			xa = resultados[0]
			xb = resultados[1]
			ya = resultados[2]
			yb = resultados[3]
			print("La solución del sistema " + ecuacion1 + " " + ecuacion2 + " es:")
			if xa == xb:
				print("x = " + str(xa))
			else:
				print("x = " + str(xb) + " = " + str(xa))
			if ya == yb:
				print("y = " + str(ya))
			else:
				print("y = " + str(yb) + " = " + str(ya))

		elif writen in ("ecuacion","ecuación"):
			ec = raw_input("Introduce una ecuación de segundo grado \"ax²+bx+c=0\"\n >>> ")
			try:
				resultados = lib.ec2(ec)
				x1a = resultados[0]
				x1b = resultados[1]
				x2a = resultados[2]
				x2b = resultados[3]
				if x1a == x2a:
					print("El resultado de la ecuación \"" + ec + "\" es:")
					print(str(x1a) + " = " + str(x1b))
				else:
					print("Los resultados de la ecuación \"" + ec + "\" son:")
					print(str(x1a) + " = " + str(x1b))
					print(str(x2a) + " = " + str(x2b))
			except:
				print("\""  + ec + "\" no tiene solución o no es una ecuación")

		elif writen in ("regla3","regla de 3"):
			r3 = input("En una regla de 3 directa en la que 'a' es a 'b' como 'c' es a 'x', escribe, separados por comas: a,b,c\n >>> ")
			x = lib.regla3(r3)
			regla = str(r3[0]) + " es a " + str(r3[1]) + " como " + str(r3[2]) + " es a 'x'"
			print("En la regla de 3 " + str(regla) + " x= " + str(x))

		elif writen in ("reglainv","regla inversa","regla de 3 inversa"):
			r3 = input("En una regla de 3 inversa en la que 'a' es a 'b' como 'c' es a 'x', escribe, separados por comas: a,b,c\n >>> ")
			a = r3[0]
			b = r3[1]
			c = r3[2]
			regla = str(a) + " es a " + str(b) + " como " + str(c) + " es a 'x'"
			x = lib.reglainv(a,b,c)
			print("En la regla de 3 inversa " + str(regla) + " x=" + str(x))

		elif writen in ("coulomb"):
			letra = raw_input("En la ley de Coulmb \"F=(k·q1·q2)/d²\", escribe la variable que quieres hallar\n >>> ")
			try:
				x = lib.coulomb(letra)
				print(str(letra) + "=" + str(x))
			except lib.RaizExcpt:
				print(letra.upper() + " es igual a la raíz de un número negativo")

		elif writen in ("perimetro","perímetro"):
			ns = input("Introduce el número de lados (n) y la longitud (l) de los lados para hallar el perimetro de un polígono regular. Ej: n,l\n >>> ")
			n = ns[0]
			l = ns[1]
			p = lib.perimetro(n,l)
			print("En un polígono de " + str(n) + " lados con una longitud de " + str(l) + " cada uno, P=" + str(p))

		elif writen in ("longitud"):
			r = input("Introduce el radio de una circunferencia para hallar su longitud.\n >>> ")
			l = lib.longitud(r)
			print("En una circunferencia de radio " + str(r) + ", L=" + str(l))

		elif writen in ("acuadrado","área cuadrado"):
			l = input("Introduce la longitud del lado de un cuadrado para hallar su área\n >>> ")
			a = lib.acuadrado(l)
			print("En un cuadrado de lado l=" + str(l) + ", su Área es igual a " + str(a))

		elif writen in ("arectangulo","área rectángulo"):
			bh = input("Introduce la base y la altura de un rectángulo, separadas por comas, para hallar su área. Ej: 4,5\n >>> ")
			b = bh[0]
			h = bh[1]
			a = lib.arectangulo(b,h)
			print("En un rectángulo de base " + str(b) + " y altura " + str(h) + " A=" + str(a))

		elif writen in ("atriangulo","área triángulo"):
			bh = input("Introduce la base y la altura de un triángulo, separadas por comas, para hallar su área. Ej: 2,6\n >>> ")
			b = bh[0]
			h = bh[1]
			a = lib.atriangulo(b,h)
			print("En un triángulo de base " + str(b) + " y altura " + str(h) + " A=" + str(a))

		elif writen in ("arombo","área rombo"):
			Dd = input("Introduce la diagonal mayor (D) y la diagonal menor (d) de un rombo, separadas por comas, para hallar su área (A). Ej: 3,4\n >>> ")
			D = Dd[0]
			d = Dd[1]
			a = lib.arombo(D,d)
			print("En un rombo en el que D=" + str(D) + " y d=" + str(d) + ", A=" + str(a))

		elif writen in ("atrapecio","área trapecio"):
			Bbh = input("Introduce la Base mayor (B), base menor (b) y la altura (h) de un trapecio, separadas por comas, para hallar su área (A). Ej:8,7,6\n >>> ")
			B = Bbh[0]
			b = Bbh[1]
			h = Bbh[2]
			a = lib.atrapecio(B,b,h)
			print("En un trapecio en el que B=" + str(B) + ", b=" + str(b) + " y h=" + str(h) + ", A=" + str(a))

		elif writen in ("apoligono","área polígono"):
			Pa = input("Introduce el Perímetro (P) y el apotema (a) de un polígono regular, separados por comas, para hallar su área (A). Ej: 2,1\n >>> ")
			P = Pa[0]
			a = Pa[1]
			A = lib.apoligono(P,a)
			print("El Área de un Polígono regular de perímetro P=" + str(P) + "y apotema a=" + str(a) + ", es A=" + str(A))

		elif writen in ("acirculo","área círculo"):
			r = input("Introduce el radio (r) de un círculo para hallar su área.\n >>> ")
			a = lib.acirculo(r)
			print("En un círculo r=" + str(r) + ", A=" + str(a))

		elif writen in ("pitagoras","pitágoras"):
			letra = raw_input("Introduce la variable a hallar en el teorema de pitágoras (a²=b²+c²).\n >>> ")
			x = lib.pitagoras(letra)
			print(str(letra) + "=" + str(x))

		else:
			print("Comando no reconocido. Escribe 'ayuda' para obtener más información, 'iAyuda' para el menú de ayuda interactivo o 'comandos' para una lista completa de los comandos reconocidos por el programa.")
	sys.exit()
