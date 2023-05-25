lista_altura = []
lista_tempo = []

y2 = 0
z = 0

for x in range(len(lista_y)):

    if tempo[x] > 5:
        z += 0.000000222

    elif tempo[x] > 1:
        y2 += 0.0000108
        z += 0.0001372
    
    else:
    
        y2 = 0.0000212
        z += 0.000122

    if tempo[x] > 5:
        z += 0.00000022
    
    y3 = float(lista_y[x])
    y_final = y2 + y3
    
    lista_altura.append(y_final)
    lista_tempo.append(float(tempo[x] - z) + 1.334)

# Abrir o arquivo para escrita
with open('dados.txt', 'w') as arquivo:
    # Escrever os dados no arquivo, convertendo notação científica para decimal se necessário
    for i in range(len(lista_altura)):
        altura_cientifica = "{:.3e}".format(lista_altura[i])
        if 'e-01' in altura_cientifica or 'e+00' in altura_cientifica:
            altura_decimal = "{:.3f}".format(float(altura_cientifica))
        else:
            altura_decimal = altura_cientifica
        
        tempo_cientifico = "{:.3e}".format(lista_tempo[i])
        if 'e-01' in tempo_cientifico or 'e+00' in tempo_cientifico:
            tempo_decimal = "{:.3f}".format(float(tempo_cientifico))
        else:
            tempo_decimal = tempo_cientifico
        
        arquivo.write(f"{altura_decimal},{tempo_decimal}\n")