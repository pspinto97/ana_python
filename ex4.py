#!/usr/bin/python3
# -*- coding: utf-8 -*-
#


import datetime

tempo = int(input("Introduza os segundos: "))

print ("Resultado com recurso a bibliotecas")
print (str(datetime.timedelta(seconds=tempo)))
print ()


print ("Resultado com recurso ao divmod")
m, s = divmod(tempo, 60)
h, m = divmod(m, 60)
print ('{:d}:{:02d}:{:02d}'.format(h, m, s))
print ()


print ("Forma básica")
segundos    = tempo % 60
minutos     = tempo // 60
horas       = minutos // 60
#Em princípio este print só funciona da versão 3.6+
print (f'{horas:d}:{minutos:02d}:{segundos:02d}')
