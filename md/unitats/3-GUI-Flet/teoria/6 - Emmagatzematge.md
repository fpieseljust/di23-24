## 1. ClientStorage

L'API d'emmagatzematge del client de Flet permet emmagatzemar dades en format clau-valor al client de forma persistent.

El mecanisme d'emmagatzematge real depèn de la plataforma on s'execute l'aplicació Flet:

- Web - Emmagatzematge local.
- Escriptori: fitxer JSON.
- iOS - NSUserDefaults.
- Android - SharedPreferences. 

### 1.1. Escriptura

!!! example "Exemple"
    
    ```python
    # strings
    page.client_storage.set("key", "value")

    # numbers, booleans
    page.client_storage.set("number.setting", 12345)
    page.client_storage.set("bool_setting", True)

    # lists
    page.client_storage.set("favorite_colors", ["read", "green", "blue"])
    ```

!!! note "Accés a la informació guardada"
    
    Cada aplicació de Flutter que utilitza les *shared_preferences*  té el seu propi conjunt de preferències. Com que s'utilitza el mateix client Flet (que és una aplicació Flutter) per executar la interfície d'usuari per a diverses aplicacions Flet, qualsevol valor emmagatzemat en una aplicació Flet és visible/disponible per a una altra aplicació Flet executada pel mateix usuari.

    Per evitar este inconvenient i poder distingir la configuració d'una aplicació d'una altra, es recomana utilitzar algun prefix únic per a totes les claus d'emmagatzematge. Per exemple, per emmagatzemar el token d'una aplicació, podeu utilitzar la clau user1.app1.auth_token, en una altra aplicació user1.app2.auth_token i en altra user2.app1.auth_token.

!!! warning "Compte amb les dades sensibles!"

    És responsabilitat del desenvolupador d'aplicacions Flet encriptar o xifrar les dades sensibles abans d'enviar-les a un emmagatzematge del client, de manera que no es puguen llegir ni manipular per una altra aplicació o usuari de l'aplicació. Ho veurem al final de l'apartat.


### 1.2. Lectura

!!! example "Exemple"
    
    ```python
    # The value is automatically converted back to the original type
    value = page.client_storage.get("key")

    colors = page.client_storage.get("favorite_colors")
    # colors = ["read", "green", "blue"]
    ```

### 1.3. Comprovacr si existeix

!!! example "Exemple"
    
    ```python
    page.client_storage.contains_key("key") # True if the key exists
    ```

### 1.4. Obtindre totes les claus

!!! example "Exemple"
    
    ```python
    page.client_storage.get_keys("key-prefix.")
    ```

### 1.5. Esborrar un valor

!!! example "Exemple"
    
    ```python
    page.client_storage.remove("key")
    ```

### 1.6. Esborra l'emmagatzematge


    !!! example "Exemple"
    
    ```python
    page.client_storage.clear()
    ```
!!! warning "Compte!"
    `clear()` és una funció perillosa que **elimina totes les preferències de totes les aplicacions Flet que haja executat el mateix usuari**. Per tant, les dades permanents de les aplicacions no s'han d'emmagatzemar a l'emmagatzematge del client, sinó a una base de dades, fitxer,...

## 2. SessionStorage

Flet proporciona una API per emmagatzemar dades clau-valor a la sessió de l'usuari en el servidor. La informació estarà disponible fins que l'usuari acabe la sessió (tanque l'aplicació web o finalitze l'execució en escriptori o mòbil). 

L'ús és idèntic al de ClientStorage canviant client_storage per session.

!!! warning "Compte!"

    A la implementació actual de Flet, les dades emmagatzemades no es conserven entre els reinicis de l'aplicació.

## 3. Ús de ClientStorage i de SessionStorage

Els dos mètodes d'emmagatzematge tenen usos diferents i funcionen amb diferents cicles de vida. Quan utilitzar cadascun?

1. ClientStorage:

    - Utilitza clientStorage quan vulguis emmagatzemar dades de forma persistent que persistiran més enllà de les sessions.
    - Les dades emmagatzemades amb clientStorage romanen disponibles fins que esborres explícitament les dades amb remove o clear.
    - És útil per emmagatzemar preferències de l'usuari, configuracions, informació de l'usuari, com ara nom d'usuari, o qualsevol altra dada que l'aplicació necessite recordar entre sessions.
    - Té un àmbit global, cosa que significa que les dades emmagatzemades en clientStorage estan disponibles per a totes les aplicacions Flet, independentment de les finestres o pestanyes obertes.

