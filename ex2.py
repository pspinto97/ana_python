#!/usr/bin/python3
# -*- coding: utf-8 -*-
#


def calculo(et1, et2):
    """
    d = 2, uma vez que a distância é igual em ambas as etapas
    Tempo gasto na ida t1 = d/et1, volta t2 = d/et2 (d = 1)
    Logo a velociade média no total é 2d/(t1 + t2)
    Devolve a velocidade média total
    """

    t1 = 1/et1
    t2 = 1/et2

    return 2/(t1+t2)


v1 = int(input("Introduza a velocidade média da 1ª etapa: "))
v2 = int(input("Introduza a velocidade média da 2ª etapa: "))

media = calculo(v1, v2)

#Valor inteiro arredondado por excesso
print ()
print ("A velocidade média de transporte é de", int(round(media)),"km/h")
