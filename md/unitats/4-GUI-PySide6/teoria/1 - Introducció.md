## 1. Introducció
En aquest primer apartat de la unitat introduirem les tecnologies que utilitzarem per als nostres desenvolupaments Qt i PySide6.

### 1.1. Qt

![Logo_QT](images/QT.png)

Qt és un framework de **desenvolupament d'aplicacions multiplataforma per a escriptori**, sistemes empotrats i sistemes mòbils. Els seus desenvolupaments permeten executar-se a plataformes com Linux, OS X, Windows, VxWorks, QNX, Android, iOS, BlackBerry, Sailfish OS i altres.

No és un llenguatge de programació sinó un conjunt d'eines per al desenvolupament d'interfícies gràfiques d'usuari multiplataforma mitjançant C++.

El desenvolupament de Qt va ser iniciat el 1990 pels programadors noruecs Eirik Chambe-Eng i Haavard Nord. La seua empresa, Trolltech, que venia llicències de Qt i donava suport va passar per diverses adquisicions al llarg dels anys. Avui, l'antiga Trolltech es diu *The Qt Company*. 

Encara que The Qt Company és el principal impulsor de Qt, ara Qt és desenvolupat per un conjunt de companyies més gran: *The Qt Project*. Està format per moltes empreses i persones de tot el món i segueix un model de govern meritocràtic. Tots els que vulguen, particulars i empreses, poden sumar-se al projecte col·laboratiu, escrivint codi o documentació, informant d'errors, ajudant altres usuaris al fòrum o mantenint pàgines al seu wiki.

Qt està disponible sota diverses llicències: The Qt Company ven llicències comercials, però Qt també està disponible com a programari lliure sota diverses versions de GPL i LGPL.

Alguns exemples d'aplicacions desenvolupades amb Qt són:

- Adobe Photoshop Album, per organitzar imatges.
- L'escriptori Kde de les distribucions Linux.
- Last.fm Player, el client descriptori per a streaming de música i ràdio.
- Skype, per a missatgeria i VOIP.
- TeamSpeak, per a la comunicació amb veu àmpliament usada per gamers.
- VirtualBox, per a la virtualització de sistemes.
- LibreOffice, paquet ofimàtic lliure. Alternativa a Microsoft Office.
- OnlyDesktops, paquet ofimàtic lliure competidor de LibreOffice.
- MuseScore, programa per a composició de partitures musicals.


### 1.2. PySide6

![PySide6](images/PySide.png)

PySide és la unió de Python i Qt . Va ser desenvolupat per The Qt Company, com a part del projecte Qt for Python. És una de les alternatives al paquet estàndard Tkinter de Python per crear interfícies. Com Qt, PySide és programari lliure. PySide és compatible amb Linux/X11, macOS i Microsoft Windows, per tant, els nostres desenvolupaments seran compatibles amb qualsevol d'aquestes plataformes amb només un desenvolupament de codi.

!!!warning "Documentació"
    Encara que hi ha documentació específica de PySide disponible, també podem i recomanem utilitzar la documentació de Qt per a C++, tenint en compte que caldrà traduir la sintaxi d'objectes i mètodes C++ per adaptar-lo a Python.

Hi ha hagut tres versions principals de PySide:

- PySide: compatible amb Qt 4
- PySide2: compatible amb Qt 5, la versió més utilitzada de Qt.
- PySide6: compatible amb Qt 6
  
La versió 1 de PySide va ser llançada a l'agost de 2009 sota llicència LGPL per Nokia, llavors propietària de Qt, després de no arribar a un acord amb els desenvolupadors de PyQt, Riverbank Computing. Va recolzar Qt 4 sota els sistemes operatius Linux/X11, Mac OS X, Microsoft Windows, Maemo i MeeGo, mentre que la comunitat PySide va afegir suport per a Android.

Christian Tismer va iniciar PySide2 per portar PySide de Qt 4 a Qt 5 el 2015. Aleshores, el projecte es va incorporar al projecte Qt. Va ser llançat el desembre del 2018. 

PySide6 es va llançar el desembre del 2020. Va afegir suport per Qt 6 i va eliminar el suport per a totes les versions de Python anteriors a la 3.6.

Nosaltres farem ús de PySide6 durant aquest curs.

### 1.3. PySide6 vs Flet

Cadascun dels frameworks té els seus avantatges i inconvenients i haurem de pensar quin és el que més ens convé per al nostre desenvolupament:

Flet és un framework més recent que de moment compta amb poca documentació i no té un respaldament de grans empreses, en canvi ens permet portar els nostres desenvolupaments a web, mòbil o escriptori.

PySide6, per la seua banda compta amb molts anys de desenvolupaments i millores, molta documentació (encara que la majoria està en C++) i el recolzament d'algunes grans empreses. En canvi, la part de Qt que aprendrem en este curs (aplicacions basades en Qt Widgets) sols ens permetran executar-se en escriptori (macOS, Windows i Linux).