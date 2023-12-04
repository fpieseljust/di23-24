## 1. Aplicacions multiplataforma

Són aquelles aplicacions que són desenvolupades en un únic llenguatge o *framework* i que faciliten la seua exportació i execució a diversos dispositiu, de manera independent al sistema operatiu.

### 1.1. Aproximacions

Per tal de minimitzar el desenvolupament específic par a cada plataforma, i el cost que això suposa, apareixen diverses tecnologíes, centrades sobretot en tecnologíes web. Dins d’aquestes, disposem d’un gran ventall de possibilitats:

- **Aplicacions web responsives**: Es tracta d’aplicacions basades en tecnologia web: HTML, CSS i JavaScript, que adapten la seua interfície a qualsevol dispositiu (disseny responsive). Aquestes aplicacions no requereixen de cap desenvolupament natiu, ja que s’executen sobre el propi navegador web del sistema. Així doncs, disposem d’ún codi únic, però que no ofereixen una experiència d’usuari tan fluïda com les aplicacions natives, ni permeten l’accés a tots els components del sistema.

- **Aplicacions híbrides**: Es tracta d’aplicacions web responsives que es carreguen dins un component de tipus WebView del sistema, que no és més que un navegador sense la barra de navegació, pel que presenta l’aparença d’una aplicació nativa. Aquestes aplicacions, a més, també permeten l’accés a través del WebView a algunes característiques del dispositiu, com la ubicació o l’acceleròmetre. El framework per al desenvolupament d’aplicacions híbrides més popular és Ionic, que permet el desenvolupament amb altres frameworks web com React, Angular o Vue.

- **Aplicacions web progressives (PWAs)**: Les PWAs segueixen sent aplicacions web, però que gràcies a determinats components, com els Service Workers i altres tecnologies estan més a prop de les aplicacions natives, de manera que permeten traure major potencial d’aquestes, accedint al maquinari, treballar amb poca connexió o sense ella, o oferir notificaions del sistema. Existeixen diversos frameworks per al desenvolupament de PWAs, entre els quals es troben React PWA Library, Angular PWA Framework, Vue PWA Framework, Ionic PWA Framework, Svelte, PWA Builder o Polymer.

Com hem comentat, aquests tres tipus d’aplicacions es basen en l’ús de tecnologíes web i algun component, bé siga el propi navegador o un WebView. Tot i que hi ha apliccions molt bones basades en aquestes tecnologíes, no aporten totes les funcionalitats ni la fluïdesa d’una aplicació nativa.

Un pas més enllà en el desenvolupament multiplataforma es troben els frameworks que, partint d’un mateix codi base, generen aplicacions compilades de forma nativa per als diferents sistemes operatius. Algunes de les tecnologies més utilitzades en aquest tipus d’aplicacions són:

- **React Native i Native Script**: Que utilitzen com a base el llenguatge de programació JavaScript, però en lloc de construir les interfícies mitjançant HTML, utilitzen components propis del framework que són compilats a codi natiu, fent ja innecessari utilitzar un WebView com a intermediari.

- **Flutter**: Aquest framework, creat i mantingut per Google permet el desenvolupament d’aplicacions multiplataforma mitjançant el llenguatge Dart. Aquestes aplicacions són compilades a codi natiu dels diferents sistemes operatius (Android, iOS, Linux, Windows) i fins i tot web. Flutter, és a més la tecnología nativa del sistema operatiu Google Fuchsia, basat en el seu propi microkernel Zircon, i que a mitjà o llarg termini podria ser el reemplaç d’Android.

## 2. Introducció
En aquest primer apartat de la unitat introduirem les tecnologies que utilitzarem per als nostres desenvolupaments, Python, Flutter i Flet.



### 2.1. Python

![Logo de Python](images/Python.png)

™/®Python Software Foundation, GPL <http://www.gnu.org/licenses/gpl.html>, via Wikimedia Commons

Python és un llenguatge de programació multiparadigma, interpretat, multiplataforma i lliure. Va nàixer de la mà de Guido Van Rossum, un programador holandés, i la seua primera versió va ser publicada el 1991. 

Característiques:

- **D'alt nivell**: proper a llenguatge de l'ésser humà i no al llenguatge màquina binari.
- **Interpretat**: s'executa en qualsevol màquina que tinga un intèrpret de Python. Això suposa un gran avantatge a l'hora de fer petits canvis de forma ràpida, ja que elimina la necessitat de recompilar el codi.
- **Multiparadigma**: podem fer servir la programació modular, estructurada o l'orientació a objectes segons les nostres necessitats.
- **Multiplataforma**: permet que el codi siga executat en diferents sistemes operatius.
- **Lliure**: és propietat de la Python Software Foundation i està publicat sota llicència PSF-License que és compatible amb GPL (General Public License), la qual cosa significa que és de lliure ús i distribució, fins i tot per a ús comercial.
- **Net i llegible**: posa l'accent en la seua llegibilitat, cosa que ho fa fàcilment comprensible i fàcil d'aprendre. Si ja heu treballat amb qualsevol altre llenguatge de programació, us resultarà fàcil l'ús de Python.
- **Tipat fort i dinàmic**: encara que les variables són d'un tipus concret, no tenim la necessitat de declarar-los, sinó que l'assignació de tipus s'anirà en temps d'execució.
- **Àmplia comunitat**: gràcies a la seua popularitat compta amb un ampli suport i es pot trobar fàcilment molta documentació, esdeveniments, conferències, etc.

