import PySimpleGUI as sg
import pyautogui as bot


def main():
    # Altera cor de fundo.
    sg.theme_background_color("white")

    # Quebra em camadas
    cabecalho = [
        [sg.Text("Calculadora", font="Inter 16", background_color="white",
                 text_color="#454545", pad=(75, (20, 30)))],
    ]

    primeiro_valor = [
        [sg.Text("Primeiro valor", font="Inter 16",
                 background_color="white", text_color="#454545", pad=(20, (30, 5)))],
        [sg.Input("", font="Inter 12",background_color="white",justification='center',border_width=0, pad=(20,(0,0)))],
        [sg.HSep(pad=(20,(0,0)))]
    ]

    segundo_valor = [
        [sg.Text("Segundo valor", font="Inter 16",
                 background_color="white", text_color="#454545", pad=(20, (30, 5)))],
        [sg.Input("", font="Inter 12",background_color="white",justification='center',border_width=0, pad=(20,(0,0)))],
        [sg.HSep(pad=(20, (0,0)))]
    ]
        
    opcoes = [
        
        if opcao == "+":
           resultado = primeiro_valor + segundo_valor
        elif opcao == "-":
           resultado = primeiro_valor - segundo_valor
        elif opcao == "*":
           resultado = primeiro_valor * segundo_valor
        elif opcao == "/":
           resultado = primeiro_valor / segundo_valor

    ]

    resultado = []

    # Agrupar tudo
    layout = [cabecalho, primeiro_valor, segundo_valor, opcoes, resultado]
    
    # Configurando a tela
    window = sg.Window("Calculadora", layout=layout, size=(268, 490), margins=(
        0, 0), grab_anywhere=True)

    # Laco de repeticao para mostrar essa tela.
    while True:
        # Atribuir os valores de exibicao.
        # event = Todos os eventos que acontecem na tela. Ex: clique no botao.
        # Values = valores dos inputs recebidos na tela.
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break


main()
