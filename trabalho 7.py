def soma_e_media(lista):
  soma = sum(lista)
  media = soma / len(lista)
  return soma, media

lista = [17, 22, 30, 14]
soma, media = soma_e_media(lista)

print(f"Soma da lista: {soma}")
print(f"Média da lista: {media}")


def substituicao(lista, palavra, substituta):
    for i in range(len(lista)):
        if (lista[i] == palavra):
            lista[i] = substituta
    return lista
print(substituicao(["abacaxi", "banana", "morango", "limao"], "banana", "pitangatuba"))

def triangulo(linhas):
    for linha in range(linhas):
         print("*" *(linha+1))
         
triangulo(4)