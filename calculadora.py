# calculadora.py

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

if __name__ == "__main__":
    print("Calculadora Simples")
    # Testando as funções existentes
    print(f"Soma: 5 + 3 = {somar(5, 3)}")
    print(f"Subtração: 10 - 4 = {subtrair(10, 4)}")

    # Testando as novas funções
    print(f"Multiplicação: 6 * 7 = {multiplicar(6, 7)}")
    print(f"Divisão: 20 / 5 = {dividir(20, 5)}")