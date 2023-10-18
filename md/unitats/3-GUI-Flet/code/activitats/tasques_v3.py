import flet as ft


def main(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task_text.value))
        new_task_text.value = ""
        add_button.disabled = True
        new_task_text.focus()
        page.update()

    def check_value(e):
        add_button.disabled = new_task_text.value == ''
        add_button.update()

    new_task_text = ft.TextField(
        hint_text="Tasca pendent", width=300, on_change=check_value)
    add_button = ft.ElevatedButton(
        "Afegir", on_click=add_clicked, disabled=True)
    page.add(ft.Row([new_task_text, add_button]))


ft.app(target=main)
