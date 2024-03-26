
def soma_e_media(lista):
  soma = sum(lista)
  media = soma / len(lista)
  return soma, media

lista = [17, 22, 30, 14]
soma, media = soma_e_media(lista)

print(f"Soma da lista: {soma}")
print(f"Média da lista: {media}")

def substituir_palavra(lista_palavras, palavra_busca, palavra_substituicao):
    lista_palavras: Uma lista de palavras
    lista_busca: A palavra deve ser substituída
    palavra_substituicao: A palavra que deve substituir a palavra_busca
    return uma nova lista com as palavras substituidas

nova_lista = []
for palavra in lista_palavras:
    if palavra == palavra_busca:
        nova_lista.append(palavra_substituicao)
    else:
        nova_lista.append(palavra)
    return nova_lista

lista_palavras = ["banana", "morango", "limão", "banana", "maçã"]
palavra_busca = "banana"
palavra_substituição = "abacaxi"
nova_lista = substituir_palavra(lista_palavras, palavra_busca, palavra_substituicao)
print(f"Lista original: {lista_palavras}")
print(f"novalista: {novalista}")
