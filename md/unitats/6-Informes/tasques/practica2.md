## Orígens de dades per a l'informe

Com ja hem comentat, els informes elaborats amb la llibreria `DataPane` prenen com a origen de dades un `DataFrame` de la llibreria `pandas`. En tots els informes que hem elaborat durant aquesta unitat hem construït el `DataFrame` a partir dun fitxer de dades CSV. No obstant, és habitual en un entorn real que les dades de partida per a un informe estiguen, per exemple, allotjades en una base de dades o en un fitxer JSON retornat per un servei web.

En esta pràctica aprendrem com construir un`DataFrame` a partir de diferents fonts de dades, utilitzant les funcionalitats de la llibreria`pandas`.

Als enllaços de la unitat s'inclou un enllaç a la pàgina de documentació de`pandas` on es detallen totes les possibilitats d´entrada/sortida que permet la llibreria.

### Base de dades relacional

Una de les opcions dentrada de dades que permet`pandas` són les bases de dades relacionals. Per això,`pandas` disposa del mètode `read_sql()`, que rep com a paràmetre la consulta SQL a executar i la connexió sobre la qual realitzar la consulta.

```python
import pandas as pd
import sqlite3 as sql

connection = sql.connect('./database_file.db')
df = pd.read_sql("SELECT * FROM tabla", connection)
```

Com veiem a l'exemple, en primer lloc es crea la connexió a la base de dades, i un cop creada s'utilitza el mètode `read_sql()` per crear el`DataFrame`. El primer paràmetre daquest mètode és una consulta SQL, però també hi ha la possibilitat d'indicar únicament el nom d'una taula per recuperar la taula sencera.

Si volem fer servir una base de dades diferent (com MySQL, PostgreSQL, Oracle o SQL Server) canviarà la manera d'establir la connexió, però no el mètode d'execució de la consulta. Python inclou a la vostra llibreria estàndard el connector per a SQLite, però per a la resta de bases de dades s'hauria d'instal·lar el paquet corresponent.

### JSON

Una altra de les possibilitats que ofereix `pandas` com a origen de dades a l'hora de crear un `DataFrame` és un fitxer JSON. Per fer la lectura tenim el mètode `read_json()`, que en la seva forma més senzilla només rep com a paràmetre el JSON que cal llegir (pot ser un string o una referència a un fitxer json).

```python
json ='[{"a": 1, "b": 2},{"a": 3, "b": 4}]'
df = pd.read_json(json)
```

En aquest senzill exemple creem una cadena en format JSON, amb una llista de dos objectes json. A partir d'aquesta cadena, el mètode `read_json()` deserialitza el contingut en un `DataFrame`. Aquest mètode compta amb multitud d'opcions (descrites a la documentació) per tractar fitxers JSON amb estructures més complexes.

### HTML

Per acabar, veurem que `pandas` també és capaç d'analitzar el contingut HTML d'una pàgina web, per això utilitzarem el mètode `read_html()`. Aquest mètode rep com a paràmetre l'HTML a llegir (que pot ser una cadena, un fitxer local o una URL) i torna una llista de *DataFrames*, un per cadascuna de les taules HTML que trobeu al document. Utilitzant aquest mètode podem fer *web scraping*.

```python
dfs = pd.read_html(url)
```

En esta pràctica hauràs de dissenyar **tres informes**, cadascun a partir d'un origen de dades diferent:

1. La taula d'artistes (*artists*) de la base de dades Chinook, una base de dades de prova que conté les dades duna botiga de discos. Pots descarregar-la en aquest enllaç: [https://www.sqlitetutorial.net/sqlite-sample-database](https://www.sqlitetutorial.net/sqlite-sample-database)
2. El fitxer JSON [coldplay_albums.json](data/coldplay_albums.json), que conté un llistat dels àlbums publicats pel grup de música Coldplay.
3. La llista de població per països, obtinguda directament de la següent pàgina de Wikipedia: [https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population)

Els informes es mostraran en una aplicació Qt utilitzant una interfície de pestanyes (QTabWidget) dissenyada amb QtDesigner. A cada pestanya, s'haurà de mostrar l'informe directament a l'aplicació i incloure un botó per obrir-lo al navegador predeterminat del sistema.