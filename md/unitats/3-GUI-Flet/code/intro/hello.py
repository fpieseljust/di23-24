import flet as ft

def main(page: ft.Page):
    page.title = "Hello world with Flet!!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    text = ft.Text(value='Hello world with Flet!!', text_align=ft.TextAlign.LEFT)

    page.add(
        text
    )

ft.app(target=main)