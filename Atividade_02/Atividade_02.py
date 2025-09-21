# Atividade Prática 02

# 1 - Conversor de Moeda
print("=== Conversor de Moeda ===")
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

print(f"Valor em Reais: R$ {valor_reais}")
print(f"Valor em Dólares: US$ {valor_dolar}")
print(f"Valor em Euros: € {valor_euro}")
print("\n")

# 2 - Calculadora de Desconto
print("=== Calculadora de Desconto ===")
produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = round(preco_original * desconto_percentual / 100, 2)
preco_final = round(preco_original - valor_desconto, 2)

print(f"Produto: {produto}")
print(f"Preço Original: R$ {preco_original}")
print(f"Desconto: {desconto_percentual}% -> R$ {valor_desconto}")
print(f"Preço Final: R$ {preco_final}")
print("\n")

# 3 - Calculadora de Média Escolar
print("=== Calculadora de Média Escolar ===")
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = round((nota1 + nota2 + nota3) / 3, 2)

print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média Final: {media}")
print("\n")

# 4 - Calculadora de Consumo de Combustível
print("=== Calculadora de Consumo de Combustível ===")
distancia_km = 300
combustivel_litros = 25

consumo_medio = round(distancia_km / combustivel_litros, 2)

print(f"Distância Percorrida: {distancia_km} km")
print(f"Combustível Gasto: {combustivel_litros} litros")
print(f"Consumo Médio: {consumo_medio} km/l")
