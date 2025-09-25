"""
Atividade Prática 03 - Exercícios Python
Descrição: Este programa contém quatro exercícios:
1. Classificador de Idade
2. Calculadora de IMC
3. Conversor de Temperatura
4. Verificador de Ano Bissexto
"""

def classificador_idade():
    """Classifica a idade em Criança, Adolescente, Adulto ou Idoso."""
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <= 12:
        categoria = "Criança"
    elif 13 <= idade <= 17:
        categoria = "Adolescente"
    elif 18 <= idade <= 59:
        categoria = "Adulto"
    elif idade >= 60:
        categoria = "Idoso"
    else:
        categoria = "Idade inválida"
    print(f"Você se encaixa na categoria: {categoria}\n")


def calculadora_imc():
    """Calcula o Índice de Massa Corporal e classifica a pessoa."""
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}\n")


def conversor_temperatura():
    """Converte temperaturas entre Celsius, Fahrenheit e Kelvin."""
    temperatura = float(input("Digite a temperatura: "))
    unidade_origem = input("Unidade de origem (C, F, K): ").upper()
    unidade_destino = input("Unidade de destino (C, F, K): ").upper()

    # Converter para Celsius
    if unidade_origem == "C":
        temp_c = temperatura
    elif unidade_origem == "F":
        temp_c = (temperatura - 32) * 5/9
    elif unidade_origem == "K":
        temp_c = temperatura - 273.15
    else:
        print("Unidade de origem inválida.\n")
        return

    # Converter de Celsius para destino
    if unidade_destino == "C":
        resultado = temp_c
    elif unidade_destino == "F":
        resultado = temp_c * 9/5 + 32
    elif unidade_destino == "K":
        resultado = temp_c + 273.15
    else:
        print("Unidade de destino inválida.\n")
        return

    print(f"{temperatura}{unidade_origem} é igual a {resultado:.2f}{unidade_destino}\n")


def verificador_ano_bissexto():
    """Verifica se o ano é bissexto."""
    ano = int(input("Digite o ano: "))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.\n")
    else:
        print(f"O ano {ano} não é bissexto.\n")


def menu():
    """Menu principal para escolher o exercício."""
    while True:
        print("Escolha uma opção:")
        print("1 - Classificador de Idade")
        print("2 - Calculadora de IMC")
        print("3 - Conversor de Temperatura")
        print("4 - Verificador de Ano Bissexto")
        print("0 - Sair")
        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            classificador_idade()
        elif opcao == "2":
            calculadora_imc()
        elif opcao == "3":
            conversor_temperatura()
        elif opcao == "4":
            verificador_ano_bissexto()
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()
