#!/usr/bin/python3
# -*- coding: utf-8 -*-
#


from math import sqrt, pi, atan

a = float(input("Comprimento do cateto A: "))
b = float(input("Comprimento do cateto B: "))
print ()

# Hipotenusa = Raíz quadrada de cateto A ao quadrado + cateto B ao quadrado
h = sqrt(a**2 + b**2)

print ("O comprimento da hipotenusa é", h)
print ()

theta  = atan(b/a)
ang = round(theta * 180 / pi)

print ("O ângulo formado entre A e a hipótenusa é", str(ang) + "º")
print ()
