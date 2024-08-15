# projeto_transacoes_bancarias -- DS-PY-17 - logica de programacao II
# readme link here:
# https://github.com/allansuzuki/ADA_classes/blob/main/DS-PY-Data-Science/DS-PY-017%20L%C3%93GICA%20DE%20PROGRAMA%C3%87%C3%83O%20II%20(PY)/Material%20do%20Aluno/projeto_README.md
#
# Esse programa é um sistema de gestao de transacoes de uma conta bancária pessoal
# no qual os dados são de transações e possuem seu valor, a categoria do gasto e seu ID.
#
# Teu objetivo é completar esse sistema CRUD (Create-Read-Update-Delete) simples
# para ver dados de transacao da tua conta pessoal, criar, editar e excluir transações.
# Também deve fazer com que o programa NUNCA pare, ou seja,
# caso ocorra um possível erro, deve validar as entradas, detectar erros e avisar o usuário
# mas o programa não deve parar.
#
#
# Notas importantes:
# 1. As funções que geram os dados e criam a interface do sistema já estão prontas.
# por favor não as altere.
#
# 2. Depois das funções do sistema estão as funções do programa
# No qual podem alterar à vontade, exceto o nome das funções
# Ou seja, podem criar funções, adicionar ou remover parâmetros,
# mas não alterar o nome das funções existentes.
#
# 3. Coloque opções de navegabilidade em cada janela que o usuário estiver.
# Por exemplo, se ele escolher a opcao "alterar transacao" sem querer, tem que ter a opcao de voltar para a tela anterior ou inicial.
#
# 4. Caso por qualquer motivo queira os dados originais novamente,
# apage o json `transactions` na pasta `data` e inicie o programa novamente para gerar os dados.
# Os valores serão os mesmos, porém os UUID NÃO serão os mesmos!!
#
# Critérios (pontos):
#   tarefas validacoes  total
# C     10      15       25
# R     25      25       50
# U     10      10       20
# D     2.5     2.5      5
#
#
# Boa sorte e divirtam-se :)
# ------------------------------------------------------------------------------
# -----------------------
# depencies
# -----------------------
import json
import os
import uuid
import random
import sys

# -----------------------
# load settings
# -----------------------
sys.path.append('./data/')
from data import settings

# -----------------------
# SYSTEM functions
# -----------------------
# não alterar nada das funções de system
def criar_transacoes(num_transacoes, proporcao_categorias, seed=settings.seed):
    assert sum([proporcao_categorias[k] for k in proporcao_categorias])==1, '`proporcao_categorias` não soma 100%! Favor rever.'

    # garantir reprodutibilidade dos valores
    random.seed(seed)

    # Calcula o número de transações por categoria com base na proporção
    numero_transacoes_por_categoria = {categoria: int(num_transacoes * proporcao) for categoria, proporcao in proporcao_categorias.items()}

    transacoes = []

    # Gera as transações
    for categoria, quantidade in numero_transacoes_por_categoria.items():
        for _ in range(quantidade):
            transacao = {
                "UUID": str(uuid.uuid4()),
                "valor": round(random.uniform(1.0, 1000.0), 2),  # Preço aleatório entre 1 e 1000
                "categoria": categoria
            }
            transacoes.append(transacao)

    return transacoes

def salvar_json(transacoes, path2save, filename):
    # create path if not exist
    if not os.path.exists(path2save):
        os.makedirs(path2save)
    with open(os.path.join(path2save,filename), "w") as file:
        json.dump(transacoes, file, indent=4)
    print(f"Arquivo salvo em: {os.path.abspath(os.path.curdir)+'/'+path2save+'/'+filename}")

def criar_bd(num_transacoes:int = 10000, proporcao_categorias:list = settings.categorias_proporcao, path2save="./data", filename='transactions.json'):
    salvar_json(criar_transacoes(num_transacoes,  proporcao_categorias),
                path2save, filename
    )

def load_bd(filepath='./data/transactions.json'):
    with open(filepath, "r") as file:
        bd = json.load(file)
    return bd

