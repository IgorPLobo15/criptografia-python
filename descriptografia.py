import collections

alfabeto = collections.deque('abcdefghijklmnopqrstuvwxyz')
alfabeto_rotacionado = alfabeto.copy()
alfabeto_rotacionado.rotate(-3)
mensagem = input('Coloque sua Mensagem:')
mensagem_decifrada = ''
for letra in mensagem:
    if letra in alfabeto:
        posicao_alfabeto = alfabeto.index(letra)
        mensagem_decifrada += alfabeto_rotacionado[posicao_alfabeto]''' '''''
    else:
        mensagem_decifrada += letra

print((mensagem_decifrada).replace('8','ã'))