estoque_alimentos = 50
estoque_bebidas = 75
estoque_mat_limpeza = 30
produto = ''
categoria = ''

print("********************************************************************************************************")
print("*                               Sistema de contagem de produtos                                        *")
print("********************************************************************************************************")
print("--------------------------------------------------------------------------------------------------------")
print(" Selecione a categoria dos produtos:\n1 => Alimentos\n2 => Bebidas\n3 => Materiais de Limpeza ")

try:
    categoria = int(input())
except ValueError:
    print("Por favor, insira um número inteiro válido.")

print("--------------------------------------------------------------------------------------------------------")

if categoria == 1:
    produto = input("Digite o tipo do alimento...ex: Arroz Camil 5kg:")
    try:
        qtd_alimento = int(input(f"Digite a quantidade do produto {produto}, em estoque\n"))
        if qtd_alimento < estoque_alimentos:
            print(f"Solicitar {produto} ao setor de compras. Temos apenas {qtd_alimento} em estoque!")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

elif categoria == 2:
    produto = input("Digite o tipo da bebida...ex: Coca Cola 2L:")
    try:
        qtd_bebida = int(input(f"Digite a quantidade do produto {produto}, em estoque\n"))
        if qtd_bebida < estoque_bebidas:
            print(f"Solicitar {produto} ao setor de compras. Temos apenas {qtd_bebida} em estoque!")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

elif categoria == 3:
    produto = input("Digite o tipo do material de limpeza...ex: Desinfetante 1L:")
    try:
        qtd_mat_limpeza = int(input(f"Digite a quantidade do produto {produto}, em estoque\n"))
        if qtd_mat_limpeza < estoque_mat_limpeza:
            print(f"Solicitar {produto} ao setor de compras. Temos apenas {qtd_mat_limpeza} em estoque!")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

print("\nFim do programa!")
input("Pressione qualquer tecla para finalizar...")
print("--------------------------------------------------------------------------------------------------------")