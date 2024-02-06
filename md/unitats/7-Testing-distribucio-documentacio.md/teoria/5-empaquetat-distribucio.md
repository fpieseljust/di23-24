<div>

[]{.c20}

</div>

5.  # [ Empaquetament i distribució d´aplicacions.]{.c19} {#h.5cmcau681fca style="display:inline"}

[]{.c5}

[L\'empaquetat ens serveix per ajuntar totes les parts d\'un programari
i tractar-les com a tot. Així doncs, també permet que sigui distribuït
de forma còmoda com una única entitat i permeti la instal·lació o
execució de les aplicacions en ordinadors dels usuaris finals.]{.c5}

Els paquets contenen tots els fitxers necessaris per a la instal·lació o
execució del codi, fitxers de dades, fitxers executables binaris, etc...
A més també contenen informació com el nom de l\'aplicació, la
descripció, els autors, les versions i els requisits. Aquesta informació
es diu en moltes ocasions el[manifest]{.c0} i és de gran ajuda als
desenvolupadors i els administradors de sistemes.[ ]{.c5}

[Hi ha diferents empaquetats segons el sistema operatiu que s\'estigui
utilitzant.]{.c5}

[]{.c5}

1.  ## [Empaquetat de programari a Windows]{.c12} {#h.cufw7ku4r5l style="display:inline"}

Per al sistema operatiu Windows, l\'estàndards de facto per a
l\'empaquetat i la distribució de paquets és el[format
.msi]{.c7} (arxius Windows Installer, anteriorment i d\'aquí el nom,
Microsoft Installers).[Windows Installer]{.c0}[, és un servei que ve
preinstal·lat en totes les versions de Windows com una API per crear,
mantenir, reparar i desinstal·lar programari. Aquest tipus de fitxers
són una mena de base de dades que contenen tota la informació necessària
per dur a terme tot el procés d\'instal·lació mitjançant una interfície
d\'instal·lació. No es tracta només de posar certs fitxers en una ruta
concreta, sinó a més registrar components, generar una seqüència de
desinstal·lació, editar les entrades al registre de Windows, ...]{.c5}

