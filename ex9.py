#!/usr/bin/python3
# -*- coding: utf-8 -*-
#


hora = 6
minuto = 52

inicio = hora*60*60+minuto*60
anda = 1*10*60
treino = 3*6*60
volta = 4*10*60

total = inicio + anda + treino + volta
m, s = divmod(total, 60)
h, m = divmod(m, 60)

print ("Começo a tomar o pequeno almoço às", str(h) + ":" + f'{m:02d}' +".")
