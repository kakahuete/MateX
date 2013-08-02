#coding: utf-8

#        |                   MateXLibrary                |
#        |                      v 0.2                    |
#        |                Licencia GNU GPLv3             |
#        |              ©Guillemo Gómez Fonfría          |

#Librerías necesarias
from fractions import Fraction
from math import pi
from random import randint

#############################
#### EXCEPCIONES Y OTROS ####
#############################
class RaizExcpt(Exception):
	"""Error lanzado si se intenta realizar la raíz cuadrada de un número negativo"""
	def __init__(self, valor):
		self.valor = valor
	def __str__(self):
		return repr(self.valor)

class DataTypeExcpt(Exception):
	"""Error lanzado si el tipo de datos no es reconocido"""
	def __init__(self,valor):
		self.valor = valor
	def __str__(self):
		return repr(self.valor)

def DataType(variable):
	"""Comprueba el tipo de cadena que es la variable
	>>> variable = (1,2,3)
	Tuple"""
	if variable == str(variable):
		return "String"
	elif variable == tuple(variable):
		return "Tuple"
	elif variable == dict(variable):
		return "Dictionary"
	elif variable == list(variable):
		return "List"
	elif variable == int(variable):
		return "Interger"
	elif variable == float(variable):
		return "Float"
	elif variable == bool(variable):
		return "Boolean"
	else:
		raise DataTypeExcpt("Tipo de Datos no reconocido")

#############################
##### FUNCIONES BÁSICAS #####
#############################

def entero(numero):
	"""Comprueba si el número es entero y si es entero lo retorna como tal"""
	if numero%1.0 == 0:
		return int(numero)
	else:
		return float(numero)

def aleatorio(rango):
	"""Genera un número aleatorio dado un rango (tupla)"""
	a = rango[0]
	b = rango[1]
	x = randint(a,b)
	return x

def primos(maximo,minimo=2):
	"""Haya todos los números primos dado un rango
	>>> maximo = 7
	[2,3,5,7]"""

	lista = [2]
	numero = minimo

	while numero <= maximo:
		for i in lista:
			primo = True
			resto = numero % i
			if resto == 0:
				primo = False
				break
		if primo == True:
			lista.append(numero)
		numero = numero + 1
	return lista

def raiz(a):
	"""Raíz cuadrada
	>>> a = 16
	4"""
	if a >= 0:
		r = a**0.5
		return r
	else:
		raise RaizExcpt("Numero Negativo")

def mcd(nums):
	"""Calcula el MCD de dos números
	>>> nums = 3,6
	3"""
	a = int(nums[0])
	b = int(nums[1])
	#Algoritmo de Euclides
	while b != 0:
		k = b
		b = a%b
		a = k
	mcd = a
	return mcd

def mcm(nums):
	"""Calcula el MCM de dos números
	>>> nums = 3,6
	6"""
	a = int(nums[0])
	b = int(nums[1])
	x = a
	y = b
	#Algoritmo de Euclides
	while b != 0:
		k = b
		b = a%b
		a = k
	mcm = (x*y)/a
	return mcm

def sist(sist1,sist2):
	"""Calcula un sistema de ecuaciones ax+by=c dx+ey=f
	>>> sist1 = 5x+y=-2
	>>> sist2 = -x+y=4
	-1,3"""

	def parser(sistema):
		"""Devuelve las variables de un sistema de dos incognitas"""
		sistema = sistema.split("x")
		a = sistema[0]
		if a in ("", "+"):
			a = 1
		elif a in ("-"):
			a = -1
		else:
			a = int(a)
		sistema = sistema[1]
		sistema = sistema.split("y")
		b = sistema[0]
		if b in ("", "+"):
			b = 1
		elif b in ("-"):
			b = -1
		else:
			b = int(b)
		sistema = sistema[1]
		sistema = sistema.split("=")
		c = sistema[1]
		return a,b,c
	sist1 = parser(sist1)
	a = int(sist1[0])
	b = int(sist1[1])
	c = int(sist1[2])
	sist2 = parser(sist2)
	d = int(sist2[0])
	e = int(sist2[1])
	f = int(sist2[2])

	ya = ((a*f)-(d*c))/((a*e)-(d*b))
	xa = (c-(b*ya))/a
	try:
		xb = Fraction((c-(b*ya)),a)
	except:
		xb = str((c-(b*ya))) + "/" + str(a)
	try:
		yb = Fraction(((a*f)-(d*c)),((a*e)-(d*b)))
	except:
		yb = str((a*f)-(d*c)) + "/" + str((a*e)-(d*b))
	return xa,xb,ya,yb

