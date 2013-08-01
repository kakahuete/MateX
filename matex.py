#!/usr/bin/python
#coding: utf-8

#        |                      MateX                    |
#        |                      v 0.1                    |
#        |                Licencia GNU GPLv3             |
#        |              Guillemo Gómez Fonfría           |



#Módulos
try:
	import matexlib as lib
except ImportError:
	print("La librería que utiliza MateX no está instalada, vuelve a ejecutar este programa como root (sudo) y escribe instalar.")

#Funciones
def comprobador(variable,ecuacion1):
	if variable == "String":
		ec1 = lib.simplificador(ecuacion1)
		a = ec1[0]
		b = ec1[1]
		c = ec1[2]
	elif variable == "Tuple":
		a = ecuacion1[0]
		b = ecuacion1[1]
		c = ecuacion1[2]
	else:
		raise lib.DataTypeExcpt("Tipo de dato no reconocido")
	return a,b,c

def main():
	#Interfaz MateX
	print("Interfaz MateX-0.2\nEscribe 'ayuda' para más información o 'comandos' para una lista completa con los comandos reconocidos.")

	#Lista de comandos
	comandos = {"salir:":"Sale de MateX",
			"exit:":"Exits MateX",
			"ayuda:":"Muestra un texto de ayuda",
			"help:":"Shows the help menu",
			"instalar:":"Instala la librería MateXlib",
			"comandos:":"Muestra una lista de comandos aceptados por el programa",
			"debugging:":"Solo para desarrolladores",
			"aleatorio:":"Genera un número aleatorio una vez determinado el rango",
			"raiz:":"Calcula la raíz cuadrada de un número",
			"mcd:":"Calcula el MCD de dos números",
			"mcm:":"Calcula el MCM de dos números",
			"sistema:":"Resuelve un sistema de ecuaciones ax+by=c} dx+ey=f}",
			"ecuacion:":"Resuelve una ecuación de segundo grado ax²+bx=c",
			"regla3:":"Halla x en una regla de 3 directa",
			"reglainv:":"Halla x en una regla de 3 indirecta",
			"coulomb:":"Halla cualquier variable de la ecuación que define la ley de Coulomb",
			"perimetro:":"Halla el perímetro de un polígono regular",
			"longitud:":"Halla la longitud de una circunferencia",
			"acuadrado:":"Halla el área de un cuadrado",
			"arectangulo:":"Halla el área de un rectángulo",
			"atriangulo:":"Halla el área de un triángulo",
			"arombo:":"Halla el área de un rombo",
			"atrapecio:":"Halla el área de un trapecio",
			"apoligono:":"Halla el área de un polígono regular",
			"acirculo:":"Halla el área de un círculo",
			"pitagoras:":"Trabaja con el Teorema de Pitágoras"}

	while True:
		writen = raw_input(">>> ")
		if writen in ("salir","exit"):
			break

		elif writen in ("ayuda","help"):
			print("Interfaz MateX-0.2\nEscribe 'comandos' para una lista completa de comandos\nLa interfaz MateX está diseñada para proporcionar la mayor facilidad posible en la interacción entre el usuario y el programa MateX")

		elif writen in ("instalar","install"):
			print("Instalando los módulos necesarios...\n")
			from os import system
			system("sudo cp matexlib.py /usr/lib/python2.7/matexlib.py")
			from time import sleep
			sleep(2)
			print("Se han creado los siguientes archivos:\n * /usr/lib/python2.7/matexlib.py")
			print("¡Instalación completada!")

		elif writen in ("comandos"):
			print("A continuación una lista con todos los comandos que acepta MateX y una breve descripción\n")
			for x in comandos:
				print x,comandos[x]

		elif writen in ("debugging","debug"):
			x = lib.test()
			print(x)

		elif writen in ("aleatorio"):
			rango = input("Introcue el número más alto y el más bajo del rango en el que quieres que se genere el número separados por comas. Ej: 2,5\n>>> ")
			a = rango[0]
			b = rango[1]
			x = lib.aleatorio(a,b)
			print("\nEl número generado es: " + str(x))

		elif writen in ("raiz"):
			n = input("Introduce el número del que quieras conocer su raíz cuadrada\n>>> ")
			try:
				x = lib.raiz(n)
				print("La raíz de " + str(n) + " es " + str(x))
			except lib.RaizExcpt:
				print("Has introducido un número negativo, que no tiene raíz cuadrada")

		elif writen in ("mcd"):
			ns = input("Introduce los dos números de los que quieres hallar su MCD, siendo el pequeño el primero y separados por comas. Ej:3,6\n>>> ")
			a = ns[0]
			b = ns[1]
			x = lib.mcd(a,b)
			print("El MCD de " + str(a) + " y " + str(b) + " es " + str(x))

		elif writen in ("mcm"):
			ns = input("Introduce los dos números de los que quieres hallar su MCM, siendo el pequeño el primero y separados por comas. Ej:3,6\n>>> ")
			a = ns[0]
			b = ns[1]
			x = lib.mcm(a,b)
			print("El MCM de " + str(a) + " y " + str(b) + " es " + str(x))

		elif writen in ("sistema"):
			print("Para un sistema \"ax+by=c dx+ey=f\" escribe:")
			ecuacion1 = raw_input(" * La primera ecuación \"ax+by=c\": ")
			ecuacion2 = raw_input(" * La segunda ecuación \"dx+ey=f\": ")
			#Comprobando si la forma en la que han sido introducidos los datos
			try:
				tipo1 = lib.DataType(ecuacion1)
				ec1 = comprobador(tipo1,ecuacion1)
				a = ec1[0]
				b = ec1[1]
				c = ec1[2]

				tipo2 = lib.DataType(ecuacion2)
				ec2 = comprobador(tipo2,ecuacion2)
				d = ec2[0]
				e = ec2[1]
				f = ec2[2]

				sistema = ecuacion1 + " " + ecuacion2

				try:
					solucion = lib.sist(a,b,c,d,e,f)
				except:
					solucion = lib.sist(a,b,c,d,e,f,0)
				x = solucion[0]
				y = solucion[1]
				print("La solución al sistema: " + str(sistema) + " es (" + str(x) + "," + str(y) + ")")
			except lib.DataTypeExcpt:
				print("MateX no sabe como manejar los datos introducidos\n")

		elif writen in ("ecuacion","ecuación"):
			ecuacion = raw_input("Introduce una ecuación de segundo grado \"ax²+bx=c\"\n>>> ")
			try:
				tipo = lib.DataType(ecuacion)
				ec = comprobador(tipo,ecuacion)
				a = ec[0]
				b = ec[1]
				c = ec[2]
				try:
					try:
						x = lib.ec2(a,b,c)
					except:
						x = lib.ec2(a,b,c,0)
					try:
						x1 = x[0]
						x2 = x[1]
						print("Las soluciones de la ecuación " + str(ecuacion) + " son " + str(x1) + " y " + str(x2))
					except:
						print("La solución de la ecuación " + ecuacion + " es " + str(x))
				except lib.RaizExcpt:
					print("X es igual a la raíz de un número negativo, por lo que no tiene un resultado real.")
			except lib.DataTypeExcpt:
				print("MateX no sabe como manejar los datos introducidos\n")

		elif writen in ("regla3","regla de 3"):
			r3 = input("En una regla de 3 directa en la que 'a' es a 'b' como 'c' es a 'x', escribe, separados por comas: a,b,c\n>>> ")
			a = r3[0]
			b = r3[1]
			c = r3[2]
			regla = str(a) + " es a " + str(b) + " como " + str(c) + " es a 'x'"
			x = lib.regla3(a,b,c)
			print ("En la regla de 3 " + str(regla) + " x=" + str(x))

		elif writen in ("reglainv","regla inversa","regla de 3 inversa"):
			r3 = input("En una regla de 3 inversa en la que 'a' es a 'b' como 'c' es a 'x', escribe, separados por comas: a,b,c\n>>> ")
			a = r3[0]
			b = r3[1]
			c = r3[2]
			regla = str(a) + " es a " + str(b) + " como " + str(c) + " es a 'x'"
			x = lib.reglainv(a,b,c)
			print ("En la regla de 3 inversa " + str(regla) + " x=" + str(x))

		elif writen in ("coulomb"):
			letra = raw_input("En la ley de Coulmb \"F=(k·q1·q2)/d²\", escribe la variable que quieres hallar\n>>> ")
			try:
				x = lib.coulomb(letra)
				print(str(letra) + "=" + str(x))
			except lib.RaizExcpt:
				print(letra.upper() + " es igual a la raíz de un número negativo")

		elif writen in ("perimetro","perímetro"):
			ns = input("Introduce el número de lados (n) y la longitud (l) de los lados para hallar el perimetro de un polígono regular. Ej: n,l\n>>> ")
			n = ns[0]
			l = ns[1]
			p = lib.perimetro(n,l)
			print("En un polígono de " + str(n) + " lados con una longitud de " + str(l) + " cada uno, P=" + str(p))

		elif writen in ("longitud"):
			r = input("Introduce el radio de una circunferencia para hallar su longitud.\n>>> ")
			l = lib.longitud(r)
			print("En una circunferencia de radio " + str(r) + ", L=" + str(l))

		elif writen in ("acuadrado","área cuadrado"):
			l = input("Introduce la longitud del lado de un cuadrado para hallar su área\n>>> ")
			a = lib.acuadrado(l)
			print("En un cuadrado de lado l=" + str(l) + ", su Área es igual a " + str(a))

		elif writen in ("arectangulo","área rectángulo"):
			bh = input("Introduce la base y la altura de un rectángulo, separadas por comas, para hallar su área. Ej: 4,5\n>>> ")
			b = bh[0]
			h = bh[1]
			a = lib.arectangulo(b,h)
			print("En un rectángulo de base " + str(b) + " y altura " + str(h) + " A=" + str(a))

		elif writen in ("atriangulo","área triángulo"):
			bh = input("Introduce la base y la altura de un triángulo, separadas por comas, para hallar su área. Ej: 2,6\n>>> ")
			b = bh[0]
			h = bh[1]
			a = lib.atriangulo(b,h)
			print("En un triángulo de base " + str(b) + " y altura " + str(h) + " A=" + str(a))

		elif writen in ("arombo","área rombo"):
			Dd = input("Introduce la diagonal mayor (D) y la diagonal menor (d) de un rombo, separadas por comas, para hallar su área (A). Ej: 3,4\n>>> ")
			D = Dd[0]
			d = Dd[1]
			a = lib.arombo(D,d)
			print("En un rombo en el que D=" + str(D) + " y d=" + str(d) + ", A=" + str(a))

		elif writen in ("atrapecio","área trapecio"):
			Bbh = input("Introduce la Base mayor (B), base menor (b) y la altura (h) de un trapecio, separadas por comas, para hallar su área (A). Ej:8,7,6\n>>> ")
			B = Bbh[0]
			b = Bbh[1]
			h = Bbh[2]
			a = lib.atrapecio(B,b,h)
			print("En un trapecio en el que B=" + str(B) + ", b=" + str(b) + " y h=" + str(h) + ", A=" + str(a))

		elif writen in ("apoligono","área polígono"):
			Pa = input("Introduce el Perímetro (P) y el apotema (a) de un polígono regular, separados por comas, para hallar su área (A). Ej: 2,1\n>>> ")
			P = Pa[0]
			a = Pa[1]
			A = lib.apoligono(P,a)
			print("El Área de un Polígono regular de perímetro P=" + str(P) + "y apotema a=" + str(a) + ", es A=" + str(A))

		elif writen in ("acirculo","área círculo"):
			r = input("Introduce el radio (r) de un círculo para hallar su área.\n>>> ")
			a = lib.acirculo(r)
			print("En un círculo r=" + str(r) + ", A=" + str(a))

		elif writen in ("pitagoras","pitágoras"):
			letra = raw_input("Introduce la variable a hallar en el teorema de pitágoras (a²=b²+c²).\n>>> ")
			x = lib.pitagoras(letra)
			print(str(letra) + "=" + str(x))

		else:
			print("Comando no reconocido. Escribe 'ayuda' o 'help' para obtener más información y 'comandos' para una lista completa de los comandos reconocidos por el programa.")

#Ejecutando el programa
main()
