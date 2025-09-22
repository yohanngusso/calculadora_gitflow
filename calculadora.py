def somar(a, b):
    """Esta função soma dois números. Corrigido para lidar com inteiros."""
    return a + b

def subtrair(a, b):
    """Esta função subtrai dois números."""
    return a - b

def multiplicar(a, b):
    """Esta função multiplica dois números."""
    return a * b

def dividir(a, b):
    """Esta função divide dois números. Retorna um erro se o divisor for zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Calculadora Interativa ---")
    print("Escolha a operação:")
    print("1: Somar")
    print("2: Subtrair")
    print("3: Multiplicar")
    print("4: Dividir")
    print("0: Sair")

# A partir daqui é o nosso novo loop principal
if __name__ == "__main__":
    while True:
        exibir_menu()
        escolha = input("Digite o número da sua opção: ")

        if escolha == '0':
            print("Encerrando a calculadora. Até mais!")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")