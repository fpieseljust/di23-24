# Integració de components en eines de disseny

En els apartats anteriors hem vist com crear nous components i la manera d'utilitzar-los a les nostres aplicacions, directament al codi del programa. Tot i això, també resulta pràctic disposar d'aquests components personalitzats quan dissenyem la interfície per mitjà d'una eina visual de disseny.

En aquest apartat veurem els dos mecanismes que ofereix Qt Designer per poder dissenyar formularis que incloguen components personalitzats:

- Promoció de components.
- Creació de complements (plugins).


## Promoció de components

És possible que durant el disseny de la interfície d'usuari amb Qt Designer no tinguem disponible el component personalitzat que volem fer servir. Per exemple, pot ser que el component no estigui finalitzat, o que sigui específic per a una plataforma i el disseny s'estigui realitzant en una altra de diferent. En aquesta situació, podem utilitzar la funcionalitat de Qt Designer coneguda com a promoció de components.

La promoció de components ens permet com a dissenyadors utilitzar un component que sí que tenim disponible a Qt Designer, en representació del component personalitzat que no tenim. D'aquesta manera podrem fer el disseny de la interfície encara que no disposem del nou control. 

### Promoció del component a Qt Designer

El primer que hem de fer per utilitzar la promoció de components és arrossegar des de la Caixa de ginys de Qt Designer al formulari el component que actuarà com a representant. Si el component personalitzat s'ha creat derivant d'un component existent, l'ideal serà utilitzar aquest component base com a representant. Si no, sempre podem utilitzar com a representant un component de tipus QWidget (que trobem a la secció Containers de la Caixa de widgets).

!!!example "Exemple"
    Si el component personalitzat que no tenim disponible és un nou tipus de botó que heu creat derivant de QPushButton, el representant serà un control d'aquest tipus. Així, el comportament del component al dissenyador a la previsualització serà més proper al que tindrà el nou component quan se substitueixi.

Un cop inserit el component, haurem d'obrir el diàleg Widgets promocionats mitjançant l'opció Promocionar del menú contextual del component.

En aquest diàleg haurem de completar la informació següent:

Nom de la classe promocionada: indicarem la classe del nostre component personalitzat.
Fitxer de capçalera: aquí escriurem el nom del mòdul Python que conté el component (el nom del fitxer de codi sense cap extensió). 

Un cop completada la informació, haurem de prémer el botó Afegeix (que afegirà aquesta configuració de promoció a Qt Designer, per si volem reutilitzar-la), i després al botó Promocionar (que aplicarà aquesta configuració de promoció al component on estem).

Podem degradar un component promocionat de nou al vostre tipus inicial amb l'opció Degradar del menú contextual del component.

!!!example "Exemple"
    El següent fragment conté el disseny d'un formulari en què s'ha utilitzat la promoció de components per poder incloure el cronòmetre desenvolupat en apartats anteriors. S'ha generat amb Qt Designer.

    ~~~xml
    <?xml version="1.0" encoding="UTF-8"?>
    <ui version="4.0">
    <class>MainWindow</class>
    <widget class="QMainWindow" name="MainWindow">
    <property name="geometry">
    <rect>
        <x>0</x>
        <y>0</y>
        <width>460</width>
        <height>297</height>
    </rect>
    </property>
    <property name="windowTitle">
    <string>Ejemplo de promoción</string>
    </property>
    <widget class="QWidget" name="centralwidget">
    <layout class="QVBoxLayout" name="verticalLayout">
        <item>
        <widget class="CronometroUI" name="widget" native="true"/>
        </item>
    </layout>
    </widget>
    </widget>
    <customwidgets>
    <customwidget>
    <class>CronometroUI</class>
    <extends>QWidget</extends>
    <header>DI_U04_A02_01</header>
    <container>1</container>
    </customwidget>
    </customwidgets>
    <resources/>
    <connections/>
    </ui>
    ~~~

### Ús de la interfície dissenyada en una aplicació

Quan el disseny del formulari estigui finalitzat i s'hagin promocionat els components necessaris, arriba el moment d'utilitzar la interfície dissenyada en una aplicació. Com vam veure a la unitat 5, hi ha dos mecanismes per fer-ho: convertint el fitxer UI a Python amb l'eina uic, o carregant-lo directament amb la classe QUiLoader.

Si optem per la primera opció, la promoció de components no introduirà cap canvi respecte al que ja vam aprendre a la unitat 3. Quan l'eina uic generi el codi Python associat al disseny, introduirà la classe promocionada en lloc de la del component que realment arrosseguem des de la Caixa de widgets. A més, afegirà l'ordre import necessària per carregar el mòdul indicat al diàleg de promoció, per la qual cosa el codi generat per uic es podrà utilitzar directament des del nostre programa principal.

