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

# Função que pausa o programa e limpando o console
def digite_para_continuar():
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

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
        print("8. Todas")
        print("-" * 10)
        print("0. Voltar ao menu inicial")
        print('\n')

# Menu de categorias para o cadastro
def lista_categorias_cadastro():

        print("1. Alimentação")
        print("2. Casa")
        print("3. Investimentos")
        print("4. Lazer")
        print("5. Saúde")
        print("6. Transferências")
        print("7. Viagens")
        print("-" * 20)
        print("0. Voltar ao menu inicial")
        print('\n')

# Função para selecionar as categorias
def selecao_categoria(num):
    categorias = {
        "1": "alimentacao",
        "2": "casa",
        "3": "investimentos",
        "4": "lazer",
        "5": "saude",
        "6": "transferencias",
        "7": "viagens",
        "8": "todas"
    }

    try:
        if num in categorias:
            return categorias[num]
        elif num == "0":
            print("Voltando ao menu anterior...")
            return None
        else:
            print("Opção inválida, tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        digite_para_continuar()

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

            digite_para_continuar()

        except IndexError:
            print("Ocorreu um erro, verifique se digitou o ID correto")
            digite_para_continuar()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            digite_para_continuar()


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
            digite_para_continuar()


def salvar_relatorio(nome_relatorio, conteudo):
    """
    Salvar o relatório gerado em .txt
    Aplicar esta função em todos os relatórios listados em `visualizar_relatorios`
    """
    while True:
        print('\n')
        print("-" * 10)
        
        # Pergunta se o usuário quer salvar ou não o relatório
        deseja_salvar = input("Deseja salvar o relatório? (y/[n]): ").strip().lower()
        
        # Condições para o salvamento do relatório
        if deseja_salvar == 'y':
            try:
                caminho_relatorio = f'{nome_relatorio}.txt'
                
                with open(caminho_relatorio, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(conteudo)
                
                print(f'Relatório salvo com sucesso em "{caminho_relatorio}"')
                break
            
            except FileNotFoundError:
                print('Erro: O diretório especificado não foi encontrado.')
                break
            except PermissionError:
                print('Erro: Permissão negada para salvar o relatório no diretório especificado.')
                break
            except IOError as e:
                print(f'Erro de I/O ao salvar o relatório: {e}') # Erro de acesso ao sistema, erro de disco, etc
                break
            except Exception as e:
                print(f'Erro inesperado ao salvar o relatório: {e}')
                break
            
        elif deseja_salvar == 'n':
            print('Salvamento do relatório cancelado')
            break
        else:
            print('Opção inválida. Digite "y" para salvar o relatório ou "n" para cancelar o salvamento.')


def calcular_total_transacoes():
    """
    Calcula o valor total de transações da conta.
    Utilize essa mesma função para o caso `por categoria`
    """
    while True:
        #Escolha por soma total ou som por categoria
        print("1. Exibir soma total de transações")
        print("2. Exibir a soma total por categoria")
        print("-" * 10)
        print("0. Voltar ao menu inicial")

        opcao_soma = input('Escolha uma opção: ')

        # Cálculo da soma total de todas as categorias  
        if opcao_soma == '1': 
            total = sum(transacao['valor'] for transacao in bd)
            relatorio = (f"Total de transações total: R$ {total:.2f}")
            print(relatorio)

            # Salvando o relatório
            nome_relatorio = f'soma_total_todas_transacoes'
            salvar_relatorio(nome_relatorio, relatorio)
            digite_para_continuar()
            break

        # Cálculo da soma total por categoria
        elif opcao_soma == '2': 
            lista_categorias()

            categoria = input("Digite o número da categoria: ")
            escolhida = selecao_categoria(categoria)

            # condição quando numero_categoria digitado foi "0"
            if escolhida == 'retorno':
                digite_para_continuar()
                break

            if escolhida != None:
                total = sum(transacao['valor'] for transacao in bd if transacao['categoria'] == escolhida)
                relatorio = (f"Total das transações da categoria {escolhida}: R$ {total:.2f}")
                print(relatorio)

                # Salvando o relatório
                nome_relatorio = f'total_transacoes_categoria_{escolhida}'
                salvar_relatorio(nome_relatorio, relatorio)
                digite_para_continuar()
            else:
                digite_para_continuar()

        elif opcao_soma == '0':
            digite_para_continuar()
            break
        else:
            digite_para_continuar()
            continue
                    

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

        # String relatório
        relatorio = f'5 transações {m}:\n'
        for transacao in transacoes:
            relatorio += f"ID: {transacao['UUID']}, Valor: R$ {transacao['valor']:.2f}, Categoria: {transacao['categoria']}\n"
            print(transacao)
        
        nome_relatorio = f'5_transações_{m}'
        salvar_relatorio(nome_relatorio, relatorio)

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
        relatorio = f"Média das transações: R$ {media:.2f}"
        print(relatorio)
        nome_relatorio = 'media_transacoes'
        salvar_relatorio(nome_relatorio, relatorio)
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

    relatorio = (
        f'Transação: {transacao_solicitada[0]["UUID"]}\n'
        f'Valor: {transacao_solicitada[0]["valor"]}\n'
        f'Categoria: {transacao_solicitada[0]["categoria"]}\n'
    )
    print(relatorio)
    
    nome_relatorio = f'transacao_{transacao_solicitada[0]["UUID"]}'

    salvar_relatorio(nome_relatorio, relatorio)
    pass

def cadastrar_transacao():
    """
    Cadastra uma nova transação.
    \nObs:Para gerar um novo uuid, veja como é feito na função `criar_transacoes`.
    """    
    while True:
        print("Cadastro de Novas Transações")
        print("")

        # listar as categorias para cadastro
        lista_categorias()
        # seleção da categoria escolhida pelo usuário
        numero_categoria = input("Digite a número da categoria:")
        categoria = selecao_categoria(numero_categoria)

        # condição quando numero_categoria digitado foi "0"
        if categoria == 'retorno':
            break

        # Salvando a transação e o valor no banco de dados
        if categoria is not None:
            print('\nDigite "0" para retornar ao menu\n')
            print(f'Foi selecionada a categoria {categoria}')

            # Tratamento do valor a ser salvo
            valor_input = input("Digite o valor: R$")
            try:
                valor_transacao = float(valor_input)
            except ValueError:
                print('Valor inválido! Digite novamente.')
                digite_para_continuar()
                continue
            
            # opção de retornar ao menu anterior
            if valor_transacao == 0:
                digite_para_continuar()
                continue
            
            # quando um valor válido é digitado
            transacao = {
                "UUID": str(uuid.uuid4()),
                "valor": valor_transacao,
                "categoria": categoria
            }

            # Salvando a transação no banco de dados
            bd.append(transacao)

            salvar_json(bd, path2save="./data", filename='transactions.json')
            
            # Dados da transação realizada para contultas futuras
            print('\nDados da transação realizada: ')
            for chave, valor in transacao.items():
                print(f'{chave}: {valor}')
            break
        else:
            digite_para_continuar()  
            pass


def editar_transacao_por_ID():
    """
    Edita uma transação específica pelo seu UUID.
    """
    while True:
        #Pede ao usuário para inserir o id da transação e verifica se o usuário quer voltar para o menu iniciar
        id = input("Digite o ID da operação que deseja alterar ou 0 se quiser voltar ao menu: ")
        if id == "0" or id == "zero":
            print("Voltando para o menu inicial")
            break  
        #Verifica o id na base de dados  
        transacao_solicitada = list((transacao for transacao in bd if transacao['UUID'] == id))
        #Mostra para o usuário como está a versão atual da transação    
        relatorio = (
            f'Transação: {transacao_solicitada[0]["UUID"]}\n'
            f'Valor: {transacao_solicitada[0]["valor"]}\n'
            f'Categoria: {transacao_solicitada[0]["categoria"]}\n'
        )
        print(f"Este é a versão atual da transacao: \n{relatorio}")
        #Recebe os novos valores e categorias    
        novo_valor = float(input("Digite o novo valor da operação ou digite 0 para sair: "))
        if novo_valor < 0:
            raise ValueError("O número não pode ser negativo.")
        if novo_valor == 0 :
            print("Voltando para o menu inicial")
            break  
        lista_categorias()
        escolha_categoria = input("Digite a nova categoria: ")
        nova_categoria = selecao_categoria(escolha_categoria)
        #Atribui os novos valores        
        transacao_solicitada[0]["valor"] = novo_valor
            
        transacao_solicitada[0]["categoria"] = nova_categoria
        #Salva as alterações no arquivo transactions.json    
        with open('./data/transactions.json', 'w') as file:
                json.dump(bd, file, indent=4)
        #Mostra para o usuário a versão atualizada dos dados        
        relatorio2 = (
            f'Transação: {transacao_solicitada[0]["UUID"]}\n'
            f'Valor: {transacao_solicitada[0]["valor"]}\n'
            f'Categoria: {transacao_solicitada[0]["categoria"]}\n'
        )
        print(f"Este é a versão editada da transação:  \n{relatorio2}")
        break
    

def excluir_transacao():
    """
    Exclui uma transação específica pelo UUID.
    """
    # Recebe o ID que o usuário quer excluir ou retorna o mesmo para a tela inicial
    transacao_a_excluir = input("Digite o UUID da transação que deseja excluir ou digite 0 para voltar para o menu principal: ").strip()
    
    if transacao_a_excluir == "0":
        raise ValueError("Retornando para o Menu principal")
    # Exclui os dados do id e salva a alterações no arquivo transactions.json
    transacao_encontrada = False
    for transacao in bd:
        if transacao['UUID'] == transacao_a_excluir:
            bd.remove(transacao)
            transacao_encontrada = True
            with open('./data/transactions.json', 'w') as file:
                json.dump(bd, file, indent=4)
            break
    
    if transacao_encontrada:
        print(f"A transação com UUID {transacao_a_excluir} foi excluída com sucesso.")
    else:
        print("UUID não encontrado. Por favor, verifique e tente novamente.")


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
