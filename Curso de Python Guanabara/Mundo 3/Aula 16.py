lanche = ('hamburger', 'suco', 'fritas', 'pudim', 'suco')
print(lanche)
print(lanche[2])
print(lanche[1:3])
for c in range(0, len(lanche)):
    print(lanche[c])
for c in lanche:
    print(f'Eu vou comer {c}')
print('comi pakas')

nums = (1, 2, 3, 4, 5)
numsfoodtruck = lanche + nums
print(numsfoodtruck)
print(len(numsfoodtruck))
print(numsfoodtruck.count('suco'))
print(numsfoodtruck.index('suco'))