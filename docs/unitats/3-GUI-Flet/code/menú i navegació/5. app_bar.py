'''Exemple de navegació entre vistes de Flet'''
import flet as ft

def main(page: ft.Page):
    '''Funció principal'''
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        # if page.route == "/": EXPLICAR
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store" or page.route == "/cart":
            page.views.append(
                ft.View(
                    "/store",controls=
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Cart", on_click=lambda _: page.go("/cart")),
                    ],
                )
            )
        if page.route == "/cart":
            page.views.append(
                ft.View(
                    "/cart",
                    [
                        ft.AppBar(title=ft.Text("Cart"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view='web_browser', port=8080)
