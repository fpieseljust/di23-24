## Activitat 1 - Habilitació i deshabilitació de controls

Partint del següent codi vist en la teoria:

```python
import flet as ft

def main(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(label="Tasca pendent", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Afegir", on_click=add_clicked)]))

ft.app(target=main)
```

Modifica'l per a que el botó `Afegir` es desactive **sempre** que la caixa de text *new_task* estiga en blanc.

!!! tip "Pistes"
    - La caixa de text estarà buida en diferents ocasions, al principi, en afegir una tasca i en borrar un text introduït.
    - Fes ús de `disabled` per a canviar l'estat del control.
    - Investiga quins esdeveniments es produixen al borrar el text. 


## Activitat 2 - Layouts niuats

Un layout és un control que a la vegada pot contindre altres controls. Aleshores, podem niuar diversos layouts per dissenyar la nostra aplicació com desitgem.

Desenvolupa una aplicació on pugam canviar (modificant una variable al codi) el nombre d'elements en una columna i en una fila. El tamany de la finestra s'ha de calcular automàticament segons el nombre d'elements que definim, encara que després es podrà reassignar el seu tamany:


<figure markdown>
  ![](images/niuats10.png){ width="300" }
  <figcaption>10 elements en la columna i 10 en la fila</figcaption>
</figure>

<figure markdown>
  ![](images/niuats8-5.png){ width="300" }
  <figcaption>8 elements en la columna i 5 en la fila</figcaption>
</figure>

!!! tip "Pista"
    - Per a canviar el tamany fes ús de la propietat page.window_width i page.window_height.
    - Pensa quants i de quin tipus són els layouts abans de començar a desenvolupar.
    

<!-- ## 4. Barres de ferramentes, barra d'estat i menús.

### **Activitat 3** - Sistema d'ajuda

L'ajuda "What's This?" o "Qué es esto?" és part del sistema d'ajuda en línia d'una aplicació i brinda als usuaris informació sobre la funcionalitat i l'ús d'un control en particular. 

QWhatsThis proporciona una sola finestra amb un text explicatiu que apareix quan l'usuari fa clic sobre "What's this?" seguit d'un altre clic sobre un control. La forma per defecte perquè els usuaris facen la pregunta és prémer Shift+F1 per activar el mode *ajuda*. El text d'ajuda apareix al fer clic, amb el mode d'ajuda activat, sobre un control; desapareix quan l'usuari torna a fer clic. 

Per entrar en el mode ajuda necessitem cridar al mètode estàtic (no necessites declarar un objecte de la classe) **enterWhatsThisMode()** mentre que per ixir es cridarà a **leaveWhatsThisMode()**. Podem saber si el tenim activat o no usant **inWhatsThisMode()**.

Creeu una aplicació amb un component tipus *dock* (flotant) que continga un **QTextEdit** i un component principal. Per defecte el *dock* se situarà a la part superior de la finestra.

Afegeix una acció “Imprimeix en *dock*” que imprimirà “Acció Polsada” al component flotant en fer clic sobre ella. La drecera serà Ctrl + P i a més apareixerà en una barra d'eines i en un menú. El vostre text d'ajuda serà "En executar aquesta acció s'afegirà el text "Acció polsada" al *dock*. 

En resum, es pot llançar per Menú -> Imprimir a *dock*, amb Ctrl + P o fent clic al botó corresponent de la barra d'eines.

Afegeix un botó *Què és això?* a l'aplicació amb el comportament habitual, és a dir, entrar o eixir del mode ajuda.

![Whats this](images/imprimir_dock.png)

## 5. Diàlegs i altres finestres.

### **Activitat 4** - Dialegs per obrir o guardar.

A la pràctica de l'apartat anterior [(Pràctica 3)](../tasques/2%20-%20Pràctiques.md#practica-3-editor-de-text), havíem començat a desenvolupar un editor de text molt simple que permetia carregar i guardar “arxiu.txt” situat a la mateixa ruta des de la qual executàvem el codi.

En aquest cas pràctic, utilitzarem dos diàlegs, un per demanar quin fitxer obrir i un altre per demanar en quin fitxer volem desar els canvis. En cas que ja hi haja un fitxer obert, en donar a desar no demanarà la ruta al fitxer, sinó que utilitzarà la ruta del fitxer obert anteriorment, sobreescrivint-lo.

A més, afegirem una entrada de menú “Tancar” per tancar l'arxiu obert actualment i començar-ne un de nou. -->
