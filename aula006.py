n = input('Digite algo:') # Por padrão, o tipo é string

# Métodos de teste
print(n.isnumeric()) # Aceita apenas números
print(n.isalpha()) # Aceita apenas letras
print(n.isalnum()) # Aceita letras e/ou números, mas não aceita espaços, por exemplo
print(n.isupper()) # Aceita apenas se todos os caracteres estiverem em maiúsculo
