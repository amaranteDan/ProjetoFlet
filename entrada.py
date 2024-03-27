import flet as ft

def main(page: ft.Page):
    page.title = 'Entrada de dados'

    txt1 = ft.Text('Nome: ', size = 16)
    nome1 = ft.TextField(label = 'Digite seu nome: ')

    page.add(txt1, nome1)

ft.app(target=main)
    