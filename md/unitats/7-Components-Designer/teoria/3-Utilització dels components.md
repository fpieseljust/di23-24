# Utilització dels nous components en aplicacions.

La creació d'un nou component ens afegeix una nova possibilitat al nostre banc de peces utilitzables. Aquests nous components, ara, poden ser utilitzats en diferents aplicacions per crear desenvolupaments més complexos sense haver de reescriure el codi. Així tenim la possibilitat de reutilitzar codi escrit per nosaltres mateixos o per tercers i utilitzar-lo a les nostres aplicacions. 

## Importació de components

Per fer servir els nostres components, el primer pas sempre serà incorporar el codi dels nostres components a una aplicació amb la instrucció _import_ de python. A partir d'aquest moment, les classes definides en aquests fitxers de codi passaran a estar disponibles a la nostra aplicació.

Estudiem una mica el sistema d'importació de mòduls i paquets de python abans de fer servir els nostres components.

### Mòduls

Un mòdul de python es defineix segons el glossari de python.org com:

!!!note "Objecte de python"
    Un objecte serveix com a unitat organitzativa del codi de Python. Tenen un espai de noms que conté objectes Python arbitraris. Es carreguen mitjançant el procés d'importació.

A la pràctica, un mòdul python és un fitxer .py amb codi.

Per exemple, imaginem que tenim un fitxer _constants.py_ amb el codi _PI=3.14159_ al seu interior. Aleshores usaríem el codi següent, situat a la mateixa ruta que el fitxer de constants, per imprimir el valor de la constant per consola:

~~~py
import constants

print(constants.PI)
~~~

### Paquets

Un paquet de python es defineix segons el glossari de python .org com:

“Un mòdul de Python que pot contenir submòduls o, recursivament, subpaquets. Tècnicament, un paquet és un mòdul de Python amb un atribut __path__.”

Fixa't que un paquet no ha de ser un mòdul, així que no importa si el que estem important està estructurat com un mòdul o com un paquet. Per a un usuari, això és indiferent, ja que la importació funciona de manera anàloga.

A la pràctica, un paquet és una carpeta que conté fitxers de python i altres carpetes. Per crear un paquet, cal crear un directori i al seu interior, un fitxer anomenat __init__.py. Aquest fitxer conté el codi quan es tracta com un mòdul. Es pot deixar buit en cas que vulguem organitzar el nostre codi en una estructura de subcarpetes. També podeu contenir imports implícits.

Vegem un exemple:

~~~
app.py

idiomes/

├── africa/

│   ├── __init__.py 

│   └── suahilli.py

├─── europa/

│   ├── __init__.py

├─── español.py

├── ingles.py

└── __init__.py -> buit

~~~

|  Arxiu   | Contingut    |
| --- | --- |
|   idioma/__init__.py  |   (buit)  |
|   idiomes/africa/__init__.py  |   (buit)  |
|  idiomes/africa/suahilli.py   |  salutació = 'Salamu, Dunia!'   |
|  idiomes/europa/__init__.py   |  from . import espanyol   |
|   idiomes/europa/español.py  |  salutació = 'Hola món!'   |
|  idiomes/europa/ingles.py   |   salutació = 'Hello world!'  |

Utilitzarem aquest paquet al fitxer app.py. El codi quedaria com segueix:

~~~py
from idiomes.africa import suahili

print(suahili.salut)

from idiomes import europa

print(europa.espanyol.salut)

import idiomes.europa.ingles as anglès

print(angles.salut)
~~~

Fixeu-vos que en el primer cas, per utilitzar la salutació a suahilli, hem de fer l'import explícitament per poder-lo fer servir. En el segon cas, ja que tenim l'import en idiomes/europa/__init__.py, només cal importar el paquet europa per poder fer servir la salutació en espanyol. En el darrer cas, necessitem importar el mòdul ingles.py per poder fer servir la salutació en aquest idioma.

Si executem el codi, obtenim el resultat següent per consola:

~~~console
Salamu, Dunia!

Hola món!

Hello world!
~~~

!!!note "Nota"
    Aquesta forma d'estructurar i usar els paquets i mòduls, pot servir-vos per mantenir el codi dels vostres components organitzats de forma lògica i còmoda per utilitzar-lo en el desenvolupament de projectes.

## Ús de components a l'aplicació principal

