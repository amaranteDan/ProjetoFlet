import flet as ft

def main(page: ft.Page):
    page.title = 'Container 2'

    titulo1 = ft.Text('Ficha Cadastral',
                      size=20)
    nome1 = ft.TextField(label= 'Digite seu nome')
    sobrenome1 = ft.TextField(label='Digite seu sobrenome: ')
    data_nasc = ft.TextField(label='Digite sua data de nascimento: ')
    rg1 = ft.TextField(label='Digite seu RG: ')
    cpf1 = ft.TextField(label='Digite seu CPF: ')

    bloco1 = ft.Row(controls=[titulo1])
    bloco2 = ft.Row(controls=[nome1, sobrenome1])
    
    bloco3 = ft.ResponsiveRow(controls=[
        ft.Column(controls=[data_nasc],
                  col= {'sm':6, 'md':4, 'xl': 2}),
        ft.Column(controls=[ft.Row(controls=[rg1, cpf1])],
                  col={'sm':6, 'md': 4, 'xl': 2})          
    ])
                  
    

    page.add(bloco1, bloco2, bloco3)

ft.app(target=main)

