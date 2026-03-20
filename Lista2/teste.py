tabela = []
#qtd = int(input("Quantos produtos você quer cadastrar? "))

for i in range(2): #qtd
    print(f"\nCadastro do produto {i+1}")

    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    total = quantidade * preco

    linha = {
        "id": i + 1,
        "produto": produto,
        "quantidade": quantidade,
        "preco": preco,
        "total": total
    }
    tabela.append(linha)

print("\n" + "-" * 60)
print(f"{'ID':<5}{'PRODUTO':<20}{'QTD':<10}{'PREÇO':<10}{'TOTAL':<10}")
print("-" * 60)
for item in tabela:
    print(f"{item['id']:<5}{item['produto']:<20}{item['quantidade']:<10}{item['preco']:<10.2f}{item['total']:<10.2f}")
print("-" * 60)