Un cop importat el component a la nostra aplicació, procedim a utilitzar-lo com qualsevol altre component de la llibreria PySide6. El primer pas serà crear les instàncies que en necessitem, per posteriorment actuar sobre l'objecte. Tindrem disponibles totes les propietats i els mètodes públics que hagi heretat de la seva classe base, més les propietats i mètodes que us haguem definit en la seva implementació.

### Exemple cronòmetre

Continuant amb l'exemple del cronòmetre, incorporarem el nostre component a una aplicació.

Com hem indicat, el primer pas consistirà a importar el nostre component:

~~~py
from cronoimetre import CronometroUI
~~~

A més necessitem importar també el nostre arxiu de recursos compilat, ja que si et fixes a l'arxiu recursos_a03.qrc, veureu que hem definit un recurs cronometro.png per carregar la nostra icona d'aplicació.

~~~py
import recursos_a03.py 
~~~

Amb els mòduls necessaris incorporats al nostre codi, utilitzarem el nostre component com ho faríem amb qualsevol altre component de la PySide6. En aquesta ocasió crearem una aplicació que estigui sempre al *system tray* o safata del sistema. Anem a veure el codi per aconseguir aquest propòsit.

Primer creem l'aplicació i configurem que no es tanque en tancar l'última finestra (perquè es mantinga a la safata del sistema encara que tanquem la finestra) i assignem una icona.

~~~py
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    app.setWindowIcon(QIcon(":/icons/cronometro.png"))
~~~

Assignem una icona a la safata del sistema i connectem el senyal activated perquè ens mostri/oculti la finestra d'execució de l'aplicació:

~~~py
    icon = QIcon(QIcon(":/icons/cronometro.png"))
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.activated.connect(mostrar_ocultar)
~~~

Seguidament instànciem al component i li assignem un títol. També configurem que sempre siga visible, per quan fem clic a la icona de l'aplicació a la safata del sistema ens mostre l'aplicació.

~~~py
    cronometro.setWindowTitle("Cronòmetre PySide6")
    cronometro.setWindowFlag(Qt.WindowStaysOnTopHint)
~~~

Finalment, ens queda afegir la possibilitat d'acabar l'aplicació des de la safata del sistema. D'altra manera, només seria possible acabar matant el procés, ja que en tancar la finestra l'aplicació es manté en execució. 

Per fer-ho, creem una acció de sortir a la qual connectem l'slot *quit* de l'aplicació. Finalment, afegim aquesta acció a un menú contextual que apareixerà en fer clic amb el botó secundari del ratolí sobre la icona de l'aplicació a la safata del sistema.

~~~py
    accion_sortir = QAction("Sortir", cronòmetre)
    accion_salir.triggered.connect(app.quit)
    menu = QMenu()
    menu.addAction(accion_sortir)
    tray.setContextMenu(menu)
~~~

### Ús del senyal del component

Quan creem el component, definirem un senyal que s'emetia sempre que el temps a què arriba el cronòmetre coincidira amb el temps d'avís i el checkbox d'avisar estigués marcat. Farem ús daquest senyal.

El disseny del component no defineix un comportament predeterminat a l'esdeveniment en complir-se el temps d'avís, sinó que simplement s'emet el senyal acompanyat d'un missatge, així que ens dota de llibertat total per utilitzar aquest senyal i connectar-lo a l'*slot* que definim a la nostra aplicació.

Nosaltres la farem servir per mostrar un QMessageBox amb el missatge que ens envia el senyal informant que el temps s'ha complert. No és obligatori fer servir aquest missatge, podem utilitzar el nostre propi missatge si així ho desitgem.

~~~py
cronometro.mensaje.connect(mostrar_aviso)

@Slot()
def mostrar_aviso(missatge):
    QMessageBox.information(cronometre, "Cronòmetre PySide6", missatge)
~~~

## Ús de decoradors a Python

T'hauràs fixat en l'apartat anterior que fem servir la instrucció @Slot() abans de definir l'slot. Veurem en aquest apartat què són els decoradors i com podem utilitzar-los als nostres components per no haver de reescriure el codi de les aplicacions si volem canviar la implementació dels components.

### Decoradors

Una funció de decorat o un decorador és bàsicament una funció que afegeix nova funcionalitat a una funció que es passa com a argument. Això ens permet afegir una funcionalitat nova a una funció existent sense modificar el codi de la funció original ni el codi on aquesta funció s'utilitza.

Fixa't al següent fragment de codi. 

~~~py
def funcio():
    print("Funcionalitat original")

funcio()
~~~

Si executem la funció, obtindrem per pantalla *Funcionalitat original*. Com podem afegir una nova funcionalitat sense tocar el codi de la funció original? Aquí és on entren en joc els decoradors.

