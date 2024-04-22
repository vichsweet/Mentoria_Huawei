import math


cobertura_por_litro = 3

volume_lata = 18

preco_lata = 80.00

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area / cobertura_por_litro

latas_necessarias = math.ceil(litros_necessarios / volume_lata)

custo_total = latas_necessarias * preco_lata

print(f"Você precisará de {latas_necessarias} lata(s) de tinta.")
print(f"O custo total será de R$ {custo_total:.2f}.")
