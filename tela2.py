import flet as ft

def main(page: ft.Page):
    page.title = 'Tela 2'

     #Tema da pagina
    page.theme_mode = ft.ThemeMode.DARK

    base = {'Nome':'',
            'Sobrenome':''}
    
    def cadastra(dados):
        base['Nome'] = nome1.value
        base['Sobrenome'] = nome2.value

    nome1 = ft.TextField(label = 'Digite o nome: ')
    nome2 = ft.TextField(label = 'Digite o sobrenome: ')

    botao_cadastrar = ft.FilledButton(text = 'Cadastrar',
                                      on_click=cadastra)

    page.add(nome1, nome2, botao_cadastrar)

ft.app(target=main)