def ec2(ec):
	"""Resuelve ecuaciones de segundo grado ax²+bx=c
	>>> ec = "2x²-7x+3=0"
	30,25"""

	ec = ec.split("=")
	ec = ec[0]

	ec = ec.split("x²")
	a = ec[0]
	if a in ("+",""):
		a = 1
	elif a in ("-"):
		a = -1
	else:
		a = int(a)
	ec = ec[1]

	ec = ec.split("x")
	b = ec[0]
	if b in ("+", ""):
		b = 1
	elif b in ("-"):
		b = -1
	else:
		b = int(b)
	c = int(ec[1])

	discriminante = b**2-(4*a*c)
	if discriminante < 0:
		raise RaizExcept("Discriminante negativo")
	else:
		x1a = (-b+raiz(discriminante))/(2*a)
		try:
			x1b = Fraction((-b+raiz(discriminante)),(2*a))
		except:
			x1b = str((-b+raiz(discriminante))) + "/" + str((2*a))
		x2a = (-b-raiz(discriminante))/(2*a)
		try:
			x2b = Fraction((-b-raiz(discriminante)),(2*a))
		except:
			x2b = str((-b-raiz(discriminante))) + "/" + str((2*a))

		return x1a, x1b, x2a, x2b


def simplificador(ecuacion1):
	"""Función que toma una ecuación ax+by=c y devuelve una tupla con a,b,c
	>>> ecuacion1 = 4x-5y=-74
	4,-5,-74"""
	ecuacion1 = ecuacion1.split("x")
	a = float(ecuacion1[0])
	a = entero(a)
	ecuacion1 = ecuacion1[1]
	ecuacion1 = ecuacion1.split("y")
	b = float(ecuacion1[0])
	b = entero(b)
	ecuacion1 = ecuacion1[1]
	ecuacion1 = ecuacion1.split("=")
	c = float(ecuacion1[1])
	c = entero(c)
	return a,b,c

def simplificador2(ecuacion):
	"""Función que toma una ecuación de segundo grado ax²+bx=c y devuelve una tupla con a,b,c
	>>> ecuacion = 2x²-5x=7
	2,-5,7"""
	ecuacion = ecuacion.split("x²")
	a = float(ecuacion[0])
	a = entero(a)
	ecuacion = ecuacion[1]
	ecuacion = ecuacion.split("x=")
	b = float(ecuacion[0])
	b = entero(b)
	c = float(ecuacion[1])
	c = entero(c)
	return a,b,c

#############################
##### PROPORCIONALIDAD ######
#############################

def regla3(regla3):
	"""Reglas de 3 simples directas. Proporción: 'a' es a 'b' como 'c' a 'x'.
	>>> regla3 = 100,50,10
	5"""
	a = regla3[0]
	b = regla3[1]
	c = regla3[2]
	b = float(b)
	x = (b*c)/a
	return x

def reglainv(a,b,c):
	"""Reglas de 3 simples inversas. Proporción: 'a' es a 'b' como 'c' a 'x'.
	>>> a = 4
	>>> b = 2
	>>> c = 8
	1"""
	x = (float(b)*a)/c
	return x


#############################
######### FÍSICA ############
#############################

