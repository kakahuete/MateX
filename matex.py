#!/usr/bin/python
#coding: utf-8

#        |                      MateX                    |
#        |                      v 0.2                    |
#        |                Licencia GNU GPLv3             |
#        |              ©Guillemo Gómez Fonfría          |


#Módulos
import matex
from sys import argv

try:
    args = argv[1]
except:
    matex.main.main()

if args in ("-h", "--help"):
    matex.helplib.help_en()
elif args in ("-a", "--ayuda"):
    matex.helplib.ayuda_es()
elif args in ("-c", "--cli"):
    matex.main.main()
elif args in ("-g", "--gui"):
    matex.gui.main()
else:
    matex.helplib.help_en()
