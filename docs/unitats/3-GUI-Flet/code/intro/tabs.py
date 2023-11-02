import flet as ft


def main(page: ft.Page):

    tab_names = ["Tab 1", "Tab 2", "Tab 3"]
    tabs_list = []
    for tab in tab_names:
        tabs_list.append(
            ft.Tab(
                text=tab,
                content=ft.Container(
                    content=ft.Text(tab), alignment=ft.alignment.center
                ),
            )
        )

    tabs = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=tabs_list,
        expand=1,
    )

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.TextField(expand=1), ft.TextButton("Prova"),
                    ]
                ),
                tabs

            ]
        )
    )


ft.app(target=main)