def coulomb(desp):
	"""Ley de Coulomb F=(k·q1·q2)/d² -> Desp: letra que el programa debe hallar"""
	print("Ley de Coulomb en el vacío.")
	print("q debe ir expresada en Coulombios.")
	print("d en metros.")
	print("F en Newtons")
	k = float(9e9)
	desp = desp.lower()
	if desp == "f":
		datos = input("Introduce los valores sin unidades de q1,q2,d: ")
		q1 = datos[0]
		q2 = datos[1]
		d = datos[2]
		x = (k*q1*q2)/(d**2)
	elif desp == "q1":
		datos = input("Introduce los valores sin unidades de F,q2,d: ")
		f = datos[0]
		q2 = datos[1]
		d = datos[2]
		x = (f*(d**2))/(k*q2)
	elif desp == "q2":
		datos = input("Introduce los valores sin unidades de F,q1,d: ")
		f = datos[0]
		q1 = datos[1]
		d = datos[2]
		x = (f*(d**2))/(k*q1)
	elif desp == "q":
		datos = input("Introduce los valores sin unidades de F,d: ")
		f = datos[0]
		d = datos[1]
		r = (f*(d**2))/k
		if r >= 0:
			x = raiz(r)
		else:
			raise RaizExcpt("Numero Negativo")
	elif desp == "d":
		datos = input("Introduce los valores sin unidades de F,q1,q2: ")
		f = datos[0]
		q1 = datos[1]
		q2 = datos[2]
		r = (k*q1*q2)/f
		if r >= 0:
			x = raiz(r)
		elif r < 0:
			raise RaizExcpt("Numero Negativo")
	else:
		x = "Los datos especificados no son validos"
	return x


#############################
######## GEOMETRÍA ##########
#############################

def perimetro(l,n):
	"""Perímetro de un polígono regular. P=l·n; n=número de lados
	>>> l = 5
	>>> n = 5
	25"""
	P = l*n
	return P

def longitud(r):
	"""Longitud de una circunferencia. L=2·Pi·r
	>>> r = 3
	18.84955592153876"""
	l = 2*pi*r
	return l

def acuadrado(l):
	"""Área de un cuadrado A=l²
	>>> l = 4
	16"""
	a = l**2
	return a

def arectangulo(b,h):
	"""Área de un rectángulo A=b·h
	>>> b = 2
	>>> h = 3
	6"""
	a = b*h
	return a

def atriangulo(b,h):
	"""Área de un triángulo A=(b·h)/2
	>>> b = 2
	>>> h = 3
	3"""
	a = (b*h)/2.0
	return a

def arombo(D,d):
	"""Área de un rombo A=(D·d)/2 ; D=Diagonal mayor ; d=diagonal menor
	>>> D = 2
	>>> d = 3
	3"""
	a = (D*d)/2.0
	return a

def atrapecio(B,b,h):
	"""Área de un Trapecio A=((B+b)·h)/2 ; B=Base mayor ; b=base menor
	>>> B = 2
	>>> b = 4
	>>> h = 2
	6"""
	a = ((B+b)*h)/2.0
	return a

def apoligono(P,a):
	"""Área de un Polígono regular. A=(P·a)/2 ; P=Perímetro ; a=apotema
	>>> P = 8
	>>> a = 1
	4"""
	A = (P*a)/2.0
	return A

def acirculo(r):
	"""Área de un círculo. A=Pi·r²
	>>> r = 2
	12.566370614359172"""
	a = pi*(r**2)
	return a

def pitagoras(desp):
	"""Teorema de Pitágoras a²=b²+c². Escribir la letra a hallar (desp)"""
	desp = desp.lower()
	if desp == "a":
		b = input("Introduce el valor de 'b': ")
		c = input("Introduce el valor de 'c': ")
		r = (b**2.0)+(c**2)
		if r >= 0:
			x = raiz(r)
		else:
			raise RaizExcpt("Numero Negativo")
	elif desp == "b":
		a = input("Introduce el valor de 'a': ")
		c = input("Introduce el valor de 'c': ")
		r = (a**2.0)-(c**2)
		if r >= 0:
			x = raiz(r)
		else:
			raise RaizExcpt("Numero Negativo")

	elif desp == "c":
		a = input("Introduce el valor de 'a': ")
		b = input("Introduce el valor de 'b': ")
		r = (a**2.0)-(b**2)
		if r >= 0:
			x = raiz(r)
		else:
			raise RaizExcpt("Numero Negativo")
	return x

def test():
	from doctest import testmod
	testmod()
