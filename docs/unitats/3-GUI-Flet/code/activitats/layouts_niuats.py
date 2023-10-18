import flet as ft


def main(page: ft.Page):
    page.title = "Layouts niuats"
    space_beetwen_elements = 10
    row_elements = 5
    column_elements = 8

    def items(count, prefix):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=prefix + str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items

    secondary_row = ft.Row(controls=items(
        row_elements, "H"), spacing=space_beetwen_elements)
    column = ft.Column(controls=items(column_elements, "V"), spacing=space_beetwen_elements)
    main_row = ft.Row(controls=[column, secondary_row],
                      spacing=space_beetwen_elements)
    page.add(main_row)

    page.window_width = (len(secondary_row.controls) + 1) * 50 + \
        (len(secondary_row.controls) + 2) * space_beetwen_elements
    page.window_height = (len(column.controls)) * 50 + \
        (len(column.controls) + 2) * space_beetwen_elements

    page.update()


ft.app(target=main)
