from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'Logo, o comprimento da hipotenusa é {hypot(co, ca):.2f}')
# hipotenusa = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))