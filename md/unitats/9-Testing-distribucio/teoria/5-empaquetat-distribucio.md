# Empaquetament i distribució d´aplicacions.


L'empaquetat ens serveix per ajuntar totes les parts d'un programari
i tractar-les com a tot. Així doncs, també permet que sigui distribuït
de forma còmoda com una única entitat i permeti la instal·lació o
execució de les aplicacions en ordinadors dels usuaris finals.

Els paquets contenen tots els fitxers necessaris per a la instal·lació o
execució del codi, fitxers de dades, fitxers executables binaris, etc...
A més també contenen informació com el nom de l'aplicació, la
descripció, els autors, les versions i els requisits. Aquesta informació
es diu en moltes ocasions elmanifest i és de gran ajuda als
desenvolupadors i els administradors de sistemes. 

Hi ha diferents empaquetats segons el sistema operatiu que s'estigui
utilitzant.



## Empaquetat de programari a Windows

Per al sistema operatiu Windows, l'estàndards de facto per a
l'empaquetat i la distribució de paquets és elformat
.msi' (arxius Windows Installer, anteriorment i d'aquí el nom,
Microsoft Installers).Windows Installer', és un servei que ve
preinstal·lat en totes les versions de Windows com una API per crear,
mantenir, reparar i desinstal·lar programari. Aquest tipus de fitxers
són una mena de base de dades que contenen tota la informació necessària
per dur a terme tot el procés d'instal·lació mitjançant una interfície
d'instal·lació. No es tracta només de posar certs fitxers en una ruta
concreta, sinó a més registrar components, generar una seqüència de
desinstal·lació, editar les entrades al registre de Windows, ...

A més, en infinitat d'ocasions trobem que per instal·lar un programari
necessitem executar unfitxer .exe'. Aquest tipus de fitxers
sónfitxers d'instal·lació executables'. Hi ha diversos tipus
deex':

-   Instal·lació de llançadors obootstrappers' que en realitat
    són arxius comprimits amb un arxiu Windows Installer al seu interior
    que sexecuta després del seu llançament.
-   Exe personalitzats no-MSI, que són fitxers executables que
    s'encarreguen de la instal·lació sense utilitzar l'API, és a dir,
    utilitzen el seu propi sistema d'instal·lació. Aquests, es fan
    servir una sola vegada per instal·lar un altre programa.
-   Fitxers .exe portables o PE (Portable Executable), són fitxers .exe
    que contenen tot el necessari per a l'execució del programa, així
    que no cal cap tipus d'instal·lació. Només cal executar aquests
    fitxers perquè l'aplicació funcioni correctament.



Hi ha alguns avantatges i desavantatges dutilitzar cadascun daquests
tipus. El principal desavantatge d'utilitzar un MSI per a una
instal·lació és que no permet el seu ús de forma paral·lela, així que
només podrem realitzar una instal·lació/desinstal·lació en un moment
donat, i haurem d'esperar que acabi per instal·lar/desinstal·lar el
programa següent. En canvi, els principals avantatges dels MSI són que
es crea un punt de restauració automàtic en instal·lar l'aplicació,
permetent la tornada a l'estat anterior de la instal·lació si així ho
desitgem. A més, permeten les instal·lacions desateses, sense que la
intervenció de l'usuari sigui necessària. Aquesta característica fa que
siguin molt populars a entorns empresarials.

Per crear paquets d'instal·lació, hi ha multitud de programes, entre
els quals podem destacar WiX Toolset, Visual Studio Installer Project,
Orca, IExpress, InstallShield o InnoSetup.



## Empaquetat "tradicional" de programari a Linux

Els paquets a Linux es creen per treballar amb una distribució en
particular, que a més utilitzarà el vostre propi administrador de
paquets. Aquest programa és l'utilitzat pels administradors dels
sistemes operatius per instal·lar programari. Tots funcionen de forma
similar però tenen peculiaritats davant dels altres. Les distribucions
principals linux han creat els seus propis administradors de paquets que
utilitzen formats concrets.

Hi ha aplicacions, per exemple l'aplicació Alien de Debian, que ens
permeten canviar entre formats de paquets.

Veurem a continuació els principals formats de paquets utilitzats a
Linux:

