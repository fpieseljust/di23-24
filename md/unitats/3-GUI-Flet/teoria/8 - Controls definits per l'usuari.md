## Creació de nous controls per codi.

Els controls són utilitzats, entre altres coses, per amagar la complexitat del programari i transformar-la en parts més manejables. Cada control amaga la seva complexitat darrere d'una interfície formada per les seves propietats i mètodes a què es té accés. Poden introduir-se i eliminar-se, fins i tot ser intercanviats com a part dun tot. 

Això redueix la complexitat del desenvolupament programari i millora el seu manteniment, permetent que el mateix codi puga ser reutilitzat a diferents llocs. El resultat és un bloc de codi encapsulat en una classe independent que passa a formar part del banc de peces disponibles per formar part de desenvolupaments més complexos.

## Controls que hereden d'altres controls

Per començar a desenvolupar un control propi, el més fàcil és buscar un control des del qual partir, de manera que se n'hereten les propietats i mètodes i així poder utilitzar-los en el control que volem crear. 

Per exemple, si voleu un `Container` amb un identificador centrat, podem heretar de `flet.Container` i afegir una propietat *id*:

!!! example "Exemple"
    
    ```python
    import flet as ft


    class ContainerID(ft.Container): # Heredem de Container
        def __init__(self, id: str):
            super().__init__()
            self.id = id # Definim la propietat id

            # Per defecte el creem amb l'identificador centrat, 
            # color de fons AMBER, tamany 150x150 i arredonit
            self.content = ft.Text(id)
            self.alignment=ft.alignment.center
            self.width = 150
            self.height = 150
            self.border_radius = 5
            self.bgcolor = ft.colors.AMBER
            


    def main(page: ft.Page):
        container_id = ContainerID("Identificador")
        container_id.on_click = container_clicked
        page.add(container_id)
        page.update()


    def container_clicked(e):
        print(e.control.id) # Accedim a la propietat que hem definit


    ft.app(target=main)
    ``` 

## Controls que hereden d'*UserControl*

En cas que el nostre control no guarde relació estreta amb altres controls o siga una composició de diversos controls, el més adequat serà heretar de `ft.UserControl` directament, que és la classe base des de la qual hereta la resta de Controls d'usuari. Això ens permetrà construir components reutilitzables combinant els controls Flet existents.

!!! example "Exemple mínim de control d'usuari"

    ```python
    import flet as ft

    class GreeterControl(ft.UserControl):
        def build(self):
            return ft.Text("Hello!")

    def main(page):
        page.add(GreeterControl())

    ft.app(target=main)
    ```
    

UserControl ha d'implementar el mètode **build()** que es crida per crear la interfície d'usuari del control i ha de retornar una únic objecte Control o una Llista de controls. UserControls hereda d'*Stack*, de manera que hi haurà diversos fills els uns sobre els altres. Si necessiteu organitzar la interfície d'usuari del control de manera diferent, podeu utilitzar *Layouts*  com Row o *Column*.

!!! example "Exemple"
    
    ```python
    class GreeterControl(ft.UserControl):
        def build(self):
            return ft.Column([
                ft.TextField(label="Your name"),
                ft.ElevatedButton("Login")
            ])
    ```

!!! warning "Actualització d'UserControl a la interfície"

    Quan es crida al mètode **update()** del control principal, els canvis dins del UserControl no s'apliquen, i per tant, la seua vista no es refresca. UserControl hauria de cridar **self.update()** per enviar els seus canvis a una pàgina de Flet.

    ```python
    import flet as ft


    class Counter(ft.UserControl):
        def __init__(self):
            super().__init__()
            self.counter = 0
            self.text = ft.Text(str(self.counter))

        def add_click(self, e):
            self.counter += 1
            self.text.value = str(self.counter)
            self.update() # Actualitzem la vista

        def subtract_click(self, e):
            self.counter -= 1
            self.text.value = str(self.counter)
            self.update() # Actualitzem la vista

        def build(self):
            return ft.Row([ft.IconButton(ft.icons.REMOVE, on_click=self.subtract_click), self.text, ft.IconButton(ft.icons.ADD, on_click=self.add_click)])


    def main(page):
        page.add(Counter())


    ft.app(target=main)
    ```

    Fixeu-se que a les línies 13 i 18, el control s'actualitza a ell mateix. Proveu a canviar per e.page.update() i comproveu el funcionament.


    