# Calculadora dos dados de consumo de um automóvel
import PySimpleGUI as sg

sg.change_look_and_feel('LightBrown9')
#Layout
layout = [
    [sg.Text("Insira a potência do seu automóvel"), sg.Input(size=(20,1), key='Potencia')],
    [sg.Text("Insira a velocidade média no percurso"), sg.Input(size=(20,1), key='Velocidade')],
    [sg.Text("Insira a quantidade de pessoas dentro do veículo"), sg.Input(size=(20,1), key='Pessoas')],
    [sg.Text("Insira a quantidade em litros de combustível"), sg.Input(size=(20,1), key='litros')],
    [sg.Text("Ar Condicionado Ligado?"), sg.Checkbox('Sim', key='Ar_Ligado'), sg.Checkbox('Não', key='Ar_Desligado')],
    [sg.Text("O veículo foi operado na estrada ou na cidade? "), sg.Checkbox("Estrada", key='estrada'), sg.Checkbox('Cidade', key= 'cidade')],
    [sg.Text("Insira o tipo do combustível"), sg.Checkbox("Diesel", key='Diesel'), sg.Checkbox("Etanol", key='Etanol'), sg.Checkbox("Gasolina", key='Gasolina')],
    [sg.Button('Obter a Média')],
]

#janela
janela = sg.Window("Calculadora automobilística", layout)
    
#Extrair dados da tela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event == "Obter a Média":
        #Variáveis para o cálculo
        ar_ligado = 0.90
        pessoas = 0.96
        ar_on = values['Ar_Ligado']
        ar_off = values['Ar_Desligado']
        potencia_do_carro = values['Potencia']
        pessoas_veiculo = int(values['Pessoas'])
        litros_combustivel = float(values['litros']) #Consumo do Carro
        Velocidade_Media = float(values['Velocidade'])
        tipo_combustivel = values['Diesel']
        outro_combustivel = values['Etanol']
        maisum_combustivel = values['Gasolina']
        operado_estrada = values['estrada']
        operado_cidade = values['cidade']
        #Definir Autonomia():
        if (Velocidade_Media == True) or (Velocidade_Media <= 100):
            autonomia = 10
        elif (Velocidade_Media == True) or (Velocidade_Media <= 110):
            autonomia = 9
        elif (Velocidade_Media == True) or (Velocidade_Media <= 120):
            autonomia = 8
        elif (Velocidade_Media == True) or (Velocidade_Media >= 121):
            autonomia = 6
        # Obter a Média():
        if (tipo_combustivel == True) and (operado_estrada == True) and (pessoas_veiculo <= 5) and (ar_on == True) and (ar_off == False):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', ((litros_combustivel*autonomia)*ar_ligado)*pessoas)
        elif (tipo_combustivel == True) and (operado_estrada == True) and (pessoas_veiculo <= 5) and (ar_on == False) and (ar_off == True):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', (litros_combustivel*autonomia)*pessoas)
        elif (tipo_combustivel == True) and (operado_cidade == True) and (pessoas_veiculo <= 5) and (ar_on == True) and (ar_off == False):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', ((litros_combustivel*6.7)*ar_ligado)*pessoas)
        elif (tipo_combustivel == True) and (operado_cidade == True) and (pessoas_veiculo <= 5) and (ar_on == False) and (ar_off == True):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', (litros_combustivel*6.7)*pessoas)
        elif (outro_combustivel == True) and (operado_estrada == True) and (pessoas_veiculo <= 5) and (ar_on == True) and (ar_off == False):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', ((litros_combustivel*autonomia)*0.90)*pessoas)
        elif (outro_combustivel == True) and (operado_estrada == True) and (pessoas_veiculo <= 5) and (ar_on == False) and (ar_off == True):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', (litros_combustivel*autonomia)*pessoas)
        elif (outro_combustivel == True) and (operado_cidade == True) and (pessoas_veiculo <= 5) and (ar_on == True) and (ar_off == False):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', ((litros_combustivel*6)*0.90)*pessoas)
        elif (outro_combustivel == True) and (operado_cidade == True) and (pessoas_veiculo <= 5) and (ar_on == False) and (ar_off == True):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', (litros_combustivel*6)*pessoas)
        elif (maisum_combustivel == True) and (operado_estrada == True) and (pessoas_veiculo <= 5) and (ar_on == True) and (ar_off == False):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', ((litros_combustivel*autonomia)*0.90)*pessoas)
        elif (maisum_combustivel == True) and (operado_estrada == True) and (pessoas_veiculo <= 5) and (ar_on == False) and (ar_off == True):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', (litros_combustivel*autonomia)*pessoas)
        elif (maisum_combustivel == True) and (operado_cidade == True) and (pessoas_veiculo <= 5) and (ar_on == True) and (ar_off == False):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', ((litros_combustivel*9)*0.90)*pessoas)
        elif (maisum_combustivel == True) and (operado_cidade == True) and (pessoas_veiculo <= 5) and (ar_on == False) and (ar_off == True):
            sg.popup('Conforme os dados inseridos, a sua média de consumo é de: ', (litros_combustivel*9)*pessoas)
                
            
            
            
            

        
    