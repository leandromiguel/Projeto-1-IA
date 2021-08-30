from regras import regras
from elevador import Elevador


e = Elevador()

print('Andar atual: 1')

while True:
    andarEscolhido = input('Informe o andar ou uma sequência de andares: ')
    e.chamadaElevador(andarEscolhido)
    e.funcoes()