2. SessionStorage:

    - Utilitza sessionStorage quan vulguis emmagatzemar dades temporalment durant la sessió actual. Aquestes dades s'esborraran quan s'acabe l'execució actual.
    - És útil per a dades que només són rellevants durant una sessió de navegació determinada, com ara les dades del carret de compra en una botiga en línia o les dades temporals d'un formulari web.
    - Com clientStorage, també té un àmbit global i està disponible per a totes les aplicacions durant la sessió actual.

En resum, tria clientStorage quan necessitis emmagatzemar dades que han de ser persistents entre sessions i tria sessionStorage per emmagatzemar dades temporals que només són rellevants durant la sessió actual del navegador.

!!! example "Exemple"
    Imagina un token d'accés a una aplicació. Si el guardem a clientStorage, ens permetria mantindre'ns autenticats entre diferents sessions. En canvi, si ferem ús de sessionStorage, ens obligaria a autenticar de nou en cada reinici o sessió nova.

    Tingues en compte que l'accés és global, i que amb el token, es podrien llançar atacs en aplicacions basades en tokens.

## 4. Encriptació de dades

Les dades sensibles, com ara fitxes, claus, números de targetes de crèdit i altres *secrets* s'haurien d'emmagatzemar, ja siga en bases de dades, fitxers, emmagatzematge del client,... en forma xifrada per evitar atacs i usos fraudulents.

Flet inclou mètodes per xifrar i desxifrar dades de text sensibles mitjançant algorisme simètric (on s'utilitza la mateixa clau per a xifrar i desxifrar).

### Clau secreta

La clau secreta de xifratge és una cadena arbitrària semblant a una contrasenya configurada per un usuari i utilitzada per xifrar i desxifrar dades. L'algoritme de criptografia utilitza una clau secreta per obtindre la clau de xifratge de 32 bytes.

!!! danger "Contrasenyes al codi"

    No poseu mai contrasenyes al codi d'una aplicació. Podrien quedar exposades al públic i ser utilitzades. Les podeu llegir d'un arxiu de configuració, d'una base de dades, d'un servei o d'una variable d'entorn.

    Inclús si distribuim l'aplicació compilada, es podria fer ingenieria inversa i obtindre-la.

A Lliurex, podem definir una variable d'entorn amb:

```bash
$ export MY_APP_SECRET_KEY="contrasenya"
```

Si la voleu fer persistent, la podeu afegir al *bashrc*, l'script que s'executa en iniciar sessió.

En Windows, ho podeu fer a través del Tauler de Control o amb PowerShell:

```PowerShell
[Environment]::SetEnvironmentVariable("MY_APP_SECRET_KEY", "contrasenya", [System.EnvironmentVariableTarget]::Machine)
```

Una vegada definida, la podem obtindre mitjançant *os.getenv* i utilitzar-la per xifrar o desxifrar, amb **encrypt** i **decrypt**.

!!! example "Exemple"
    
    ```python
    import os
    import flet.security as ft_sec

    contrasenya = os.getenv("MY_APP_SECRET_KEY")
    text_sense_xifrar = "Este és un missatge secret!"
    text_xifrat = ft_sec.encrypt(text_sense_xifrar, contrasenya)

    print(f"\nMissatge xifrat: {text_xifrat}\n")

    text_desxifrat = ft_sec.decrypt(text_xifrat, contrasenya)
    print(f"Missatge desxifrat: {text_desxifrat}\n")

    if text_sense_xifrar == text_desxifrat:
        print("El missatge s'ha desxifrat correctament!")
    ```

!!! bug "Xifrfatge vs codificació"

    No és el mateix xifar que codificar. La finalitat del xifratge és protegir la informació, mentre que la finalitat de la codificació és representar la mateixa informació en un format diferent, però en ningun cas ocultar-la.

    Per exmeple, un token no està xifrat, sinó codificat. En [este enllaç](https://jwt.io/) podeu codificar i decodificar tokens.
    
