#!/usr/bin/python
#coding: utf-8

#        |                      MateX                    |
#        |                      v 0.2                    |
#        |                Licencia GNU GPLv3             |
#        |              ©Guillemo Gómez Fonfría          |



#Módulos
import helplib
import main
import gui
from sys import argv

try:
	args = argv[1]
except:
	main.main()

if args in ("-h", "--help"):
	helplib.help_en()
elif args in ("-a", "--ayuda"):
	helplib.ayuda_es()
elif args in ("-c", "--cli"):
	main.main()
elif args in ("-g", "--gui"):
	gui.main()
else:
	helplib.help_en()
