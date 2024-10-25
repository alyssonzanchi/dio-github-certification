# Desafio 4: Verificando Números Pares e Ímpares 🧮

# Recebendo um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

# Exibindo o resultado
print("O número", numero, "é", resultado)
