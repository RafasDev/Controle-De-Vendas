codigo_produto1, unidade_produto1, preço_produto1 = input().split()
codigo_produto1 = int(codigo_produto1)
unidade_produto1 = int(unidade_produto1)
preço_produto1 = float(preço_produto1)

codigo_produto2, unidade_produto2, preço_produto2 = input().split()
codigo_produto2 = int(codigo_produto2)
unidade_produto2 = int(unidade_produto2)
preço_produto2 = float(preço_produto2)

pagar = (unidade_produto1 * preço_produto1) + (unidade_produto2 * preço_produto2)

print(f"VALOR A PAGAR: R$ {pagar:.2f}")