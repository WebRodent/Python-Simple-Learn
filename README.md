# Velkommen til Python Dev Container!

Dette oppsettet er designet for å hjelpe deg med å komme i gang med Python-programmering ved å bruke Visual Studio Code Dev Containers. Her er noen raske tips og triks for å hjelpe deg med å få mest mulig ut av dette oppsettet.

## Oppsett

1. **Forutsetninger**: Sørg for at du har Visual Studio Code installert, samt Docker på datamaskinen din. Installer også extension "ms-vscode-remote.remote-containers"(i extension tab i editoren)

2. **Klon prosjektet**: Klon dette prosjektet til datamaskinen din ved å kjøre følgende kommando i terminalen:
_____________

```bash
git clone git@github.com:WebRodent/Python-Simple-Learn.git
```
3. **Åpne i VS Code**: Åpne prosjektmappen i Visual Studio Code ved å bruke kommandoen:
_________________
```bash
cd Python-Simple-Learn.git
code .
```
4. **Start Dev Container**: Når mappen er åpnet, vil Visual Studio Code oppdage Dev Container-konfigurasjonsfilen (`.devcontainer/devcontainer.json`) og tilby å bygge og starte Dev Containeren. Godta dette for å sette opp utviklingsmiljøet.

## Bruk av Python

1. **Interaktiv Python-konsoll**: Åpne en terminal i Visual Studio Code (trykk `Ctrl` + ``) og skriv `python` for å starte en interaktiv Python-konsoll.

2. **Kjør Python-filer**: For å kjøre en Python-fil, åpne filen og bruk kommandoen:
___________
```bash
python test-api-get.py
```

3. **Pakkehåndtering med pip**: Installer eksterne biblioteker ved hjelp av pip. For eksempel:
____________
```bash
pip install requests
```
4. **Feilsøking og Debugging**: Sett brytpunkter i koden din ved å klikke i margen. Bruk "Run and Debug" i VS Code for å starte feilsøkingsmodus.

## Nyttige Ressurser

- [Python-dokumentasjon](https://docs.python.org/3/): Offisiell dokumentasjon for Python-programmeringsspråket.

- [Visual Studio Code Dokumentasjon](https://code.visualstudio.com/docs): Ressurser for å lære mer om Visual Studio Code og dens funksjoner.

- [Python Programmering på W3Schools](https://www.w3schools.com/python/): En nyttig nettressurs for nybegynnere som ønsker å lære Python.

- [Stack Overflow](https://stackoverflow.com/): Et nettsted hvor du kan søke etter svar på programmeringsspørsmål og få hjelp fra samfunnet.

Lykke til med programmeringen din! Ikke nøl med å nå ut hvis du har spørsmål eller trenger hjelp.
