largura = float(input("Largura da Parede: "))
altura = float(input("Altura da Parede: "))
area= largura * altura
print('Sua Parede possui {}m de Largura e {}m de Altura.'.format(largura, altura))
print('A Área é de: {}m2'.format(area))
tinta = area / 2
print("Para Pintar sua Parede você irá precisar de: {:.2f} Litros de Tinta".format(tinta))