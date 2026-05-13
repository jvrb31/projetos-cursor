def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obeso"


def ler_float_positivo(prompt: str) -> float:
    texto = input(prompt).strip().replace(",", ".")
    valor = float(texto)
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    return valor


def main():
    print("Calculadora de IMC")
    print("(peso em kg, altura em metros)\n")

    try:
        peso = ler_float_positivo("Qual é o seu peso (kg)? ")
        altura = ler_float_positivo("Qual é a sua altura (m)? ")
    except ValueError as e:
        print(f"\nEntrada inválida: {e}")
        return

    imc = peso / (altura * altura)
    classificacao = classificar_imc(imc)

    print()
    print(f"IMC: {imc:.1f}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    main()
