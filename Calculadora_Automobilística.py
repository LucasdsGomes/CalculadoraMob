# Calculadora dos dados de consumo de um automóvel
import PySimpleGUI as sg

sg.change_look_and_feel('LightBrown9')
#Layout
layout = [
    [sg.Text("Insira a média de consumo do seu automóvel"), sg.Input(size=(20,1), key='consumo')],
    [sg.Text("Insira a potência do seu automóvel"), sg.Input(size=(20,1), key='Potencia')],
    [sg.Text("Insira a velocidade média no percurso"), sg.Input(size=(20,1), key='Velocidade')],
    [sg.Text("Insira a quantidade de pessoas dentro do veículo"), sg.Input(size=(20,1), key='Pessoas')],
    [sg.Text("Insira a quantidade em litros de combustível"), sg.Input(size=(20,1), key='litros')],
    [sg.Text("Ar Condicionado Ligado?"), sg.Checkbox('Sim', key='Ar_Ligado'), sg.Checkbox('Não', key='Ar_Desligado')],
    [sg.Text("O veículo possui algum tipo de carga/malas?"), sg.Checkbox('Sim', key='Possui_Carga'), sg.Checkbox('Não', key='Sem_carga')],
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
        litros_combustivel = float(values['litros']) 
        Velocidade_Media = float(values['Velocidade'])
        tipo_combustivel = values['Diesel']
        outro_combustivel = values['Etanol']
        maisum_combustivel = values['Gasolina']
        operado_estrada = values['estrada']
        operado_cidade = values['cidade']
        #def DefinirAutonomia():
        if (Velocidade_Media == True) or (Velocidade_Media <= 100):
            autonomia = 10
        elif (Velocidade_Media == True) or (Velocidade_Media <= 110):
            autonomia = 9
        elif (Velocidade_Media == True) or (Velocidade_Media <= 120):
            autonomia = 8
        elif (Velocidade_Media == True) or (Velocidade_Media >= 121):
            autonomia = 6
        #def ObterMedia():
        if (tipo_combustivel == True) and (operado_estrada == True):
            sg.popup('Você obtêm uma média de: ', litros_combustivel*autonomia)
        if (tipo_combustivel == True) and (operado_cidade == True):
            sg.popup('Você obtêm uma média de: ', litros_combustivel*6.7)
        if (outro_combustivel == True) and (operado_estrada == True):
            sg.popup('Você obtêm uma média de: ', litros_combustivel*autonomia)
        if (outro_combustivel == True) and (operado_cidade == True):
            sg.popup('Você obtêm uma média de: ', litros_combustivel*6)
        if (maisum_combustivel == True) and (operado_estrada == True):
            sg.popup('Você obtêm uma média de: ', litros_combustivel*autonomia)
        if (maisum_combustivel == True) and (operado_cidade == True):
            sg.popup('Você obtêm uma média de: ', litros_combustivel*9)
        else:
            if Velocidade_Media >= 122:
                sg.popup("Você está em alta velocidade")
        
    
