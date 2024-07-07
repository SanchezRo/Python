n = int(input('Digite um numero de 1 a 9999: '))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print(n)
print('unidade', u)
print('dezena', d)
print('centena', c)
print('milhar', m)