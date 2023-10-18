import flet as ft


def main(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        add_button.disabled = True
        new_task.focus()
        page.update()

    def check_value(e):
        if (new_task.value == ''):
            add_button.disabled = True
        else:
            add_button.disabled = False
        page.update()

    new_task = ft.TextField(label="Tasca pendent",
                            width=300, on_change=check_value)
    add_button = ft.ElevatedButton(
        "Afegir", on_click=add_clicked, disabled=True)
    page.add(ft.Row([new_task, add_button]))


ft.app(target=main)