def tela_inicial():
    print("Bem-vindo <teu nome inteiro aqui>!")
    print('conta: 0000001-0')
    print("\nEste programa permite gerenciar transações de sua conta pessoal.")
    print("\nEscolha uma das opções abaixo:")
    print("1. Visualizar relatórios")
    print("2. Cadastrar transações")
    print("3. Editar transações")
    print("4. Excluir transações")
    print("-" * 10)
    print("0. Sair")
    print('\n')

# -----------------------
# PROGRAM functions
# -----------------------
# pode editar como quiser as funções abaixo! Somente não altere os nomes das funções.
# para alterar as funções abaixo, basta apagar o `pass` e preencher com as instruções.

# Funções Auxiliares:

# Menu escolhendo a opçao 1:
def menu_visualizar_relatorios():
        
        print("Opções de Relatórios:")
        print("1. Exibir soma total de transações")
        print("2. 5 transações mais caras")
        print("3. 5 transações medianas")
        print("4. 5 transações mais baratas")
        print("5. Exibir média total")
        print("6. Consultar transação por ID")
        print("-" * 10)
        print("0. Voltar ao menu inicial")
        print('\n')

# Menu de categorias
def lista_categorias():

        print("1. Alimentação")
        print("2. Casa")
        print("3. Investimentos")
        print("4. Lazer")
        print("5. Saúde")
        print("6. Transferências")
        print("7. Viagens")
       #print("8. Outros")
        print("-" * 10)
        print("0. Voltar ao menu inicial")
        print('\n')

# Função para selecionar as categorias
def selecao_categoria(num):
    
    try:

        if num == "1":
            categoria = "alimentacao"
            return categoria
        elif num == "2":
            categoria = "casa"
            return categoria
        elif num == "3":
            categoria = "investimentos"
            return categoria
        elif num == "4":
            categoria = "lazer"
            return categoria
        elif num == "5":
            categoria = "saude"
            return categoria
        elif num == "6":
            categoria = "transferencias"
            return categoria
        elif num == "7":
            categoria = "viagens"
            return categoria
        elif num == "0":
            print("Voltando ao menu anterior...")   
        else:
            print("Opção inválida, tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione Enter para continuar...")
        

# Função principal        
def run():
    """
    Esta é a função principal que vai rodar o programa
    """
    while True:
        try:
            tela_inicial()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                visualizar_relatorios()
            elif opcao == "2":
                cadastrar_transacao()
            elif opcao == "3":
                editar_transacao_por_ID()
            elif opcao == "4":
                excluir_transacao()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente.")

            input("Pressione Enter para continuar...")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            input("Pressione Enter para continuar...")


def visualizar_relatorios():
    """
    Mostra um menu de opcoes no qual gera relatórios com base na escolha do usuário.
    """
    while True:
        
        menu_visualizar_relatorios()
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            calcular_total_transacoes()
        elif opcao == "2":
            mostrar_m5_transacoes('max')
        elif opcao == "3":
            mostrar_m5_transacoes('median')
        elif opcao == "4":
            mostrar_m5_transacoes('min')
        elif opcao == "5":
            calcular_media()
        elif opcao == "6":
            consultar_transacao_por_ID()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

        input("Pressione Enter para continuar...")