Afegim un decorador a la funció original:

~~~py
def decorador(funcio_original):
    def nova_funcio():
        print("Funcionalitat extra")
        funcio_original()
    return nova_funcio

@decorador
def funcio():
    print("Funcionalitat original")
funcio()

Si ara executem de nou el codi, la sortida per consola mostrarà els dos missatges:

~~~console
Funcionalitat extra
Funcionalitat original
~~~

Analitzem una mica el codi. La funcio decoradora rep com a paràmetre una funció (funcio_original) i té una funció imbricada una altra funció (nova_funcio). La funció original s'executa dins de la nova funció per mantenir la seva funcionalitat mentre afegeix nova funcionalitat a la crida. La funció decoradora torna la nova funció, així que en executar una funció que decorem amb aquesta funció decoradora, s'executarà la funció original més la funció afegida sense canviar la implementació de la funció original.

### El decorador @Slot()

Encara que PySide6 permet que qualsevol objecte *callable* de Python, com són les funcions, es facin servir com a ranures quan es connecten a senyals, de vegades cal marcar explícitament un mètode de Python com una ranura Qt. 

PySide6 proporciona el decorador de funcions Slot() per fer-ho. A més, connectar un senyal a un mètode Python decorat també té l'avantatge de reduir la quantitat de memòria utilitzada i és una mica més ràpid, així que és recomanable, encara que no necessari utilitzar-los a les ranures.

### El decorador @property

Partim del codi següent:

~~~py
class Component:
    def __init__(self, atribut):
        self.atributo = atribut

component = Component(10)
print(component.atributo)
~~~

Aquest atribut d'instància és públic perquè el seu nom no té un guió baix, per declarar-lo com a protegit, ni un doble guió baix, per declarar-lo com a privat. Atés que l'atribut és públic podem accedir-hi directament des de fora de la classe per imprimir-lo com és el cas.

En executar el codi, veurem a la consola el text 10.

Però suposem que ens demanen que protegim aquest atribut passant-lo a privat i validem que el valor és un enter positiu abans d'assignar-lo. Com ho fem?

Si canviem el codi i el passem a privat, ja no hi podrem accedir des de fora de la classe:

~~~py
class Component:
    def __init__(self, atribut):
        self.__atribut = atribut

component = Component(10)
print(component.__atribut)
~~~

En executar el codi no sortirà un error com el següent:

_AttributeError: 'Component' object has no attribute '__atribut'._

En aquest punt, el més probable és que decidiu afegir mètodes getters i setters per llegir i assignar el valor de l'atribut. Però això té un problema gravíssim. Si la classe ja està en ús en algun projecte, fallarà el programa a cada línia que llegiu o assigneu l'atribut, ja que anteriorment era públic i estem obligant els desenvolupadors a canviar el seu codi en canviar la nostra classe.

Però aquí és on podem fer ús del decorador @property, de manera que canviarem la nostra classe sense obligar a canviar el codi de les aplicacions que en fan ús.

Reescrivim aleshores la nostra classe amb el decorador @property:

~~~py
class Component:
    def __init__(self, atribut):
        self.__atribut = atribut

    @property
    def atribut(self):
        return self.__atribut

    

    @atribut.setter
    def atribut(self, nou_valor):
        if nou_atribut > 0 and isinstance(nou_atribut, int):
            self.__atribut = nou_valor
        else:
            print("Per favor, introduïu un valor enter positiu per a l'atribut")
~~~

Ara, no caldria reescriure el codi de l'aplicació, ja que en llegir el valor d'atribut, s'executaria el getter atribut(), retornant el valor de l'atribut privat. I en assignar el valor, s'executaria el setter atribut(nou_valor).

Si utilitzem la classe amb el codi següent:

~~~py
component = Component(10)
print(component.atributo)
component.atribut = -1
print(component.atribut)
component.atribut = 20
print(component.atribut)
~~~

El resultat seria el següent:

~~~console
10
Si us plau, introduïu un valor enter positiu per a l'atribut
10
20
~~~

Fixeu-vos que en intentar assignar un valor negatiu, l'atribut no canvia de valor, sinó que simplement llança l'avís per consola.

En resum, en definir propietats de components, podem canviar la implementació interna sense afectar els programes, per la qual cosa podem afegir getters i setters que actuen com a intermediaris de manera transparent per evitar accedir o modificar les dades directament. En farem ús a les tasques.