Si carregarem el fitxer de disseny amb la utilitat QUiLoader directament, sí que caldrà fer una modificació al nostre programa principal. Abans de carregar el fitxer UI (amb el mètode load de QUiLoader) haurem d'indicar al carregador que el formulari té un nou tipus de component. Per això utilitzarem el mètode registerCustomWidget de QUiLoader, passant-li com a paràmetre la classe associada al nou component. Aquesta referència a la nova classe ens portarà a haver dafegir la clàusula import corresponent.

EXEMPLE

Als recursos de la unitat trobaràs també el fitxer DI_U04_A04_02.py, que conté el programa principal modificat per poder utilitzar el fitxer de disseny DI_U04_A04_01.ui.

[Final de quadre]

4.2 Creació de complements (plugins)

Quan sí que tenim disponible el nou component durant el disseny de la interfície, Qt Designer ens ofereix una alternativa a la promoció de components, que ens permetrà integrar-lo completament a l'eina. Per això haurem de desenvolupar un complement (plugin) associat al nostre component personalitzat.

Quan tinguem el plugin desenvolupat, el nostre component apareixerà a la Caixa de ginys com la resta de controls estàndard de Qt. El desenvolupador podrà arrossegar-lo al formulari, obtenint una representació realista de com el component apareixerà a la seva aplicació.

A. Actualitzar la variable d'entorn PYSIDE_DESIGNER_PLUGINS

El primer pas per fer que el nostre component estigui disponible a Qt Designer és actualitzar la variable d'entorn PYSIDE_DESIGNER_PLUGINS, que contindrà les rutes de tots els connectors que hàgim desenvolupat. Si és el nostre primer plugin, primer haurem de crear la variable d'entorn. Si ja existeix, simplement afegirem la ruta del nou plugin al contingut previ de la variable.


Als enllaços de la unitat s'inclouen articles on s'explica com gestionar les variables d'entorn als sistemes operatius Windows, Linux i MacOS.



B. Crear l' script de registre per al plugin

Al directori del plugin que hem inclòs a la variable d'entorn, a més del fitxer Python del nou component, caldrà incloure un script Python amb la informació que Qt Designer necessita per registrar el component. 

Perquè Qt Designer reconegui correctament el plugin, el nom del fitxer que conté l'script de registre ha d'estar format per la paraula register, seguida del nom del fitxer que conté el nou component.

EXEMPLE

L'script de registre associat al component creat als apartats anteriors (el cronòmetre) s'hauria de dir registerDI_U04_A02_01.py.

[Final de quadre]

En aquest script farem ús de la classe QPyDesignerCustomWidgetCollection, inclosa al mòdul PySide6.QtDesigner. Aquesta classe disposa del mètode estàtic registerCustomWidget que sencarregarà de realitzar el registre del nou component. Aquest mètode rep els paràmetres següents:

type: el nom de la classe del nostre nou component. És l'únic paràmetre obligatori del mètode i cal indicar-lo en primer lloc. Per poder referenciar el nou tipus caldrà incloure a l'script la clàusula import corresponent.
xml: descripció en format Qt UI de com es crearà el component en situar-se en un formulari, incloent valors inicials que s'hagin de donar a algunes de les propietats. 
tool_tip: text d'ajuda que es mostrarà a la Caixa de ginys quan se situï el punter del ratolí a sobre del nou component.
icon: ruta a la icona que es mostrarà a la Caixa de ginys. Pot ser una ruta local o una referència a un recurs.
group: nom del grup de controls a la Caixa de ginys on s'inclourà el component. Heu de coincidir amb el nom que veiem a Qt Designer.
module: nom del mòdul Python on es troba el component (normalment, el fitxer de codi sense l'extensió). Quan utilitzem l'eina uic per generar el codi s'inserirà al resultat una clàusula import per a aquest mòdul.


EXEMPLE

El fitxer DI_U04_A04_03.py inclòs als recursos de la unitat conté l'script de registre complet per al component cronòmetre. També s'hi inclou el fitxer de recursos per a la icona (DI_U04_A04_04.qrc), la pròpia icona (DI_U04_A04_05.png) i el resultat de compilar el fitxer de recursos amb l'eina rcc (DI_U04_A04_06.py). Per poder utilitzar l'script de registre caldria canviar-li el nom tal com s'ha indicat anteriorment (hauríeu d'anomenar registerDI_U04_A02_01.py).

[Final de quadre]

A la següent imatge podem veure com el component s'ha integrat a la Caixa de ginys de Qt Designer (situat dins de la secció Display Widgets), i la forma en què es mostra un cop l'arrosseguem al formulari.




C. Ús de la interfície dissenyada en una aplicació

Quan integrem un nou component a Qt Designer mitjançant un plugin, l'ús del fitxer UI resultant en una aplicació no requereix cap acció especial. Es podrà optar per qualsevol dels dos mètodes comentats a la unitat 3 (conversió a codi Python amb uic, o càrrega directa amb QUiLoader), sense realitzar cap modificació