-   Paquetes Debian (.deb)': originalment desenvolupat per a la
    distribució de paquetsDebian'. És l'estàndard de facto tant
    per a aquesta distribució com per a les seves distribucions
    derivades, comUbuntu'. Cada paquet d'aquest tipus conté dos
    fitxers, un amb informació de control i l'altre amb les dades de la
    instal·lació. Els fitxers estan en format .tar que veurem a
    continuació.

DPKG s'encarrega de la gestió d'aquests paquets, empaquetat,
desempaquetat, instal·lació, desinstal·lació, ... Hi ha diverses
utilitats en línia d'ordres que fan ús de dpkg per facilitar tot el
procés de gestió de paquets, com araAPT' (Eina de paquets
avançats),APT-GET'OAptitud'. També n'hi ha alguns amb
interfície gràfica com elSinàptic' o elDescobreix'.

-   Paquetes rpm (RPM Package Manager):' Originalment Red Hat
    Package Manager i desenvolupat per a la distribucióRed Hat
    Linux', avui dia s'utilitza en tots els seus derivats,
    comOpenSUSE' OFedora'. És el format adoptat per a la
    LSB (Linux Standard Base), un projecte de diverses distribucions
    Linux per normalitzar l'estructura interna dels sistemes operatius
    derivats de Linux.

Normalment contenen executables en format binari (.rpm), però també es
poden utilitzar per distribuir els fitxers de codi font sense compilar
(src.rpm).

-   Fitxers .tar (Tape Archive):'Arxius dissenyats originalment
    per Bell Laboratories el 1979 per al sistema operatiu UNIX (sobre el
    qual es va basar posteriorment Linux). Aquest format estava pensat
    per arxivar, transferir i fer còpies de seguretat i recuperació
    sobre cintes magnètiques. Permetia als administradors replicar una
    estructura de fitxers i carpetes en diferents màquines o en la
    mateixa.

Als arxius creats amb TAR se'ls denomina comunament tarballs i segueix
sent un format utilitzat tant a Linux com a Windows. Les implementacions
més recents de tar permeten crear fitxers tar comprimits, per estalviar
espai i ample de banda en transmissions. Es comprimeixen i
descomprimeixen utilitzant GZip o directament amb les opcions z o x de
tar, donant lloc a fitxers .tar.gz, que solen contenir els tipus de
lletra perquè l'usuari es construeixi el paquet o aplicació.

## Noves formes de distribució
Des del punt de vista de l'experiència de l'usuari, hi ha grans
diferències quant a la facilitat d'obtenció i d'instal·lació
d'aplicacions entre les plataformes d'escriptori i mòbils. Obtenir
aplicacions per a dispositius mòbils és molt més senzill que fer-ho amb
ordinadors gràcies a les diferentsbotigues', com elPlay
Store' d'Android o laTenda d'aplicacions' d'Apple.

En un dispositiu mòbil n'hi hauria prou amb tenir connexió a internet i
utilitzar l'aplicació de gestió d'aplicacions, mentre que en un
ordinador es necessita (tret que sigui un usuariavançat'i es
controli la CLI) obrir un navegador, obrir un motor de cerca, cerca el
nom de l'app, parar atenció a què estàs baixant i d'on ho estàs
baixant, verificar que no ha estat modificat, etc.

Altres desavantatges que existeixen per al desenvolupador són tot allò
relacionat amb la gestió de la distribució, la gestió de llicències, la
seguretat, les actualitzacions automàtiques en cas de voler assegurar-se
que l'usuari utilitza l'última versió de l'aplicació, l'obtenció de
dades , ja siguin informes derror o dades per a la seva explotació. Tot
això ho ha de dur a terme lequip de desenvolupament.

Per solucionar aquests problemes, els sistemes operatius moderns, han
desenvolupat solucions tipusbotiga' o similar per als
usuaris.



### Microsoft Store



![](images/image2.png)



