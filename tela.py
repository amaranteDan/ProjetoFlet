import flet as ft

def main(page):
    page.title = "Tela 1"

    txt1 = ft.Text('Nome: ', size = 16)
    nome1 = ft.TextField(label= 'Digite seu nome: ')

    txt2 = ft.Text('Senha:', size = 20)
    senha1 = ft.TextField(label='Digite a senha: ', password=True, can_reveal_password=True)

    page.add(txt1, nome1, txt2, senha1)

ft.app(target=main)


