def ler_dados_do_arquivo(nome_arquivo):
    dados = []
    with open(nome_arquivo, 'r', encoding = 'utf-8') as arquivo:
        cabecalho = arquivo.readline().strip().split(',')
        for linha in arquivo:
            linha = linha.strip().split(',')
            dado = {
                cabecalho[0]: linha[0], #Cliente
                cabecalho[1]: int(linha[1]), #Caso
                cabecalho[2]: float(linha[2]), #Despesa
                cabecalho[3]: float(linha[3]), #Receita
            }
            dados.append(dado)
    return dados

#  1 solicitar ao usuário a parte de um nome e imprima na tela os 
# nomes de clientes existentes no arquivo cujos nomes possuam o texto informado (sem repetição)

def buscar_cliente_por_nome(dados, parte_nome):
    resultados = []
    for dado in dados:
        if parte_nome.lower() in dado["Cliente"].lower():
            if dado["Cliente"] not in resultados:
                resultados.append(dado["Cliente"])
    return resultados

# 2 solicitar ao usuário o nome completo de um cliente e
# imprima na tela o(s) número(s) do(s)caso(s) associado(s) a ele;


def buscar_cliente(dados, nome):
    cliente_s = []
    for dado in dados:
        if  nome.lower() ==  dado["Cliente"].lower():
            cliente_s.append(dado)
    return cliente_s

def buscar_cliente_caso(dados, nome):
    casos_nome = []
    cliente = buscar_cliente(dados, nome)
    for dado in cliente:
        casos_nome.append(dado["Caso"])
    return casos_nome

# 3 solicite ao usuário um número de caso e informe (imprima na tela) o nome do cliente, a 
# despesa, a receita e a diferença entre receita e a despesa do caso

def buscar_informacao_caso(dados, caso):
    for dado in dados:
        if caso == str(dado["Caso"]):
            lucro = dado["Despesa"] - dado["Receita"]
            d = {
                "Cliente": dado["Cliente"],
                "Despesa": dado["Despesa"],
                "Receita": dado["Receita"],
                "Lucro": lucro 
            }
            return d

# 4 imprimir na tela a despesa total;

#  5 imprimir na tela a despesa total;

def calcular_total(dados, referencia):
    total = 0.0

    for dado in dados:
        total += dado[referencia]    
    return round(total,2) 

#  6 imprimir na tela o nome do cliente, número, receita e despesa do caso com a maior despesa;

def maior_despesa(dados):
    caso_despesa_max = dados[0]
    despesa_max = dados[0]["Despesa"] 
    for dado in dados:
        if dado["Despesa"] > despesa_max:
            despesa_max = dado["Despesa"]
            caso_despesa_max = dado
    return caso_despesa_max
     
#  7 imprimir na tela o nome do cliente, número, receita e despesa do caso com a maior receita;

def maior_receita(dados):
    caso_receita_max = dados[0]
    receita_max = dados[0]["Receita"] 
    for dado in dados:
        if dado["Receita"] > receita_max:
            receita_max = dado["Receita"]
            caso_receita_max = dado
        return caso_receita_max

# 8  solicitar ao usuário o nome completo de um cliente e grave um arquivo contendo o nome do
# cliente, os números, as receitas e despesas de cada caso associado a ele, além de conter o total
# de despesas, receitas e a diferença entre esses totais.

def gravar_dados_cliente(dados, nome_completo):
    
    cliente = buscar_cliente(dados, nome_completo)
        
    if len(cliente) == 0:
        return False

    nome_cliente = cliente[0]['Cliente'].replace(" ", "_")
    nome_arquivo = f"./Clientes/{nome_cliente}_dados.txt"
    
    caso_string = " "
    for c in cliente:
        caso_string += f"""        
        Caso {c['Caso']}
            Despesas: {c['Despesa']}
            Receitas: {c['Receita']}
            
        """
    total_despesa = calcular_total(cliente,"Despesa")
    total_receita = calcular_total(cliente,"Receita")
    diferenca = total_receita - total_despesa

    conteudo = f"""
    Nome do Cliente: {nome_completo}
    
    Casos:
    {caso_string}
    
    Total de Despesas: {total_despesa}
    Total de Receitas: {total_receita}
    Diferença entre Totais: {round(diferenca,2)}
    """

    with open(nome_arquivo, 'w', encoding = 'utf-8') as arquivo:
        arquivo.write(conteudo)
    return True     
           
def menu():

    registros = ler_dados_do_arquivo('registro.txt')

    while(True):
        print("1 - Buscar clientes por parte do nome")
        print("2 - Buscar casos por nome completo do cliente")
        print("3 - Buscar detalhes do caso por número")
        print("4 - Imprimir a Despesa Total")
        print("5 - Imprimir a Receita Total")
        print("6 - Cliente com maior despesa")
        print("7 - Cliente com maior receita")
        print("8 - Gravar dados de cliente em arquivo")
        print("0 - Sair")
        
        resp = input("Escolha uma Opção: ")

        try:
            resp = int(resp)
        except ValueError:
            print("Opção nao encontrada.")
            continue
        
        if(resp==0):
            print("Saindo..")
            break
        
        elif(resp==1):
            nome = input('Insira o nome do Cliente: ')
            nome_buscado = buscar_cliente_por_nome(registros,nome)
            if nome_buscado : 
                print("Clientes encontrados:")
                for i in nome_buscado :
                    print(i)
            else : print("Nome não encontrado.")
            
        elif(resp==2):
            nome_completo = input('Insira o nome completo do Cliente: ')
            casos_nome = buscar_cliente_caso(registros,nome_completo)
            if casos_nome:
                print("Casos encontrados: ")
                for i in casos_nome:
                    print(i)
            else : print("Caso não encontrado.")
        
        elif(resp==3):
            caso_buscado = input('Informe o numero do Caso: ')
            caso = buscar_informacao_caso(registros,caso_buscado)
            if caso:
                print("Cliente: ",caso["Cliente"],"Despesa: ", caso["Despesa"],"Receita: ",
                    caso["Receita"],"Diferenca da receita e despesa: ",caso["Lucro"])        
            else: print("Sem informcao para esse numero de caso.")    
        
        elif(resp==4):
            despesas_total = calcular_total(registros,"Despesa") 
            print('Total de Despesa da Agencia: ', despesas_total)
            
        elif(resp==5):
            receita_total = calcular_total(registros, "Receita") 
            print('Total de Receita da Agencia: ', receita_total)
        
        elif(resp==6):
            maxima_despesa = maior_despesa(registros) 
            if maxima_despesa:
                print(maxima_despesa)
            else: print("Cliente com maior despesa não encontrado. ")
        
        elif(resp==7):
            maxima_receita = maior_receita(registros)
            if maxima_receita:
                print(maxima_receita)
            else: print("Cliente com maior receita não encontrado. ")
        
        elif(resp==8):
            nome_completo = input('Insira o nome completo do Cliente: ')
            todos = gravar_dados_cliente(registros, nome_completo)
            if todos:
                print("Cliente encontrado! Seu arquivo foi gerado com sucesso.")
            else: print("Cliente não encontrado. ")
            
        else: print("Opção não encontrada.")
        
if __name__ == "__main__":
    menu()