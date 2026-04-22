bebidas = []

for i in range(5):
    bebida = input(f"Digite uma bebida favorita: ")
    bebidas.append(bebida)

bebidas.sort()

print(f"\nBebidas escolhidas: ")
for bebida in bebidas:
    print(bebida.center(20, "-"))


def dobro(n):
    return n * 2

if __name__ == "__main__":
    numero = int(input("Digite um número para calcular o dobro:"))
    resultado = dobro(numero)