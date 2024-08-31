"""
Este código será comentado a todo momento para que seja o mais claro possível 
Agradeço o tempo que tiraram para corrigir o meu código :) """

# Parte 1: Validação dos dados que irão entrar no código

# Lista que irá armazenar todas as temperaturas 
TemperaturaDeCadaMes = []

# Laço para receber todas as temperaturas 
for mes in range(1, 13): 
    # O loop abaixa irá receber e validar os dados de entrada
    while True:
        # Requisitando ao usuario as temperaturas 
        temperatura = float(input(f"Digite a temperatura máxima do mês {mes}: "))

        # Verificando se a temperatura é valida 
        if temperatura >= -60 and temperatura <= 50:
            # Se a temperatura estiver correta, usamos o códico abaixo para adicionar a lista de temperaturas de cada mes 
            TemperaturaDeCadaMes.append(temperatura)

            break
        else:
            # Se a temperatura estiver fora dos padrões colocamos a seguinte mensagem 
            print("A temperatura é invalida, insira uma medida entre -60 a 50 Graus Celsius")

