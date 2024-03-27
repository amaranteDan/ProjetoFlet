import flet as ft

def main(page: ft.Page):
    page.title = 'Menu Dropdown'

    def seleciona_pais(v):
        pais.value = (f'Pais escolhido: {escolha.value}')
        
        page.update()

    texto1 = ft.Text('Selecione o pais de origem: ')

    escolha = ft.Dropdown(width = 200,
                            hint_text='País',
                            options = [ft.dropdown.Option('Brasil'),
                                        ft.dropdown.Option('Alemanha'),
                                        ft.dropdown.Option('França'),
                                        ft.dropdown.Option('Rusia'),
                                        ft.dropdown.Option('Japão')],
                            autofocus=True)
    pais = ft.Text()
        
    botao_seleciona = ft.ElevatedButton(text = 'Seleciona',
                                            on_click=seleciona_pais)
        
    page.add(texto1, escolha, botao_seleciona, pais)

ft.app(target=main)

