# 1. Geração de Relatório Dinâmico
# Crie um programa que solicita ao usuário o nome de 2 produtos,
# suas quantidades em estoque e seus preços unitários.
# Depois, exiba uma tabela formatada com alinhamento justificado,
# casas decimais nos preços e total de cada produto.
# Use f-strings e. format() para praticar os dois métodos.

# Produto	    | Quantidade	| Preço Unitário    | Total
# Caderno	    |       10	    |  12.50            | 125.00
# Caneta Azul	|       50	    |  2.75	            | 137.50

# 2. Gerador de Fatura Personalizada
# Solicite o nome completo de um cliente, o número do pedido e a data de emissão.
# Formate uma fatura em formato fixo como se fosse enviada por e-mail.
# O layout deve conter espaços definidos, alinhamento central e colunas formatadas.
# Use .format() com placeholders posicionais e nomeados.


# 3. Validador e Formatador de CPF
# Peça ao usuário que digite um CPF apenas com números (11 dígitos) e exiba o
# CPF formatado corretamente no padrão ###.###.###-## utilizando f-strings.


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

