import flet as ft

def main(page: ft.Page):
    page.title = 'Container 1'
    page.bgcolor = 'white'

    bloco1 = ft.Container(
        content=ft.Text('Ficha Cadastral',
                        color ='black',
                        size=20,
                        weight='bold'),
        bgcolor = ft.colors.BLUE_100,
        border_radius=ft.border_radius.all(25),
        padding=5                
    )

    bloco2 = ft.Container(
        content=ft.TextField(label= 'Digite o seu nome:',
                             color='black',
                             value= 'Nome Completo'),
        bgcolor= ft.colors.AMBER_50,
        border_radius= ft.border_radius.only(bottom_left=5,
                                             bottom_right=25),
                                             padding=5                     

    )

    page.add(bloco1, bloco2)

ft.app(target=main)



