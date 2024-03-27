import flet as ft


def main(page):

    nombre = ft.Ref[ft.TextField]()
    apellido = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hola, {nombre.current.value} {apellido.current.value}!")
        )
        nombre.current.value = ""
        apellido.current.value = ""
        page.update()
        nombre.current.focus()

    page.add(
        ft.TextField(ref=nombre, label="First name", autofocus=True),
        ft.TextField(ref=apellido, label="Last name"),
        ft.ElevatedButton("Saludar!", on_click=btn_click),
        ft.Column(ref=greetings),
    )

ft.app(target=main)