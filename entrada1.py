# Usando o prefixo e sufixo

import flet as ft

def main(page: ft.Page):
    page.title = 'Entrada de dados'
    
    #Tema da pagina
    page.theme_mode = ft.ThemeMode.DARK
   


    txt1 = ft.Text('Valor final: ', size=16)
    val1 = ft.TextField(label='Digite o valor inteiro',
                        prefix_text='R$ ')
    
    txt2 = ft.Text('Desconto aplicado: ', size=16)
    val2 = ft.TextField(label='Digite o percentual',
                        suffix_text='%')
    
    page.add(txt1,val1, txt2, val2)

ft.app(target=main)

