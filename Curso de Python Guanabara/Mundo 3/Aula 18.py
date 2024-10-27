'listas'

pessoas = list
pessoas = [['pedro', 25],['Maria', 19],['João', 33]]
print(pessoas[0][0]) #pedro
print(pessoas[1][0]) #Maria
print(pessoas[1][1]) #19


'''-------------------------------------------'''
'''teste = list()
teste.append(58)
teste.append('Ruberval')
teste.append(61)
teste.append('Josefina')
galera3aIDADE = list()
galera3aIDADE.append(teste)
print(galera3aIDADE)'''

galera3aIDADE = [['Ruberval', 58],['Joseffina', 61],['Cleide', 57],['Deodoro', 62],['Helivani', 60]]
for p in galera3aIDADE:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galerinha = list()
dado = list()
n = int(input('Quantas pessoas compõem o grupo? '))
for c in range(0,(n)):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galerinha.append(dado[:])
    dado.clear()
print(galerinha)
