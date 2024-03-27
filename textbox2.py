import flet as ft

def main(page: ft.Page):
    def btn_click(e):
        if not txt_valor.value:

            txt_valor.error_valor = 'Enter com um valor inteiro'
            page.update()

        else:
            valor = int((txt_valor.value + txt_valor1))
            page.clean()
            page.add(ft.Text(f"O valor, {valor}"))

    txt_valor = int(input("Digite um valor"))
    #txt_valor = ft.TextField(label='Digite o valor1')
    #txt_valor1 = ft.TextField(label='Digite o valor2')

    page.add(txt_valor, txt_valor1, ft.ElevatedButton("Calcular", on_click=btn_click))

ft.app(target=main)





