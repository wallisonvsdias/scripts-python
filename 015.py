aluguel = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preco = 60 * aluguel + 0.15 * km
print(f'O total a pagar é de R${preco}')