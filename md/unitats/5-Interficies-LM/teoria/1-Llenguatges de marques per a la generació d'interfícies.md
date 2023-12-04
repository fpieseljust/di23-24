# 1. Llenguatges de marques per a la generació d'interfícies d'usuari

La majoria de les tecnologies d'interfície d'usuari actuals ofereixen la possibilitat d'utilitzar un llenguatge de marques per a la generació de la interfície d'una aplicació, com a alternativa a la creació d'interfícies per mitjà de codi. Quasi tots aquests llenguatges es basen en XML, utilitzant la sintaxi d'elements i atributs per definir l'estructura i els components de la interfície.  

## 1.1. Avantatges dels llenguatges de marques per a la generació d'interfícies

La utilització d'aquest tipus de llenguatges ofereix els avantatges següents sobre la creació utilitzant un llenguatge de programació:

- Millora la separació de responsabilitats en l'aplicació, diferenciant clarament la interfície d'usuari de la resta de capes.
- Són llenguatges fàcilment entendibles, tant per les persones com per les màquines.
- La seva estructura jeràrquica en forma d'arbre és semblant a l'estructura visual establerta entre els components de la interfície.
- Permeten reutilitzar el mateix disseny d'interfície a diferents plataformes o amb diferents llenguatges de programació.

## 1.2. Llenguatges de marques més utilitzats per a la generació d'interfícies

La taula següent recull alguns dels llenguatges de marques més populars per a la creació d'interfícies gràfiques d'usuari:

| Llenguatge  | Descripció                                                                                                                                                       |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Qt UI       | Llenguatge associat al framework de desenvolupament d'interfícies Qt. És el que veurem al llarg de la unitat.                                                    |
| FXML        | Desenvolupat per Oracle per a la definició de la interfície d'usuari a les aplicacions JavaFX.                                                                   |
| XAML        | Introduït amb la tecnologia WPF, continua sent el llenguatge utilitzat per la majoria de tecnologies d'interfície d'usuari de Microsoft (com UWP, WinUI o MAUI). |
| Gtk UI      | Format utilitzat pel toolkit GTK, vinculat al projecte de programari lliure GNOME.                                                                               |
| Android XML | Llenguatge utilitzat en el desenvolupament de la interfície dusuari de les aplicacions mòbils Android.                                                           |
| Storyboards | Format desenvolupat per Apple per a la interfície dusuari de les aplicacions mòbils iOS.                                                                         |

!!!example "Exemples"
    === "Qt UI"
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <ui version="4.0">
            <class>MainWindow</class>
            <widget class="QMainWindow" name="MainWindow">
                <property name="geometry">
                    <rect>
                        <x>0</x>
                        <y>0</y>
                        <width>435</width>
                        <height>267</height>
                    </rect>
                </property>
                <property name="windowTitle">
                    <string>MainWindow</string>
                </property>
                <widget class="QWidget" name="centralwidget">
                    <widget class="QLabel" name="label">
                        <property name="geometry">
                        <rect>
                            <x>0</x>
                            <y>0</y>
                            <width>73</width>
                            <height>16</height>
                        </rect>
                        </property>
                        <property name="text">
                            <string>Hola mundo</string>
                        </property>
                    </widget>
                </widget>
            </widget>
            <resources/>
            <connections/>
        </ui>
        ```
    === "FXML"
        ```xml        
        <?xml version="1.0" encoding="UTF-8"?>
        <?import javafx.scene.layout.VBox?>
        <?import javafx.scene.control.Label?>
        <VBox>
            <children>
                <Label text="Hola mundo"/>
            </children>
        </VBox>
        ```

    === "Gtk UI"
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <interface>
        <requires lib="gtk+" version="3.20"/>
            <object class="GtkApplicationWindow" id="window">
                <property name="can_focus">False</property>
                    <child>
                        <placeholder/>
                    </child>
                <child>
                <object class="GtkLabel">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label" translatable="yes">
                        Hola mundo
                    </property>
                    <property name="use_markup">True</property>
                </object>
                </child>
            </object>
        </interface>
        ```

    === "XAML"
        ```xml
        <Window x:Class="HolaMundo.MainWindow" xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" Title="MainWindow">
            <Grid>
                <TextBlock>Hola mundo</TextBlock>
            </Grid>
        </Window>
        ```

!!!important "IMPORTANT"
    Tot i que la major part de tecnologies relacionades amb la interfície d'usuari incorporen llenguatges de marques per a la definició d'interfícies, no sempre és així. En el cas de Flutter, el framework multiplataforma de Google, la interfície només es pot crear mitjançant el llenguatge de programació declarativa Dart.