Actualment ocupa el **primer lloc al rànquing TIOBE**, que és un prestigiós indicador de la popularitat dels llenguatges de programació que s'actualitza un cop al mes. No només això, sinó que a més mostra una tendència creixent davant de llenguatges com C o Java, que mostren la tendència contrària. Això és degut en gran manera al seu ús majoritari en camps com la Intel·ligència Artificial, el Big Data, el Machine Learning o la Ciberseguretat, àrees predominants en un futur proper. 

!!!warning "TIOBE"
    És important assenyalar que l'índex TIOBE no tracta d'escollir el millor llenguatge de programació o el llenguatge en què s'han escrit la majoria de les línies de codi.

Tot això ens ha portat a escollir aquest llenguatge de programació per al present curs.

!!!example "Vegem la comparació entre “Hola Món!” de Java i de Python"

    === "Java"
        ~~~Java
        public class HolaMón {
            public static void main(String[] args) {
                System.out.println("Hola Món!");
            }
        }
        ~~~

    === "Python"
        ~~~py
        print("Hola món!")
        ~~~

!!!warning "Versions de Python"
    Hi ha dues versions de python no compatibles entre elles, la versió 2 i la versió 3.
    **Nosaltres utilitzarem la versió 3 de python.**

### 2.2. Flutter

![Logo de Flutter](https://docs.flutter.dev/assets/images/shared/brand/flutter/logo+text/horizontal/default.svg)

Flutter és un framework de codi obert desenvolupat per Google que es fa servir per a la creació d'aplicacions mòbils per a diferents plataformes, com Android i iOS, així com per a aplicacions per a la web i escriptori. Les seves principals característiques són les següents:

- **Desenvolupament multiplataforma**: Flutter permet als desenvolupadors crear una sola base de codi que pot ser utilitzada per a desplegar aplicacions en diverses plataformes. Això significa que pots desenvolupar una aplicació i fer-la funcionar en dispositius Android, iOS, la web i fins i tot en altres plataformes com Windows o macOS.

- **Llenguatge de programació Dart**: Flutter fa servir el llenguatge de programació Dart com a base. Dart és un llenguatge modern i eficient que es compila a codi nativo, la qual cosa millora l'eficiència de l'aplicació i el seu rendiment.

- **Widgets personalitzats**: Flutter ofereix una àmplia gamma de widgets personalitzats que es poden utilitzar per a crear una interfície d'usuari atractiva i dinàmica. Aquests widgets són altament personalitzables i permeten als desenvolupadors dissenyar aplicacions amb un aspecte i comportament únic.

- **Ràpides actualitzacions d'UI**: Flutter utilitza un sistema de composició de l'interfície d'usuari (UI) basat en widgets que permet actualitzacions ràpides i eficients de la UI. Això significa que les animacions i les interaccions són suaus i responsives.

- **Hot Reload**: Aquesta característica permet als desenvolupadors veure els canvis immediatament a mesura que editen el codi font, sense necessitat de reiniciar l'aplicació. Això accelera el procés de desenvolupament i la depuració.

- **Suport de tercers**: Flutter té un ecosistema actiu i en creixement de paquets i extensions que faciliten l'accés a funcionalitats i integracions diverses. Això fa que sigui fàcil d'integrar amb altres serveis i biblioteques.

- **Altes prestacions i rendiment**: Gràcies a la compilació a codi natiu, les aplicacions Flutter solen tenir un bon rendiment i una càrrega ràpida.

- **Comunitat activa**: Flutter té una comunitat àmplia i actiu, amb molts recursos en línia, tutorials i ajuda disponible per a desenvolupadors.

En resum, Flutter és una opció atractiva per a desenvolupadors que volen crear aplicacions mòbils i multiplataforma amb un aspecte i comportament personalitzats, així com un alt rendiment i un cicle de desenvolupament eficient. La seva versatilitat i la seva creixent popularitat han fet que sigui una eina rellevant en el món del desenvolupament d'aplicacions.

### 2.3. Flet

![Logo de Flet](https://raw.githubusercontent.com/flet-dev/flet/main/media/logo/flet-logo.svg)

Flet és un framework que permet crear aplicacions GUI tant web, com d'escriptori com per a mòbils. Tot i que el projecte vol incorporar la possibilitat d'utilitzar diversos llenguatges de programació com C++ o Go, actualment sols permet la creació d'aplicacions amb Python.

Els controls de Flet es basen en els controls Flutter de Google, combinant controls més menuts, ocultant complexitats i aplicant valors predeterminats raonables per garantir que les nostres aplicacions tinguen un aspecte professional sense molts esforços.

En definitiva, farem ús dels controls de Flutter des de Python.