# -*- coding: utf-8 -*-
"""STexto: lira@gmail.com

-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  l   i   r   a   @  g  m  a  i  l  .  c  o  m
  0   1   2   3   4  5  6  7  8  9 10 11 12 13
  
-25  -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
  t   i   a   g   o   s   a   n   t   o   s   0   4   1   2   @   g   m   a   i   l   .   c   o   m
  0   1   2   3   4   5   6   7   8   9   1   11  12  13  14  15  16  17  18  19  20  21  22  23  24
  
  
Para pegar um texto de trás para frente: texto[índice] -> onde índice é negativo
Para pegar o pedaço de um texto use : (dois pontos). texto[:indice] ou texto[indice:] ou ainda texto[indice:indice]
"""

email = 'tiagosantos0412@gmail.com'
nome = 'Tiago Felipe dos Santos'

print(email[0:15])'

"""Exercícios para Fixação:
Basta completar os prints de forma correta
"""

print('Tamanho do e-mail ' + str(len(email)) + ' caracteres')
print('Primeiro Caractere ? ' + email[0])
print('Último Caractere ? ' + email[24])
print('Servidor do email ? ' + email[15:])