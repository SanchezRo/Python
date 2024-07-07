print("-=-=-=-=-=-=-=-=-=-=-")
print("ANALISADOR DE TRIANGULO")
print("-=-=-=-=-=-=-=-=-=-=-")

r1 = float(input("Qual o valor do Primeiro Segmento: "))
r2 = float(input("Qual o valor do Segundo Segmento: "))
r3 = float(input("Qual o valor do Terceiro Segmento: "))

print("-=-=-=-=-=-=-=-=-=-=-")
if r1 < r2+r3 and r2 < r3+r1 and r3 < r1+r2:
    print('Estes Segmentos PODEM FORMAR um Triangulo')
else: print('Estes Segmentos NÃO PODEM FORMAR um Triangulo')
