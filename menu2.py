import flet as ft

def main(page: ft.Page):
    page.title = 'Menu 2'

    def seleciona_quarto(v):
        quarto.value = (f'Quarto escolhido: {escolha.value}')

        page.update()

    texto1 = ft.Text('Escolha o quarto: ')

    escolha = ft.RadioGroup(
        content = ft.Column([
                ft.Radio(value = 'quarto tipo 1',
                         label = 'Executivo (cama de solteiro + tv + ar)')
            ])
        )
    quarto=ft.Text()

    botao_confirma = ft.ElevatedButton(text = 'Confirma',
                                           on_click= seleciona_quarto)
        
    page.add(texto1, botao_confirma, quarto)

ft.app(target=main)