Va aparèixer amb Windows XP, on el servei era conegut com a Windows
Catalog. Posteriorment a les versions de Windows 8 se'l va rebatejar
com a Windows Store per passar a ser Microsoft Store a les versions de
Windows 10 i 11. La microsoft Store aglutina les anteriors Windows
Marketplace, Windows Phone Store, Xbox Video i Xbox Music, sent possible
ara obtenira més d'aplicacions, vídeos, àudios i llibres electrònics.
Les aplicacions que es vulguin distribuir a través d'aquesta botiga han
d'estar certificades quant a compatibilitat i contingut.



Per als usuaris de Windows 11, teniu disponibles aplicacions Android,
que es podran instal·lar des de l'Amazon Appstore.



###  Mac App Store

![](images/image3.png)



La Mac App Store és la plataforma de distribució d'aplicacions
d'Apple per al sistema operatiu macOS llançada el gener del 2011. Es
tracta de l'adaptació de l'App Store per a desenvolupada per a iPhone,
i permet comprar, descarregar, instal·lar, reinstal·lar aplicacions
comprades anteriorment i actualitzar-les. Abans d'estar disponibles,
heu de passar un procés d'aprovació. Una cosa a destacar és que han de
complir les especificacions per a interfícies dApple i altres
restriccions imposades per la mateixa Apple amb fins comercials.



### Noves formes de distribució a Linux

Per resoldre el problema de la fragmentació a Linux, és a dir,
diferents configuracions del sistema operatiu quant a escriptori,
organització de directoris, empaquetat de distribucions (.deb, .rpm...), apareixen diferents iniciatives que intenten resoldre'l. Entre
elles destaquen Appimage, Snap i Flatpack.



#### Imatge de l'aplicació

![](images/image5.png)

La idea d'Appimage és distribuir aplicacions portables, és a dir,
aplicacions que no requereixen ser instal·lades, sinó simplement
executades i sense necessitat de ser administrador sempre que no sigui
necessari per funcionar.

No es disposa d'una botiga des d'on descarregar i instal·lar les
aplicacions, però hi ha un repositori (AppImageHub) on trobar-ne
infinitat, encara que n'hi pot haver algunes no publicades al lloc. Un
cop localitzada l'aplicació, es baixa, se li donen permisos d'execució
i s'executa.

La imatge de l'aplicació ja inclou qualsevol dependència que es
necessiti però no quedarà integrada a l'escriptori. Si es vol integrar,
podem fer ús del dimoniimatge de l'aplicació' perquè s'integri a
l'escriptori, afegint-les als menús, registrant les icones, etc. Es
poden mantenir al dia les actualitzacions amb una altra eina
anomenadaAppImageUpdate'.





#### Snap

![](images/image1.png)



Aquest sistema de gestió de paquets universals va ser originalment creat
per Canonical, l'empresa darrere del desenvolupament d'Ubuntu. Els
seus paquets o snaps són gestionats per una eina anomenada snapd,
disponible en moltes de les distribucions actuals com Ubuntu, Arch
Linux, CentOS, Debian, Fedora, Manjar Linux, Linux Mint, OpenSUSE, etc.
Per tant, qualsevol distribució que disposi de l'eina snapd podrà
utilitzarencaix'.

El sistema està preparat per funcionar amb dispositius IoT, al núvol i
en entorns descriptori. Els seus paquets no depenen de
capbotiga', sinó que es poden obtenir de diferents fonts, però,
la botiga d'aplicacions d'Ubuntu s'usa com a repositori predeterminat
en aquesta distribució, encara que se'n poden utilitzar
d'altres.

Per empaquetar un snap s'utilitza l'eina snapcraft, que permet
empaquetar aplicacions cli, gui i serveis. El fitxer resultant té
extensió .snap.



#### Paquet pla

![](images/image4.png)

Aquesta eina permet desplegar, gestionar paquets universals i
virtualitzar aplicacions en entorns d'escriptori. Proporciona un entorn
d'aïllament de procés, de manera que l'aplicació s'executa de manera
independent a la resta del sistema, aconseguint que l'execució no
depengui de la distribució o la configuració de l'entorn sobre el qual
s'executa. Les aplicacions necessiten permisos dusuari per executar-se.
Hi ha moltes aplicacions tant en versió oficial com desenvolupades per
tercers. No depenen d'una botiga sinó que es distribueixen normalment a
través del vostre repositori, disponible als links de la unitat.