def salvar_relatorio(nome_relatorio, conteudo):
    """
    Salvar o relatório gerado em .txt
    Aplicar esta função em todos os relatórios listados em `visualizar_relatorios`
    """
    try:
        caminho_relatorio = f'{nome_relatorio}.txt'
        
        with open(caminho_relatorio, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        
        print(f'Relatório salvo com sucesso em {caminho_relatorio}')
    except Exception as e:
        print(f'Erro ao salvar o relatório: {e}')

def calcular_total_transacoes():
    """
    Calcula o valor total de transações da conta.
    Utilize essa mesma função para o caso `por categoria`
    """
    try:
        lista_categorias()
        categoria = input("Digite o número da categoria: ")
        escolhida = selecao_categoria(categoria)
        # TEM QUE ARRUMNAR AQUI PRA ELE SOMAR SÓ PRA CADA CATEGORIA
        # FILTRO DE CATEGORIA ARRUMADO - ALINE
        if escolhida != None:
            total = sum(transacao['valor'] for transacao in bd if transacao['categoria'] == escolhida)
            relatorio = (f"Total das transações da categoria {escolhida}: R$ {total:.2f}")
            print(relatorio)

        # Salvando o relatório
            nome_relatorio = f'total_transacoes_categoria_{escolhida}'
            salvar_relatorio(nome_relatorio, relatorio)
        else:
            pass
    except Exception as e:
        print(f"Ocorreu um erro ao calcular o total das transações: {e}")

def mostrar_m5_transacoes(m):
    """
    Mostra as m5 transações realizadas, sendo m parâmetro que deve ser adicionada à função.
    \nm : 'max','min','median', sendo
    \n\t'max' mostra os top 5 maior valor,
    \n\t'min' mostra os top 5 menor valor,
    \n\t'mean' mostra os top 5 valores próximos a média

    Utilize essa mesma função para o caso `por categoria`
    """
    try:
        if m == 'max':
            transacoes = sorted(bd, key=lambda x: x['valor'], reverse=True)[:5]
        elif m == 'min':
            transacoes = sorted(bd, key=lambda x: x['valor'])[:5]
        elif m == 'median':
            total = sum(transacao['valor'] for transacao in bd)
            media = total / len(bd)
            transacoes = sorted(bd, key=lambda x: abs(x['valor'] - media))[:5]
        else:
            raise ValueError("Opção inválida para 'm'.")

        for transacao in transacoes:
            print(transacao)

    except Exception as e:
        print(f"Ocorreu um erro ao mostrar as transações: {e}")

def calcular_media():
    """
    Calcula a média dos valores das transações.
    Utilize essa mesma função para o caso `por categoria`
    """
    try:
        total = sum(transacao['valor'] for transacao in bd)
        media = total / len(bd)
        print(f"Média das transações: R$ {media:.2f}")
        return media
    except Exception as e:
        print(f"Ocorreu um erro ao calcular a média das transações: {e}")
        return 0

def consultar_transacao_por_ID():
    """
    Consulta uma transação específica pelo seu UUID.
    """
    opcao = input("Digite o ID da Transação: ")

    transacao_solicitada = list((transacao for transacao in bd if transacao['UUID'] == opcao))

    print(f"Transação:{transacao_solicitada[0]['UUID']}")
    print(f"Valor:{transacao_solicitada[0]['valor']}")
    print(f"Categoria:{transacao_solicitada[0]['categoria']}")


    pass

def cadastrar_transacao():
    """
    Cadastra uma nova transação.
    \nObs:Para gerar um novo uuid, veja como é feito na função `criar_transacoes`.
    """
    print("Cadastro de Novas Transações")
    print("")

    lista_categorias()

    numero_categoria = input("Digite a número da categoria:")
    categoria = selecao_categoria(numero_categoria)

    transacao = {
        "UUID": str(uuid.uuid4()),
        "valor": float(input("Digite o valor:")),
        "categoria": categoria
    }
    
    bd.append(transacao)

    salvar_json(bd, path2save="./data", filename='transactions.json')
    
    pass


def editar_transacao_por_ID():
    """
    Edita uma transação específica pelo seu UUID.
    """
    pass

def excluir_transacao():
    """
    Exclui uma transação específica pelo UUID.
    """
    pass

# -----------------------
# MAIN SCRIPT
# -----------------------
# não alterar nada abaixo
if __name__ == "__main__":

    # -----------------------
    # NÃO ALTERAR ESTE BLOCO
    # -----------------------
    # criar o banco de dados caso ele não exista
    print(os.path.abspath('.'))
    if not os.path.exists('./data/transactions.json'):
        criar_bd()

    # load bd
    bd = load_bd()
    # -----------------------

    # -----------------------
    # ABAIXO PODE ALTERAR
    # -----------------------
    #limpar console (opcional)
    os.system('cls' if os.name == 'nt' else 'clear')
    # inicia o programa
    run()
