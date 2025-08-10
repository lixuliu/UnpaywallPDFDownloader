# UnpaywallPDFDownloader

Een Python-script dat het proces automatiseert van het downloaden van open-access onderzoeksartikelen in PDF-formaat met behulp van DOIs (Digital Object Identifiers) opgehaald uit een CSV-bestand. Het script gebruikt de Unpaywall API om de beschikbaarheid van open-access versies van de artikelen te controleren en deze te downloaden naar een opgegeven directory.

## Webapplicatie

**🌐 Probeer de online versie:** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

Voor een gebruiksvriendelijke webapplicatie die geen Python-installatie vereist, bezoek de online versie van dit hulpmiddel. Upload eenvoudig je CSV-bestand met DOIs en download de PDF's direct vanuit je browser.

## Steun dit project

Dit project is beschikbaar als **webapplicatie** op [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com) en als open-source code voor lokaal gebruik. Als je dit hulpmiddel nuttig vindt voor je onderzoek of werk, overweeg dan om de voortdurende ontwikkeling en onderhoud te ondersteunen:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

Je donaties helpen bij het ondersteunen van:

- 🌐 **Webapplicatie onderhoud** - Serverkosten, updates en betrouwbaarheid
- 💻 **Lokale app interface ontwikkeling** - Nieuwe functies en verbeteringen voor de desktopversie
- 🔧 Doorlopende ontwikkeling en bugfixes voor beide platforms
- 📚 Documentatie up-to-date houden
- ⚡ Compatibiliteit met nieuwste API's waarborgen

Zelfs kleine bijdragen maken een groot verschil in het levend en nuttig houden van dit project voor de onderzoeksgemeenschap!

## Functies

- DOI-gebaseerde PDF ophalen: Haalt en downloadt automatisch PDF's op met behulp van de Unpaywall API
- Voortgangsbewaking: Visualiseert de downloadvoortgang met een voortgangsbalk met behulp van tqdm
- Foutafhandeling: Logt en behandelt fouten zoals ontbrekende DOIs, mislukte downloads en niet-beschikbare open-access versies
- Geluidsmelding: Speelt een meldingsgeluid af bij voltooiing van alle downloads
- CSV-logging: Mislukte downloads worden opgenomen in een apart CSV-bestand voor eenvoudige follow-up

## Vereisten

- Python 3.6 of hoger
- Vereiste Python-pakketten (installeer via `pip install -r requirements.txt`):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## Installatie

1. Clone deze repository:

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. Installeer de vereiste pakketten:

```bash
pip install -r requirements.txt
```

## Gebruik

1. Bereid een CSV-bestand voor met een kolom genaamd 'DOI' met de Digital Object Identifiers van de artikelen die je wilt downloaden.
   Je kunt deze gegevens exporteren van:

   - Scopus: Exporteer zoekresultaten als CSV, zorg ervoor dat DOI is opgenomen
   - Web of Science: Exporteer zoekresultaten als CSV, zorg ervoor dat DOI is opgenomen

2. Configureer het script door deze variabelen te wijzigen in `UnpaywallPDFDownloader.py`:

   ```python
   # Je e-mailadres voor de Unpaywall API
   api_email = "your.email@example.com"  # Vervang door je e-mail

   # Directory waar je de gedownloade PDF's wilt opslaan
   download_dir = "path/to/your/download/directory"  # Vervang door je gewenste pad

   # Pad naar je CSV-bestand
   csv_file_path = "path/to/your/dois.csv"  # Vervang door je CSV-bestandspad
   ```

3. Voer het script uit:

```bash
python UnpaywallPDFDownloader.py
```

## Output

- Succesvol gedownloade PDF's worden opgeslagen in de opgegeven downloaddirectory
- Mislukte downloads worden opgenomen in een nieuw CSV-bestand genaamd 'rest_articles.csv' in dezelfde directory als de invoer-CSV
- Er wordt een meldingsgeluid afgespeeld wanneer het proces is voltooid
- Voortgangs- en foutmeldingen worden weergegeven in de console

## Foutafhandeling

Het script behandelt verschillende foutgevallen:

- Ontbrekende of ongeldige DOIs
- Netwerkverbindingsproblemen
- Niet-beschikbare open-access versies
- Mislukte PDF-downloads

Alle fouten worden gelogd met passende berichten in de console.

## Citering

Als je dit hulpmiddel gebruikt in je onderzoek, citeer het dan als volgt:

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

Gerelateerde DOI: https://doi.org/10.25500/edata.bham.00001292

## LICENTIE

Creative Commons Attribution 4.0 International (CC BY 4.0)

Je bent vrij om:

- Delen — het materiaal te kopiëren en te herdistribueren in elk medium of formaat
- Aanpassen — het materiaal te remixen, te transformeren en erop voort te bouwen voor elk doel, zelfs commercieel

Onder de volgende voorwaarden:

- **Naamsvermelding** — Je moet passende krediet geven, een link naar de licentie verstrekken en aangeven of wijzigingen zijn aangebracht.

Geen aanvullende beperkingen — je mag geen juridische voorwaarden of technologische maatregelen toepassen die anderen juridisch beperken om alles te doen wat de licentie toestaat.

Voor details, zie de volledige licentie op: https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## KENNISGEVING

Deze software is gelicenseerd onder de Creative Commons Attribution 4.0 International License (CC BY 4.0).

De auteur, Dr. Lixu Liu, verwelkomt kopiëren, wijziging, integratie en samenwerking.

Deze software is beschikbaar voor zowel academisch als commercieel gebruik, met de volgende verwachtingen:

- **Naamsvermelding is vereist** in alle openbaar gebruik of integraties.
- **Directe wederverkoop of herdistributie van de code of outputs zonder wijziging of toegevoegde waarde wordt ontmoedigd.**
- Gewijzigde versies moeten duidelijk aangeven dat ze verschillen van het origineel.

Om de auteur te erkennen of te informeren, neem contact op via: lixu@verdemetrix.com

## Bijdragen

Bijdragen zijn welkom! Aarzel niet om een Pull Request in te dienen.

# Richtlijnen voor commercieel gebruik

Dit project is gelicenseerd onder de [Creative Commons Attribution 4.0 License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).  
Je bent vrij om het materiaal te gebruiken, te delen en aan te passen — inclusief in commerciële projecten — mits je passende krediet geeft.

## Vereisten voor naamsvermelding

Als je dit project gebruikt (inclusief als onderdeel van een betaald product of dienst), moet je duidelijk krediet geven aan:

> Dr. Lixu Liu, University of Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## Respectvol gebruik

Hoewel commercieel gebruik is toegestaan door de licentie, **ontmoedigt de auteur directe wederverkoop of herdistributie** van dit project zonder betekenisvolle wijziging of toegevoegde waarde.

### ✅ Je mag:

- De software gebruiken of aanpassen in je betaalde platform of dienst
- Gewijzigde versies delen met passende krediet
- Het werk refereren of opnemen in academische, consultancy of publieke sector projecten

### ❌ Doe dit niet:

- De code "zoals-ie-is" verkopen of verpakken
- Het ZIP-bestand opnieuw posten als betaalde download
- Auteurskrediet verwijderen van outputs

Voor belangrijk commercieel gebruik of partnerschapsdiscussies, neem contact op via: info@verdemetrix.com
