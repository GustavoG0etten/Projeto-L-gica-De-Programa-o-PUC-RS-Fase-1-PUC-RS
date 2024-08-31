"""
Este código será comentado a todo momento para que seja o mais claro possível 
Agradeço o tempo que tiraram para corrigir o meu código :) """

# Parte 1: Validação dos dados que irão entrar no código

# Lista que irá armazenar todas as temperaturas 
temps = []

# Loop para receber as temperaturas 
for mes in range(1, 13): 

    while True:
        
        temperatura = float(input(f"Digite a temperatura máxima do mês {mes}: "))

        # Verificando se a temperatura é valida 
        if temperatura >= -60 and temperatura <= 50:
            
            temps.append(temperatura)

            break
        else:
            print("A temperatura é invalida, insira uma medida entre -60 a 50 Graus Celsius")

# Parte 2: Calculos requisitados no enunciado 

# Colocando os meses por extenso 
meses_escritos = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# Temperatura média máxima anual
media_maxima = sum(temps) / 12
print(f"\nTemperatura média máxima anual: {media_maxima: .2f}°C")

# Meses que tivera temperatura acima dos 33°C 
meses_escaldantes = 0
for temperatura in temps:
    if temperatura > 33:
        meses_escaldantes += 1

print(f"Quantidade de meses escaldantes (temperatura acima de 33°C): {meses_escaldantes}")

# Mes com a maior temperatura 
mes_mais_quente = max(temps)
mes_mais_quente_nome = temps.index(mes_mais_quente)
print(f"O mes mais escaldante foi {meses_escritos[mes_mais_quente_nome]} com {mes_mais_quente}°C")

# Mes com a menor temperatura
mes_menos_quente = min(temps)
mes_menos_quente_nome = temps.index(mes_menos_quente)
print(f"O mes mais frio foi {meses_escritos[mes_menos_quente_nome]} com {mes_menos_quente}°C")