A més, en infinitat d\'ocasions trobem que per instal·lar un programari
necessitem executar un[fitxer .exe]{.c7}. Aquest tipus de fitxers
són[fitxers d\'instal·lació executables]{.c7}. Hi ha diversos tipus
de[ex]{.c0}[:]{.c5}

-   Instal·lació de llançadors o[bootstrappers]{.c0}[ que en realitat
    són arxius comprimits amb un arxiu Windows Installer al seu interior
    que sexecuta després del seu llançament.]{.c5}
-   [Exe personalitzats no-MSI, que són fitxers executables que
    s\'encarreguen de la instal·lació sense utilitzar l\'API, és a dir,
    utilitzen el seu propi sistema d\'instal·lació. Aquests, es fan
    servir una sola vegada per instal·lar un altre programa.]{.c5}
-   [Fitxers .exe portables o PE (Portable Executable), són fitxers .exe
    que contenen tot el necessari per a l\'execució del programa, així
    que no cal cap tipus d\'instal·lació. Només cal executar aquests
    fitxers perquè l\'aplicació funcioni correctament.]{.c5}

[]{.c5}

[Hi ha alguns avantatges i desavantatges dutilitzar cadascun daquests
tipus. El principal desavantatge d\'utilitzar un MSI per a una
instal·lació és que no permet el seu ús de forma paral·lela, així que
només podrem realitzar una instal·lació/desinstal·lació en un moment
donat, i haurem d\'esperar que acabi per instal·lar/desinstal·lar el
programa següent. En canvi, els principals avantatges dels MSI són que
es crea un punt de restauració automàtic en instal·lar l\'aplicació,
permetent la tornada a l\'estat anterior de la instal·lació si així ho
desitgem. A més, permeten les instal·lacions desateses, sense que la
intervenció de l\'usuari sigui necessària. Aquesta característica fa que
siguin molt populars a entorns empresarials.]{.c5}

[Per crear paquets d\'instal·lació, hi ha multitud de programes, entre
els quals podem destacar WiX Toolset, Visual Studio Installer Project,
Orca, IExpress, InstallShield o InnoSetup.]{.c5}

[]{.c5}

2.  ## [Empaquetat "tradicional" de programari a Linux]{.c12} {#h.xniig4d5o7z0 style="display:inline"}

[Els paquets a Linux es creen per treballar amb una distribució en
particular, que a més utilitzarà el vostre propi administrador de
paquets. Aquest programa és l\'utilitzat pels administradors dels
sistemes operatius per instal·lar programari. Tots funcionen de forma
similar però tenen peculiaritats davant dels altres. Les distribucions
principals linux han creat els seus propis administradors de paquets que
utilitzen formats concrets.]{.c5}

[Hi ha aplicacions, per exemple l\'aplicació Alien de Debian, que ens
permeten canviar entre formats de paquets.]{.c5}

[Veurem a continuació els principals formats de paquets utilitzats a
Linux:]{.c5}

-   [Paquetes Debian (.deb)]{.c7}: originalment desenvolupat per a la
    distribució de paquets[Debian]{.c7}. És l\'estàndard de facto tant
    per a aquesta distribució com per a les seves distribucions
    derivades, com[Ubuntu]{.c7}[. Cada paquet d\'aquest tipus conté dos
    fitxers, un amb informació de control i l\'altre amb les dades de la
    instal·lació. Els fitxers estan en format .tar que veurem a
    continuació.]{.c5}

DPKG s\'encarrega de la gestió d\'aquests paquets, empaquetat,
desempaquetat, instal·lació, desinstal·lació, ... Hi ha diverses
utilitats en línia d\'ordres que fan ús de dpkg per facilitar tot el
procés de gestió de paquets, com ara[APT]{.c7} (Eina de paquets
avançats),[APT-GET]{.c7}O[Aptitud]{.c7}. També n\'hi ha alguns amb
interfície gràfica com el[Sinàptic]{.c7} o el[Descobreix]{.c7}[.]{.c5}

-   [Paquetes rpm (RPM Package Manager):]{.c7} Originalment Red Hat
    Package Manager i desenvolupat per a la distribució[Red Hat
    Linux]{.c7}, avui dia s\'utilitza en tots els seus derivats,
    com[OpenSUSE]{.c7} O[Fedora]{.c7}[. És el format adoptat per a la
    LSB (Linux Standard Base), un projecte de diverses distribucions
    Linux per normalitzar l\'estructura interna dels sistemes operatius
    derivats de Linux.]{.c5}

[Normalment contenen executables en format binari (.rpm), però també es
poden utilitzar per distribuir els fitxers de codi font sense compilar
(src.rpm).]{.c5}

-   [Fitxers .tar (Tape Archive):]{.c7}[Arxius dissenyats originalment
    per Bell Laboratories el 1979 per al sistema operatiu UNIX (sobre el
    qual es va basar posteriorment Linux). Aquest format estava pensat
    per arxivar, transferir i fer còpies de seguretat i recuperació
    sobre cintes magnètiques. Permetia als administradors replicar una
    estructura de fitxers i carpetes en diferents màquines o en la
    mateixa.]{.c5}

[Als arxius creats amb TAR se\'ls denomina comunament tarballs i segueix
sent un format utilitzat tant a Linux com a Windows. Les implementacions
més recents de tar permeten crear fitxers tar comprimits, per estalviar
espai i ample de banda en transmissions. Es comprimeixen i
descomprimeixen utilitzant GZip o directament amb les opcions z o x de
tar, donant lloc a fitxers .tar.gz, que solen contenir els tipus de
lletra perquè l\'usuari es construeixi el paquet o aplicació.]{.c5}

3.  ## [Noves formes de distribució]{.c12} {#h.z86lnl61yndz style="display:inline"}

[]{.c5}

Des del punt de vista de l\'experiència de l\'usuari, hi ha grans
diferències quant a la facilitat d\'obtenció i d\'instal·lació
d\'aplicacions entre les plataformes d\'escriptori i mòbils. Obtenir
aplicacions per a dispositius mòbils és molt més senzill que fer-ho amb
ordinadors gràcies a les diferents[botigues]{.c0}, com el[Play
Store]{.c0} d\'Android o la[Tenda d\'aplicacions]{.c0}[ d\'Apple.]{.c5}

[]{.c5}

En un dispositiu mòbil n\'hi hauria prou amb tenir connexió a internet i
utilitzar l\'aplicació de gestió d\'aplicacions, mentre que en un
ordinador es necessita (tret que sigui un usuari[avançat]{.c0}[i es
controli la CLI) obrir un navegador, obrir un motor de cerca, cerca el
nom de l\'app, parar atenció a què estàs baixant i d\'on ho estàs
baixant, verificar que no ha estat modificat, etc.]{.c5}

[]{.c5}

[Altres desavantatges que existeixen per al desenvolupador són tot allò
relacionat amb la gestió de la distribució, la gestió de llicències, la
seguretat, les actualitzacions automàtiques en cas de voler assegurar-se
que l\'usuari utilitza l\'última versió de l\'aplicació, l\'obtenció de
dades , ja siguin informes derror o dades per a la seva explotació. Tot
això ho ha de dur a terme lequip de desenvolupament.]{.c5}

[]{.c5}

Per solucionar aquests problemes, els sistemes operatius moderns, han
desenvolupat solucions tipus[botiga]{.c0}[ o similar per als
usuaris.]{.c5}

[]{.c5}

1.  ### [Microsoft Store]{.c1} {#h.e5pupwrcjspj style="display:inline"}

[]{.c5}

[![](images/image2.png){style="width: 240.00px; height: 240.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 240.00px; height: 240.00px;"}

[]{.c5}

Va aparèixer amb Windows XP, on el servei era conegut com a Windows
Catalog. Posteriorment a les versions de Windows 8 se\'l va rebatejar
com a Windows Store per passar a ser Microsoft Store a les versions de
Windows 10 i 11. La microsoft Store aglutina les anteriors Windows
Marketplace, Windows Phone Store, Xbox Video i Xbox Music, sent possible
ara obtenir[a més d\'aplicacions, vídeos, àudios i llibres electrònics.
Les aplicacions que es vulguin distribuir a través d\'aquesta botiga han
d\'estar certificades quant a compatibilitat i contingut.]{.c5}

[]{.c5}

[Per als usuaris de Windows 11, teniu disponibles aplicacions Android,
que es podran instal·lar des de l\'Amazon Appstore.]{.c5}

[]{.c5}

2.  ### [ Mac App Store]{.c1} {#h.mdw9fppnku33 style="display:inline"}

[![](images/image3.png){style="width: 250.00px; height: 250.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 250.00px; height: 250.00px;"}

[]{.c5}

[La Mac App Store és la plataforma de distribució d\'aplicacions
d\'Apple per al sistema operatiu macOS llançada el gener del 2011. Es
tracta de l\'adaptació de l\'App Store per a desenvolupada per a iPhone,
i permet comprar, descarregar, instal·lar, reinstal·lar aplicacions
comprades anteriorment i actualitzar-les. Abans d\'estar disponibles,
heu de passar un procés d\'aprovació. Una cosa a destacar és que han de
complir les especificacions per a interfícies dApple i altres
restriccions imposades per la mateixa Apple amb fins comercials.]{.c5}

[]{.c5}

3.  ### [Noves formes de distribució a Linux]{.c1} {#h.u9w0mcx9o0a3 style="display:inline"}

[Per resoldre el problema de la fragmentació a Linux, és a dir,
diferents configuracions del sistema operatiu quant a escriptori,
organització de directoris, empaquetat de distribucions (.deb, .rpm,
...), apareixen diferents iniciatives que intenten resoldre\'l. Entre
elles destaquen Appimage, Snap i Flatpack.]{.c5}

[]{.c5}

4.  #### [Imatge de l\'aplicació]{.c11} {#h.v4hocmttjx4z style="display:inline"}

[![](images/image5.png){style="width: 250.00px; height: 250.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 250.00px; height: 250.00px;"}

[La idea d\'Appimage és distribuir aplicacions portables, és a dir,
aplicacions que no requereixen ser instal·lades, sinó simplement
executades i sense necessitat de ser administrador sempre que no sigui
necessari per funcionar.]{.c5}

[No es disposa d\'una botiga des d\'on descarregar i instal·lar les
aplicacions, però hi ha un repositori (AppImageHub) on trobar-ne
infinitat, encara que n\'hi pot haver algunes no publicades al lloc. Un
cop localitzada l\'aplicació, es baixa, se li donen permisos d\'execució
i s\'executa.]{.c5}

La imatge de l\'aplicació ja inclou qualsevol dependència que es
necessiti però no quedarà integrada a l\'escriptori. Si es vol integrar,
podem fer ús del dimoni[imatge de l\'aplicació]{.c0} perquè s\'integri a
l\'escriptori, afegint-les als menús, registrant les icones, etc. Es
poden mantenir al dia les actualitzacions amb una altra eina
anomenada[AppImageUpdate]{.c0}[.]{.c5}

[]{.c5}

[]{.c5}

5.  #### [Snap]{.c11} {#h.uf0kudyrn1az style="display:inline"}

[![](images/image1.png){style="width: 275.00px; height: 183.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 275.00px; height: 183.00px;"}

[]{.c5}

Aquest sistema de gestió de paquets universals va ser originalment creat
per Canonical, l\'empresa darrere del desenvolupament d\'Ubuntu. Els
seus paquets o snaps són gestionats per una eina anomenada snapd,
disponible en moltes de les distribucions actuals com Ubuntu, Arch
Linux, CentOS, Debian, Fedora, Manjar Linux, Linux Mint, OpenSUSE, etc.
Per tant, qualsevol distribució que disposi de l\'eina snapd podrà
utilitzar[encaix]{.c0}[.]{.c5}

El sistema està preparat per funcionar amb dispositius IoT, al núvol i
en entorns descriptori. Els seus paquets no depenen de
cap[botiga]{.c0}[, sinó que es poden obtenir de diferents fonts, però,
la botiga d\'aplicacions d\'Ubuntu s\'usa com a repositori predeterminat
en aquesta distribució, encara que se\'n poden utilitzar
d\'altres.]{.c5}

[Per empaquetar un snap s\'utilitza l\'eina snapcraft, que permet
empaquetar aplicacions cli, gui i serveis. El fitxer resultant té
extensió .snap.]{.c5}

[]{.c5}

6.  #### [Paquet pla]{.c11} {#h.cq4gpitjswo6 style="display:inline"}

[![](images/image4.png){style="width: 256.00px; height: 256.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 256.00px; height: 256.00px;"}

Aquesta eina permet desplegar, gestionar paquets universals i
virtualitzar aplicacions en entorns d\'escriptori. Proporciona un entorn
d\'aïllament de procés, de manera que l\'aplicació s\'executa de manera
independent a la resta del sistema, aconseguint que l\'execució no
depengui de la distribució o la configuració de l\'entorn sobre el qual
s\'executa. Les aplicacions necessiten permisos dusuari per executar-se.
Hi ha moltes aplicacions tant en versió oficial com desenvolupades per
tercers. No depenen d\'una botiga sinó que es distribueixen normalment a
través del vostre repositori, disponible als links de la unitat.
