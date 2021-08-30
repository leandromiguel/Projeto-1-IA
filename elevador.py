from regras import regras
import time

class Elevador():
    def __init__(self):
        self.andar = 1
        self.destino = None
        self.deslocamento = False
        self.fila = []
    
    def chamadaElevador(self, andar):
        self.fila.extend(andar.strip().split(' ')) #Anexa as chamadas a lista.
    
    def statusElevador(self):
        return regras(str(self.andar), str(self.destino)) #consulta as regras passando andar atual e andar destino e retorna a mensagem indicamdo o destino do elevador

    def funcoes(self):
        while self.fila:
            self.destino = int(self.fila.pop(0)) #Remove o item da fila e devolve o item no índice
            print('Status do elevador: {}\n'.format(self.statusElevador()))

            if self.andar != self.destino: #se o andar escolhido for diferente do andar destino
                print('Elevador em movimento...')
                self.deslocamento = True #seta deslocamento como Ttue
                time.sleep(2) #dá delay de 2 segundos
                self.andar = self.destino #atribui destino a variavel andar
                print('Andar atual do elevador: {}\n'.format(self.andar)) #exibe a menságem com o andar atual