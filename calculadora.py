def somar(a, b):
    """Esta função soma dois números. Corrigido para lidar com inteiros."""
    return a + b

def subtrair(a, b):
    """Esta função subtrai dois números."""
    return a - b

if __name__ == "__main__":
    print("Calculadora Simples")
    resultado_soma = somar(5, 3)
    print(f"Resultado da soma: {resultado_soma}")

    resultado_subtracao = subtrair(10, 4)
    print(f"Resultado da subtração: {resultado_subtracao}")