#!/usr/bin/python3
# -*- coding: utf-8 -*-
#


def calcula_km():
    """
    Total dos 3 andares = 9m
    Andar 1 = 3, Andar = 2, Andar = 3
    1 morador por andar * 2 utilização
    Devolve o resultado em metros
    """

    # Andar(n) = Número * metros * moradores * utilizações
    andar1 = 1*3*1*2
    andar2 = 2*3*1*2
    andar3 = 3*3*1*2

    return (andar1 + andar2 + andar3) * 365



def calcula_tempo(temp):
    """
    Recebe como parâmetro o resultado da função calcula_km
    Tempo = distância / velocidade
    Devolve o tempo em segundos
    """

    return temp/1

km = calcula_km()/1000
m = calcula_tempo(calcula_km())/60
h, m = divmod(m, 60)

print ()
print ("Num ano o elevador percorre", str(km) + "km.")
print ("Num ano o elevador trabalha durante", str(h) + "H", str(m) + "M")
print()
