import random 

def advinhe_o_numero():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    acertou = False 
    print("advinhe o número entre 1 e 100")
    
    while not acertou :
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite < numero_aleatorio :
            print("Muito baixo!")
        elif palpite > numero_aleatorio:
            print("Muito alto!")
        else:
            print(f"Você advinhou em {tentativas} tentativas.")
            acertou = True


def sorteio_premios():
    premios = ["Carro", "Viagem", "Notebook", "Smartphone"]
    participante = input("Digite seu nome: ")
    premios = random.choice(premios)
    print(f"Parabéns, {participante} ! Você ganhou um(a) {premios}")
    
import random

def lancar_dado():
  """
  Simula o lançamento de um dado de 6 lados e retorna o resultado.
  """
  numero = random.randint(1, 6)
  print(f"O resultado do lançamento foi: {numero}")
