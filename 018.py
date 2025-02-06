from math import radians, sin, cos, tan
ang = float(input('Qual o ângulo? '))
rad = radians(ang)
print(f'Seu seno é {sin(rad):.2f}.')
print(f'Seu cosseno é {cos(rad):.2f}.')
print(f'Sua tangente é {tan(rad):.2f}.')