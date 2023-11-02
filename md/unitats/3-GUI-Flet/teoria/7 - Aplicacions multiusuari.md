## PubSub

Les aplicacions multiusuari estan dissenyades de forma que les accions d'un usuari en local es repliquen a la sessió d'un usuari remot. 

Pensem per exemple en una aplicació de xat. Quan un usuari envia un missatge, s'hauria de transmetre a totes les altres sessions de l'aplicació i mostrar-lo a les seves interfícies corresponents. Necessitem d'alguna manera, passar missatges d'usuari entre sessions.

Flet proporciona un mecanisme senzill per a la comunicació asíncrona entre sessions anomenat **PubSub**.

PubSub permet emetre missatges a totes les sessions d'aplicacions o enviar-los només a subscriptors específics.

El funcionament bàsic de *PubSub* és:

- *subscribe* - a missatges de difusió o subscriu-te a un tema a l'inici de la sessió de l'aplicació.
- *send* - enviar missatges de difusió o enviar a un tema concret.
- *unsubscribe* - cancel·leu la subscripció als missatges de difusió o cancel·leu la subscripció a un tema.
- *unsubscribe* -  cancel·lem la subscripció de tot en tancar la sessió, *page.on_close*.

!!! example "Xat"

    Aquest és un exemple d'una aplicació de xat senzilla
    
    ```python
    import flet as ft

    def main(page: ft.Page):
        page.title = "Flet Chat"

        # subscribe to broadcast messages
        def on_message(msg):
            messages.controls.append(ft.Text(msg))
            page.update()

        page.pubsub.subscribe(on_message)

        def send_click(e):
            page.pubsub.send_all(f"{user.value}: {message.value}")
            # clean up the form
            message.value = ""
            page.update()

        messages = ft.Column()
        user = ft.TextField(hint_text="Your name", width=150)
        message = ft.TextField(hint_text="Your message...", expand=True)  # fill all the space
        send = ft.ElevatedButton("Send", on_click=send_click)
        page.add(messages, ft.Row(controls=[user, message, send]))

    ft.app(target=main, view='web_browser')
    ```

    <center>
    
    ![Xat](images/xat.gif){width=50%}
    
    </center>

