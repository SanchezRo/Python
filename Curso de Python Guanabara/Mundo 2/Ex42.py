print("-=-=-=-=-=-=-=-=-=-=-")
print("ANALISADOR DE TRIANGULO")
print("-=-=-=-=-=-=-=-=-=-=-")

r1 = float(input("Qual o valor do Primeiro Segmento: "))
r2 = float(input("Qual o valor do Segundo Segmento: "))
r3 = float(input("Qual o valor do Terceiro Segmento: "))

print("-=-=-=-=-=-=-=-=-=-=-")
if r1 < r2+r3 and r2 < r3+r1 and r3 < r1+r2:
    if r1 == r2 and r2 == r3:
        print('Estes Segmentos PODEM FORMAR um Triangulo Equilatero')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Estes Segmentos PODEM FORMAR um Triangulo Retangulo')
    else:
        print('Estes Segmentos PODEM FORMAR um Triangulo Isóceles')
else: print('Estes Segmentos NÃO PODEM FORMAR um Triangulo')
