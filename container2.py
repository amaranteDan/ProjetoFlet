import flet as ft

def main(page: ft.Page):
    page.title = 'Container 2'

    titulo1 = ft.Text('Ficha Cadastral',
                      size=20)
    nome1 = ft.TextField(label= 'Digite seu nome')
    sobrenome1 = ft.TextField(label='Digite seu sobrenome: ')

    bloco1 = ft.Row(controls=[titulo1])
    bloco2 = ft.Row(controls=[nome1, sobrenome1])

    page.add(bloco1, bloco2)

ft.app(target=main)

