## 1. Pràctica 1 - "Troba el número"

Es pretén implementar un joc l'objectiu del qual és trobar el número buscat. A la pantalla es veuran una sèrie de números que al clicar sobre ells et portaran a una nova vista indicant si és el número trobat o per contra no és el número que es buscava. El joc acabarà en trobar el número buscat, moment en què es ja no es podrà clicar sobre estos i apareixerà un botó per reiniciar el joc. El número de ítems es podrà canviar programàticament simplement canviant el valor d'una de les variables al codi.

!!! tip "Aplica la POO"
	Fins ara hem utilitzat la programació estructurada per als nostres desenvolupaments amb Flet. Passa al paradigma de programació orientat a objectes per a facilitar el desenvolupament del joc.

	```python
	import flet as ft
	

	class App:
		def __init__(self) -> None:
			ft.app(target=self.main)
			...

		def main(self, page: ft.Page):
			self.page = page
			...

	if __name__ == "__main__":
    	app = App(25)
	```
  

Observeu el següent vídeo on es mostra el comportament del joc:

<center>

  ![Joc Dark Theme](images/joc_dark.gif){ width=100% }
  <figcaption>Dark Theme</figcaption>

</center>



<center>

  ![Joc Light Theme](images/joc_light.gif){ width=100% }
  <figcaption>Light Theme</figcaption>

</center>

## 2. Projecte ToDo APP

Anem a desenvolupar, a través d'una sèrie de pràctiques, una aplicació completa ToDo. 

### 2.1. Pràctica 2 - Editar i modificar tasques

Partint del teu codi de l'activitat 1, anem a afegir la funcionalitat de destacar la tasca, editar-la i eliminar-la, tal com es mostra a continuació:

<center>

![ToDo APP](images/task_2.gif)

</center>

Fixeu-se que abans d'eliminar la tasca, l'usuari ha de confirmar que la vol eliminar.

Fes que no calga utilitzar el clic a `Afegir` per a afegir la tasca, ni fer el clic al `check` per a confirmar el canvi en la descripció de la tasca. En els dos casos, s'ha d'executar automàticament en donar-li a la tecla `Enter`.

!!! tip "Pulsació de Enter en un TextField"

	El control TextField llança un esdeveniment on_submit en donar-li a la tecla `Enter`.

!!! tip "Focus"
	Fes que el focus vagen adoptant-lo els controls adequats en cada situació. Per exemple, en editar el nom de la tasca, el textfield deuria prendre el focus per evitar que l'usuari haja de fer clic per a començar a escriure. Idem per a botons en dialegs.