# 1. Geração de Relatório Dinâmico
# Crie um programa que solicita ao usuário o nome de 2 produtos,
# suas quantidades em estoque e seus preços unitários.
# Depois, exiba uma tabela formatada com alinhamento justificado,
# casas decimais nos preços e total de cada produto.
# Use f-strings e. format() para praticar os dois métodos.
import os

# Produto	    | Quantidade	| Preço Unitário    | Total
# Caderno	    |       10	    |  12.50            | 125.00
# Caneta Azul	|       50	    |  2.75	            | 137.50

# tabelas = []
# for i in range (2):
#     produt = input("Insira o produto: ")
#     quant = int(input("Insira a quantidade: "))
#     preco = float(input("Insira o valor"))
#     total = preco * quant
#     linha = {
#         "produto": produt,
#         "quantidade": quant,
#         "preco": preco,
#         "total": total
#     }
#     tabelas.append(linha)
# print("\n"+"-" * 70)
# print("{:<20}{:<20}{:<15}{:<20}".format("PRODUTO", "QUANTIDADE", "PRECO", "TOTAL"))
# print("\n"+"-" * 70)
# for i in tabelas:
#     print("{:<20}{:<20}{:<15.2f}{:<20.2f}".format(
#         i['produto'],
#         i['quantidade'],
#         i['preco'],
#         i['total']
#     ))
# print("-" * 70)

# 2. Gerador de Fatura Personalizada
# Solicite o nome completo de um cliente, o número do pedido e a data de emissão.
# Formate uma fatura em formato fixo como se fosse enviada por e-mail.
# O layout deve conter espaços definidos, alinhamento central e colunas formatadas.
# Use .format() com placeholders posicionais e nomeados.

from datetime import datetime

cliente = input("Digite o nome completo do cliente: ")
pedido = input("Digite o número do pedido: ")
data_texto = input("Digite a data de emissão EX: 00/00/0000 ")

data = datetime.strptime(data_texto, "%d/%m/%Y")

# Exibição da fatura
print("\n" + "=" * 60)
print("{:^60}".format("FATURA DE PEDIDO"))
print("=" * 60)

print("Cliente.........: {}".format(cliente))
print("Pedido..........: {}".format(pedido))
print("Data de Emissão.: {}".format(data))

print("-" * 60)
print("{:^60}".format("RESUMO DO PEDIDO"))
print("-" * 60)

# Cabeçalho com placeholders posicionais
print("{:<20} {:^15} {:>20}".format("Descrição", "Pedido", "Data"))
print("{:<20} {:^15} {:>20}".format("-" * 10, "-" * 6, "-" * 10))

# Linha com placeholders nomeados
print("{desc:<20} {num:^15} {dt:>20}".format(
    desc="Fatura emitida",
    num=pedido,
    dt = data.strftime("%d/%m/%Y")
))

print("-" * 60)

# Rodapé estilo e-mail
mensagem = """
Prezado(a) {cliente},

Sua fatura referente ao pedido número {pedido} foi emitida com sucesso
na data de {data}.

Agradecemos pela preferência!

Atenciosamente,
Equipe Financeira
""".format(cliente=cliente, pedido=pedido, data=data)

print(mensagem)
print("=" * 60)


# 3. Validador e Formatador de CPF Peça ao usuário que digite um
# CPF apenas com números (11 dígitos) e exiba o
# CPF formatado corretamente no padrão ###.###.###-## utilizando f-strings.

# cpf = input('Digite seu cpf: ')
# if len(cpf) == 11 :
#      if cpf.isnumeric():
#          os.system('cls')
#          print(f"seu CPF formatado é: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2::]}")
# else:
#     os.system('cls')
#     print("Erro!! Tente novamente\nDigite apenas os numeros do CPF")

# 4. Simulador de Cupom Fiscal
# Implemente uma função que recebe uma lista de produtos (nome, quantidade, preço unitário)
# e retorna uma string formatada em estilo de cupom fiscal de supermercado.
# Inclua nome da loja, data, e o valor total no final,
# com todos os valores alinhados e com R$ corretamente formatado.
# Supermercado Malvader
# Data:        05/03/2025 16:24
# ------------------------------
# Item             Qtd     Preço
# Caderno            2     12.50
# Caneta            10      2.75
# ------------------------------
# Total                    52.50
#
#
# 5. Formatação Condicional de Resultados Acadêmicos
# Dado um dicionário com nomes de alunos e suas notas, gere um boletim formatado onde:
# - Notas acima de 7 aparecem em verde (use ANSI escape codes).
# - Notas entre 5 e 7 aparecem em amarelo.
# - Notas abaixo de 5 aparecem em vermelho.
# Exemplo:
# Ana       :  9.5 (Aprovado) - VERDE
# João      :  4.0 (Reprovado) - VERMELHO
# Maria     :  6.5 (Recuperação) MARROM
#

# 6. Registro de Logs com Nível de Criticidade
# Crie uma função de log que receba uma mensagem, o nível de criticidade
# (INFO, WARNING, ERROR) e a hora atual.
# A função deve gerar uma string formatada com cor e estilo de acordo com o nível
# (INFO = azul, WARNING = amarelo, ERROR = vermelho).
# Use f-strings e datetime e # Cores ANSI para o terminal.
# [2025-03-05 16:33:29] [INFO] Sistema iniciado
# [2025-03-05 16:33:29] [WARNING] Atenção: baixo estoque
# [2025-03-05 16:33:29] [ERROR] Falha na conexão


# 7. Formatação de Código SQL Dinâmico
# Peça ao usuário o nome de uma tabela, uma lista de colunas e seus tipos de dados,
# e gere dinamicamente uma string de comando SQL de criação da tabela (CREATE TABLE),
# formatada com identação correta e alinhamento dos tipos de dados.
#
# CREATE TABLE clientes (
#     id INT PRIMARY KEY,
#     nome VARCHAR(100),
#     nascimento DATE,
#     saldo DECIMAL(10,2)
# );

