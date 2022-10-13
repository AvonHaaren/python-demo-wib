# Python Demo-Projekt für WIB Workshop
27.10.2022, Andreas von Haaren


[macOS Installation](#macos)  
[macOS Deinstallation](#macos-1)  
[Windows Installation](#windows)  
[Windows Deinstallation](#windows-1)  


# Installationsanleitung

Viele (eigentlich alle) der folgenden Schritte müssen aus einem Terminal ausgeführt werden. Wenn Du vorher noch nie mit einem Terminal gearbeitet hast, keine Sorge, das kriegen wir hin!

Alles, was Du installierst, ist zusammen ca. 5GB groß. So viel Speicher wirst Du also mindestens brauchen.
Es gibt am Ende eine Anleitung zum Deinstallieren, wenn Du alles wieder loswerden willst, was Du für den Workshop installiert hast.


## macOS

*Du kannst ein Terminal öffnen, indem Du Cmd+Leertaste drückst, dann Terminal eingibst und Enter drückst. Das sieht dann ungefähr so aus:*
![Terminal](docs/terminal.png)

#### 1. Installation von Homebrew  
   Homebrew ist ein sogenannter Package Manager. Damit kann man viele Programme einfach vom Terminal aus installieren und muss sich nicht Gedanken darum machen, wo man bspw eine .dmg oder .pkg Datei herunterlädt, man muss sich nicht durch einen Installer kämpfen, und man muss keine Programme selbst in den Applications Ordner verschieben. Noch viel besser: Wenn man ein Programm wieder deinstallieren will, ist das in einem Befehl erledigt!  
   
   Um homebrew zu installieren, musst Du nur diesen Befehl kopieren und in das Terminal einfügen und dann mit Enter bestätigen.
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   ![Homebrew](docs/commandpaste.png)
   Um die Installation durchzuführen, musst Du Dein Benutzerpasswort eingeben und mit Enter bestätigen:
   ![Passwort](docs/sudoaccess.png)
   *Hinweis: wenn Du hier etwas eingibst, wird man das nicht sehen, es gibt keine **** oder ähnliches*  
   Jetzt noch einmal mit Enter bestätigen
   ![Bestätigung](docs/homebrewconfirm.png)
   Das Skript wird Dich gegebenenfalls ab und zu um Bestätigung bitten. Die Entwickler von Homebrew sind extrem gründlich, daher befolge bitte alle Anweisungen, die Dir gestellt werden.
   Wenn die Installation abgeschlossen ist, steht unten im Terminal wieder
   ```
   dein-benutzername@Dein-MBP ~ % 
   ```
   Jetzt kannst du das Terminal Fenster schließen und ein neues öffnen, damit die geänderten Einstellungen übernommen werden.
   Wenn alles geklappt hat, müsste der Command
   ```
   brew --version
   ```
   dir die installierte Version von Homebrew anzeigen.

#### 2. Installation von Python und Visual Studio Code
   Jetzt können wir Python und den Code Editor, den wir für den Workshop benutzen, herunterladen und installieren.
   Führe dazu den Befehl
   ```
   brew install python visual-studio-code
   ```
   aus.

#### 3. Die richtige Python Version nutzen

#### 4. Installation von Python Modulen
   Wir benötigen im Workshop einige sogenannte Packages, die uns als Programmierern Arbeit abnehmen. Du kannst die benötigten Pakete mit
   ```
   pip3 install lmfit numpy yfinance matplotlib pandas
   ```
   installieren.


## Windows
   Auf Windows ist es tatsächlich recht einfach, eine funktionierende Entwicklungsumgebung für Python zu installieren.


#### 1. Installation von Python
   [Dieser Link](https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe) lädt den Installer für Python 3.10.8 herunter. Führe den Installer einfach wie für jedes andere Programm aus, alle default Einstellungen können einfach übernommen werden. Du kannst die Installation überprüfen, indem Du Powershell/Windows Terminal öffnest (*Rechtsklick auf Startmenü, dann sollte eins der beiden auftauchen*) und dort den Befehl ```py``` eingibst und mit Enter bestätigst. Dann startet der sogenannte Python Interpreter. Wenn die angezeigte Version ```3.10.8``` ist, hat alles geklappt. Du kannst den Interpreter mit ```exit()``` + Enter verlassen und das Fenster schließen.

#### 2. Installation von Python Modulen
   Wir benötigen im Workshop einige sogenannte Packages, die uns als Programmierern Arbeit abnehmen. Du kannst die benötigten Pakete mit
   ```
   py -m pip install lmfit numpy yfinance matplotlib pandas
   ```
   installieren.

#### 3. Installation von Visual Studio Code
   Visual Studio Code (VSCode) ist der Codeeditor, den wir im Workshop benutzen.
   [Hier](https://code.visualstudio.com/download#) findest Du den Installer für VSCode.


---

# Deinstallation

## macOS

#### Python, VSCode und Homebrew
Die Deinstallation ist sehr einfach:
Führe einfach die folgenden Kommandos hintereinander aus:

```
brew uninstall python visual-studio-code
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```
Das zweite Skript deinstalliert homebrew. Wenn das Skript fertig ist, werden einige Ordner aufgelistet, die Du gegebenenfalls noch manuell löschen musst. Dazu kannst du beispielsweise in einem Finder Fenster Shift+Cmd+G drücken und dann den übergeordneten Ordner eingeben, um dann von dort alles weitere zu löschen.

Je nachdem, auf welcher Version von macOS Du bist, musst Du auch noch eine Einstellung für das Terminal ändern. Auf einem neuen MacBook mit Apple Silicon kannst Du dazu in einem Terminal
```
open .zprofile
```
eingeben.
Dann öffnet sich der default Text Editor von macOS, textedit:
![Textedit](docs/textedit.png)
Die Zeile mit "brew shellenv" musst Du löschen, dann speichern und das Fenster schließen.

#### XCode Command Line Tools
Die offizielle Dokumentation von Apple sagt, dass man einfach den Ordner löschen soll, wo diese installiert sind. Öffne dazu im Finder den Ordner "/Library/Developer" und lösche dort den Ordner "CommandLineTools". Gegebenenfalls musst Du dein Passwort eingeben.


#### Fertig 🎉



## Windows

#### VSCode
Deinstalliere VSCode mittels *Startmenü > Apps und Programme deinstallieren*.

#### Python
Führe den Installer erneut aus, aber wähle die Option *Installation ändern/Entfernen*

#### pip Cache
Die Installation der Packages hinterlässt ein paar Dateien. Tippe in einem Windows Explorer in der Pfadleiste ```%LOCALAPPDATA%``` ein und lösche den Ordner "pip"

#### Fertig 🎉