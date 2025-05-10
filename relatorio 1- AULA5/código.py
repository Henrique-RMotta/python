import random

def informacoes():
    print("Seja Bem-vindo ao simulador de consumo de energia elétrica!")
    nome = input("Qual aparelho você deseja fazer o cálculo de consumo de energia: ")  # Nome do aparelho
    potencia = float(input(f"Qual é o consumo em Watts de potência elétrica do seu(a) {nome}: "))  # Potência do aparelho
    tensao = int(input(f"Qual a tensão que seu(a) {nome} está trabalhando (em Volts): "))  # Tensão de trabalho
    corrente = potencia / tensao  # Corrente consumida pelo aparelho
    tempo = float(input(f"Cerca de quantas horas por dia o(a) {nome} realiza trabalho: "))  # Tempo de uso diário
    dias = int(input(f"Quantos dias por mês o(a) {nome} fica ligado: "))  # Dias de uso no mês


    # Chama a função de cálculo
    conta, consumomedio, consumo, tarifas = calculo(potencia, tempo, dias)
    

    # Exibe os resultados
    print(f"\nResultados para o aparelho {nome}:")
    print(f"Corrente consumida: {corrente:.2f} A")
    print(f"Consumo total no período: {consumo:.2f} kWh")
    print(f"Consumo médio diário: {consumomedio:.2f} kWh")
    print(f"Tarifa atual: {tarifas:.2f} por kWh")
    print(f"Custo estimado na conta de energia: R$ {conta:.2f}")

    # Pergunta se o usuário deseja adicionar outro aparelho
    msg = input("Quer adicionar outro aparelho? (s/n): ")
    if msg == 's':
        informacoes()  # Chama a função novamente para outro aparelho
    else:
        print("volte sempre !")


def calculo(potencia, tempo, dias):
    """
    Calcula o consumo de energia elétrica e o custo estimado.
    """
    consumomedio = (potencia * tempo) / 1000 #consumo em kwH por dia 
    consumo = (potencia * tempo * dias) / 1000  # Consumo em total kWh
    tarifas = random.uniform(0.41, 1.47)  # Tarifa aleatória entre 0.41 e 1.47
    conta = consumo * tarifas# Cálculo do custo total
    return conta, consumomedio, consumo, tarifas


# Inicia o programa
informacoes()