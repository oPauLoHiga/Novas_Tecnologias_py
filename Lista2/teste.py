# Gerador de Fatura Personalizada
from datetime import datetime

cliente = input("Digite o nome completo do cliente: ")
pedido = input("Digite o número do pedido: ")
data_texto = input("Digite a data de emissão: ")

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