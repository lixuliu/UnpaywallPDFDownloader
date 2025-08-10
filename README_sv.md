# UnpaywallPDFDownloader

Ett Python-skript som automatiserar processen att ladda ner öppen tillgång forskningsartiklar i PDF-format med hjälp av DOIs (Digital Object Identifiers) hämtade från en CSV-fil. Skriptet använder Unpaywall API för att kontrollera tillgängligheten av öppen tillgång-versioner av artiklarna och laddar ner dem till en angiven katalog.

## Webbapplikation

**🌐 Prova online-versionen:** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

För en användarvänlig webbapplikation som inte kräver Python-installation, besök online-versionen av detta verktyg. Ladda bara upp din CSV-fil med DOIs och ladda ner PDF:erna direkt från din webbläsare.

## Stöd detta projekt

Detta projekt finns tillgängligt både som en **webbapplikation** på [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com) och som öppen källkod för lokal användning. Om du tycker att detta verktyg är användbart för din forskning eller ditt arbete, överväg att stödja dess fortsatta utveckling och underhåll:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

Dina donationer hjälper till att stödja:

- 🌐 **Webbapplikationsunderhåll** - Serverkostnader, uppdateringar och tillförlitlighet
- 💻 **Lokal appgränssnittsutveckling** - Nya funktioner och förbättringar för desktop-versionen
- 🔧 Pågående utveckling och buggfixar för båda plattformarna
- 📚 Hålla dokumentationen uppdaterad
- ⚡ Säkerställa kompatibilitet med senaste API:er

Även små bidrag gör stor skillnad för att hålla detta projekt levande och användbart för forskningssamhället!

## Funktioner

- DOI-baserad PDF-hämtning: Hämtar och laddar ner PDF:er automatiskt med hjälp av Unpaywall API
- Framstegsspårning: Visualiserar nedladdningsframsteget med en framstegsindikator med hjälp av tqdm
- Felhantering: Loggar och hanterar fel som saknade DOIs, misslyckade nedladdningar och otillgängliga öppen tillgång-versioner
- Ljudmeddelande: Spelar upp ett meddelandeljud när alla nedladdningar är klara
- CSV-loggning: Misslyckade nedladdningar registreras i en separat CSV-fil för enkel uppföljning

## Krav

- Python 3.6 eller högre
- Nödvändiga Python-paket (installera via `pip install -r requirements.txt`):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## Installation

1. Klona detta repository:

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. Installera de nödvändiga paketen:

```bash
pip install -r requirements.txt
```

## Användning

1. Förbered en CSV-fil som innehåller en kolumn med namnet 'DOI' med Digital Object Identifiers för artiklarna du vill ladda ner.
   Du kan exportera denna data från:

   - Scopus: Exportera sökresultat som CSV, se till att DOI ingår
   - Web of Science: Exportera sökresultat som CSV, se till att DOI ingår

2. Konfigurera skriptet genom att modifiera dessa variabler i `UnpaywallPDFDownloader.py`:

   ```python
   # Din e-postadress för Unpaywall API
   api_email = "your.email@example.com"  # Ersätt med din e-post

   # Katalog där du vill spara de nedladdade PDF:erna
   download_dir = "path/to/your/download/directory"  # Ersätt med din önskade sökväg

   # Sökväg till din CSV-fil
   csv_file_path = "path/to/your/dois.csv"  # Ersätt med din CSV-fils sökväg
   ```

3. Kör skriptet:

```bash
python UnpaywallPDFDownloader.py
```

## Utdata

- Framgångsrikt nedladdade PDF:er kommer att sparas i den angivna nedladdningskatalogen
- Misslyckade nedladdningar kommer att registreras i en ny CSV-fil med namnet 'rest_articles.csv' i samma katalog som indata-CSV:en
- Ett meddelandeljud kommer att spelas upp när processen är klar
- Framsteg och felmeddelanden kommer att visas i konsolen

## Felhantering

Skriptet hanterar olika felfall:

- Saknade eller ogiltiga DOIs
- Nätverksanslutningsproblem
- Otillgängliga öppen tillgång-versioner
- Misslyckade PDF-nedladdningar

Alla fel loggas med lämpliga meddelanden i konsolen.

## Citering

Om du använder detta verktyg i din forskning, citera det gärna enligt följande:

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

Relaterad DOI: https://doi.org/10.25500/edata.bham.00001292

## LICENS

Creative Commons Attribution 4.0 International (CC BY 4.0)

Du får fritt:

- Dela — kopiera och distribuera om materialet i vilket medium eller format som helst
- Anpassa — remixa, transformera och bygga vidare på materialet för vilket syfte som helst, även kommersiellt

Under följande villkor:

- **Erkännande** — Du måste ge lämplig erkänsla, tillhandahålla en länk till licensen och ange om ändringar gjordes.

Inga ytterligare begränsningar — du får inte tillämpa juridiska villkor eller tekniska åtgärder som juridiskt begränsar andra från att göra något som licensen tillåter.

För detaljer, se den fullständiga licensen på: https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## MEDDELANDE

Denna programvara är licensierad under Creative Commons Attribution 4.0 International License (CC BY 4.0).

Författaren, Dr. Lixu Liu, välkomnar kopiering, modifiering, integration och samarbete.

Denna programvara görs tillgänglig för både akademiskt och kommersiellt bruk, med följande förväntningar:

- **Erkännande krävs** i alla offentliga användningar eller integrationer.
- **Direkt återförsäljning eller omdistribution av koden eller utdata utan modifiering eller tillagd värde uppmuntras inte.**
- Modifierade versioner bör tydligt indikera att de skiljer sig från originalet.

För att erkänna eller meddela författaren, kontakta: lixu@verdemetrix.com

## Bidrag

Bidrag är välkomna! Tveka inte att skicka in en Pull Request.

# Riktlinjer för kommersiell användning

Detta projekt är licensierad under [Creative Commons Attribution 4.0 License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).  
Du får fritt använda, dela och anpassa materialet — inklusive i kommersiella projekt — förutsatt att du ger lämplig erkänsla.

## Krav för erkännande

Om du använder detta projekt (inklusive som en del av en betald produkt eller tjänst), måste du synligt erkänna:

> Dr. Lixu Liu, University of Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## Respektfull användning

Även om kommersiell användning tillåts av licensen, **uppmuntrar författaren inte direkt återförsäljning eller omdistribution** av detta projekt utan meningsfull modifiering eller tillagt värde.

### ✅ Du får:

- Använda eller anpassa programvaran i din betalda plattform eller tjänst
- Dela modifierade versioner med lämplig erkänsla
- Referera eller inkludera arbetet i akademiska, konsult- eller offentliga sektorprojekt

### ❌ Vänligen gör inte:

- Sälja eller paketera koden "som den är"
- Återpublicera ZIP:en som en betald nedladdning
- Ta bort författarens erkännande från utdata

För större kommersiell användning eller partnerskapsdiskussioner, kontakta: info@verdemetrix.com

---

**🌍 [Tillbaka till språkval / Back to Language Selection / 返回语言选择 / Volver a Selección de Idioma / Retour à la Sélection de Langue](README.md)**
