## Introducció al disseny d'informes

A totes les organitzacions, els processos de presa de decisions es basen en informació sobre l'activitat de l'organització. La forma en què s'obté i s'ofereix aquesta informació varia molt d'uns casos a uns altres, però l'objectiu és sempre facilitar la tasca a les persones que han de prendre aquestes decisions dins de l'empresa.

!!! note "Business intelligence"
    Tot allò relacionat amb la transformació de la informació en coneixement per a la millora de la presa de decisions a les organitzacions s'engloba sota el terme intel·ligència empresarial o de negocis (en anglès, business intelligence).


Una de les maneres habituals de presentar la informació és com un informe. Encara que hi ha diferents tipus d'informe (com veurem més endavant), podríem dir que un informe és un mitjà per proporcionar informació d'utilitat en un format predefinit. Moltes vegades, els informes estan integrats en aplicacions (com passa als ERP o CRM), encara que també hi ha eines orientades específicament a la consulta d'informes, com per exemple, PowerBI de Microsoft.

!!! example "Exemple d'informe"
    El fitxer ["Informe1.html"](../exemples/informe1.html) és un exemple d'informe creat amb la llibreria que utilitzarem durant la unitat.

### Tipus dinformes

Segons la funcionalitat que ofereixen a l'usuari de l'informe, podem distingir els tipus següents:

- **Informes predefinits**: són informes amb una estructura prefixada pel dissenyador de l'informe, que l'usuari no pot modificar. Moltes vegades, estan orientats a la seva impressió o enviament per correu electrònic, i poden constar de diverses pàgines.

!!! example "Exemple"
    En una empresa amb activitat comercial, un exemple d'informe predefinit podria ser el que inclou les vendes del darrer mes per a cadascun dels agents comercials de l'empresa.

- **Informes configurables**: aquest tipus d'informes permet a l'usuari configurar certs paràmetres de l'informe per adaptar la informació a les seues necessitats. Tot i que l'estructura bàsica de l'informe també l'estableix el dissenyador, l'usuari pot ajustar certs aspectes.

!!! example "Exemple"
    Seguint amb l'exemple anterior, un informe configurable podria permetre a l'usuari decidir el període de temps per al qual vol obtenir les vendes, en comptes de limitar-se a les del darrer mes.

- **Informes personalitzats**: en aquest tipus d'informes és l'usuari qui decideix quina informació voleu veure i de quina manera organitzar-la. Per fer-ho, es fa servir algun tipus d'aplicació de disseny d'informes orientada a usuaris finals.

!!! example "Exemple"
    Un informe de vendes personalitzat deixaria a l'usuari seleccionar tant el període de temps com el comercial per al qual vol veure la informació, podent a més decidir quina mètrica us interessa (nombre de vendes, import total, mitjana de l'import,...) i si vol la informació en forma de taula o gràfic.

- **Quadres de comandament**: es tracta d'un tipus especial d'informe on es representen de manera visual mètriques i indicadors rellevants per a la presa de decisions.

!!! example "Exemple"
    Un quadre de comandament per a l'empresa del nostre exemple podria incloure el total de vendes acumulades a l'any, la comparació d'aquesta dada amb l'any anterior i un gràfic de l'evolució de les vendes en els darrers 6 mesos.

### Orígens de dades

Un dels aspectes importants quan ens plantegem el disseny d'un informe és l'origen d'on provenen les dades. La majoria de les eines destinades a la creació d'informes permeten la utilització de diferents tipus d'orígens de dades, com ara:

- **Fitxers de dades**: poden estar en diversos formats, sent els més habituals CSV, XML, JSON o en el format de les aplicacions de full de càlcul més utilitzades.
- **Bases de dades**: un dels orígens més habituals per als informes són les bases de dades de l'organització, predominant les bases de dades relacionals com ara Oracle, SQL Server o MySQL (encara que també es poden utilitzar bases de dades NoSQL com MongoDB).
- **Magatzems de dades (data warehouse)** : es tracta de repositoris de dades organitzades orientades a l'anàlisi d'informació, que solen alimentar-se de diverses fonts de dades de l'organització.
- **Dades massives (Big Data)**: moltes de les eines de creació d'informes actuals permeten obtenir dades des d'un origen big data, com ara Apache Hadoop.

!!! note "Dades al núvol"
    Tots aquests orígens de dades poden estar implementats a les plataformes de núvol públic actuals (com Amazon AWS, Microsoft Azure o Google Cloud), que ofereixen multitud de serveis orientats a l'emmagatzematge de dades.

### Eines per a l'elaboració d'informes

Quan ens plantegem l'elecció de l'eina o la tecnologia per al desenvolupament d'informes, tenim diferents opcions:

- **Llibreria d'informes**: una primera opció és utilitzar una llibreria per al nostre llenguatge de programació que ens permeta generar informes directament des del nostre codi. Aquesta és l'alternativa que farem servir en aquesta unitat mitjançant la llibreria `DataPane` de Python.
- **Eina visual de disseny d'informes**: també hi ha l'opció de crear els informes amb una eina visual. Algunes estan orientades a desenvolupadors (com ara SAP Crystal Reports o TIBCO JasperReports), mentre que d'altres també permeten als usuaris allunyats de l'àmbit tecnològic personalitzar els seus propis informes (com Microsoft PowerBI o MicroStrategy).

!!! note "Informes al núvol"
    Algunes plataformes de núvol públic també ofereixen serveis relacionats amb l'anàlisi de dades i la intel·ligència de negocis. És el cas d'Amazon QuickSight a AWS i Looker a Google Cloud.