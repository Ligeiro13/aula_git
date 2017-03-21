#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:46:32 2017

@author: gabrielligeiro
"""
n = int(input("Digite um numero: "))
def ler_numeros(n):
    lista = []
    for i in range(n):
        a = int(input("Digite um numero da lista"))
        lista.append(a)
    return lista