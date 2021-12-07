import random   
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import G


class Gerador:
    def __init__(self):
        sg.theme('Black')
        self.layout = [
            [sg.Text('Site/Software'), sg.Input(key='site')],
            [sg.Text('Login'), sg.Input(key='login')],
            [sg.Text('Tamanho'), sg.Combo(values=list(range(30)), key='tam', default_value=1)],
            [sg.Button('Gerar'), sg.Button('Salvar')]
        ]
        
        self.janela = sg.Window('Gerador de Senhas', self.layout)

    def iniciar(self):
        while True:
            eventos, valores = self.janela.read()

            if eventos == sg.WINDOW_CLOSED:
                break

            if eventos == 'Gerar':
                nova_senha = self.gera_senha(valores)
                print(nova_senha)
                pass

            if eventos == 'Salvar':
                self.salva_senha(nova_senha, valores)
                pass

    def gera_senha(self, valores):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh1jklmnopqrstuvwxyz123456789!@#$&*'
        sorteado = random.choices(chars, k=int(valores['tam']))
        senha = ''.join(sorteado)
        return senha

    def salva_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"Site/Software: {valores['site']}\nLogin: {valores['login']}\nSenha: {nova_senha}\n\n")


        print("Senha salva.\n")

       
gen = Gerador()
gen.iniciar()
