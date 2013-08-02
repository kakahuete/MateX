#coding: utf-8

#        |                 MateX HelpLibrary             |
#        |                      v 0.2                    |
#        |                Licencia GNU GPLv3             |
#        |              ©Guillemo Gómez Fonfría          |

#Módulos/librerías
from sys import exit
from sys import argv
from os import system
from time import sleep

#Español
def ayuda_es():
	print("Uso: " + argv[0] + " [ARGUMENTOS]\n")
	print("ARGUMENTOS:")
	print("\t'-a'  '--ayuda'\tMuestra esta ayuda y finaliza")
	print("\t'-h'  '--help'\tThis menu writen in English")
	print("\t'-c'  '--cli'\tInicia el programa (CLI)")
	print("\t'-g'  '--gui'\tInicia la interfaz gráfica")
	print("\n")
	print("'--cli' es el valor por defecto, si ningún otro es especificado")
	exit()

def ayuda2_es():
	print("Interfaz MateX-0.2 (CLI)")
	print("Escribe 'comandos' para una lista completa de comandos")
	print("La interfaz MateX está diseñada para proporcionar la mayor facilidad posible en la interacción entre el usuario y la librería MateX")

def instalar_es():
	print("Instalando los módulos necesarios...\n")
	system("sudo cp matexlib.py /usr/lib/python2.7/matexlib.py")
	sleep(2)
	print("Se han creado los siguientes archivos:")
	print(" * /usr/lib/python2.7/matexlib.py")
	sleep(1)
	print("¡Instalación completada!")


comandos = {"salir:":"Sale de MateX",
		"ayuda:":"Muestra un texto de ayuda",
		"iAyuda":"Accede a la ayuda interactiva",
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

#English
def help_en():
	print("Usage: " + argv[0] + " [OPTIONS]\n")
	print("OPTIONS:")
	print("\t'-h'  '--help'\tPrints this help menu")
	print("\t'-a'  '--ayuda'\tEste menú de ayuda en castellano")
	print("\t'-c'  '--cli'\tRuns the program (CLI)")
	print("\t'-g'  '--gui'\tRuns the program (GUI)")
	print("\n")
	print("'--cli' is the default value, if any is specified")
	exit()

def help2_en():
	print("MateX-0.2 CLI Interface")
	print("Type 'commands' to get a full list with the internal commands")
	print("The MateX interface is designed to offer the most possible ease of use regarding to the interaction between the use and MateX library")

def install_en():
	print("Installing MateXlib...\n")
	system("sudo cp matexlib.py /usr/lib/python2.7/matexlib.py")
	sleep(2)
	print("The following files were created:")
	print(" * /usr/lib/python2.7/matexlib.py")
	sleep(1)
	print("Instalation completed!")


commands = {"exit:":"Exits MateX",
		"help":"Shows the help menu",
		"iHelp":"Runs the interactive help menu",
		"install":"Installs MateX library (MateXlib)",
		"commands":"Shows a list with the recognized internal commands",
		"debugging":"For developers only",
		"random":"Prints a random number given a range",
		"sqroot":"Calculates the square root of the number given",
		"gcd":"Calculates the GCD of two given numbers",
		"lcm":"Calculates the LCM of two given numbers",
		"system":"Solves a system of two linear equations ax+by=c} dx+ey=f}",
		"quadratic":"Solves a quadratic equation",
		"cross":"Solves a rule of three (cross-multiplication)",
		"coulomb-law":"Calculates any variable that appears in Coulomb's law",
		"perimeter":"Calculates the perimeter of a regular polygon",
		"circumference":"Calculates the circumference of a given circle",
		"asquare":"Calculates the area of a given square",
		"arectangle":"Calculates the area of a given rectangle",
		"atriangle":"Calculates the area of a given triangle",
		"arhombus":"Calculates the area of a given rhombus",
		"atrapezium":"Calculates the area of a given trapezium",
		"apolygon":"Calculates the area of a given polygon",
		"acircle":"Calculates the area of a given circle",
		"Pythagorean":"Works with the Pythagorean theorem"}

