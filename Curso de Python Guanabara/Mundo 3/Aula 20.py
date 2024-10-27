'''a = 4
b = 5
s = a+b
print(s)

a = 8
b = 9
s = a+b
print(s)

a = 2
b = 1
s = a+b
print(s)'''

#funções
def line():
    print('-='*30)


def soma(a, b):
    line()
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A Soma A + B = {s}')


#Programa Principal
soma(b=5, a=5)
soma(a=7, b=2)
soma(4, 5)
soma(8, 9)
soma(2, 1)

print()
line()

def contador(*num):
    tam = len(num)
    line()
    print(f'Recebi os valores {num} e são ao todo {tam} números!')


nums = list()
def valores():
    nums.clear()
    while len(nums) < 5:
        nums.append(int(input('Digite um valor: ')))


valores()
print(nums)
contador(nums[0], nums[1], nums[2], nums[3], nums[4])

print()

def dobraValList(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    line()


valores()
dobraValList(nums)
print(nums)