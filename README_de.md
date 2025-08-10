# UnpaywallPDFDownloader

Ein Python-Skript, das den Download von Open-Access-Forschungsartikeln im PDF-Format automatisiert, indem es DOIs (Digital Object Identifiers) aus einer CSV-Datei abruft. Das Skript nutzt die Unpaywall API, um die Verfügbarkeit von Open-Access-Versionen der Artikel zu überprüfen und lädt sie in ein angegebenes Verzeichnis herunter.

## Web-Anwendung

**🌐 Testen Sie die Online-Version:** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

Für eine benutzerfreundliche Web-Anwendung, die keine Python-Installation erfordert, besuchen Sie die Online-Version dieses Tools. Laden Sie einfach Ihre CSV-Datei mit DOIs hoch und laden Sie die PDFs direkt aus Ihrem Browser herunter.

## Unterstützen Sie dieses Projekt

Dieses Projekt ist sowohl als **Web-Anwendung** unter [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com) als auch als Open-Source-Code für die lokale Nutzung verfügbar. Wenn Sie dieses Tool für Ihre Forschung oder Arbeit nützlich finden, erwägen Sie bitte, seine kontinuierliche Entwicklung und Wartung zu unterstützen:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsoren-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Spende%20mir%20einen%20Kaffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

Ihre Unterstützung hilft dabei, das Projekt zu erhalten:

- 🌐 **Wartung der Web-Anwendung** - Serverkosten, Updates und Zuverlässigkeit
- 💻 **Entwicklung der lokalen App-Oberfläche** - Neue Funktionen und Verbesserungen für die Desktop-Version
- 🔧 Laufende Entwicklung und Fehlerbehebung für beide Plattformen
- 📚 Dokumentation aktuell halten
- ⚡ Kompatibilität mit den neuesten APIs sicherstellen

Jeder Beitrag ist wertvoll, um dieses Projekt lebendig und nützlich für die Forschungsgemeinschaft zu halten!

## Funktionen

- DOI-basierter PDF-Download: Lädt PDFs automatisch mit der Unpaywall API herunter
- Fortschrittsverfolgung: Visualisiert den Download-Fortschritt mit einer Fortschrittsleiste unter Verwendung von tqdm
- Fehlerbehandlung: Protokolliert und behandelt Fehler wie fehlende DOIs, fehlgeschlagene Downloads und nicht verfügbare Open-Access-Versionen
- Tonbenachrichtigung: Spielt eine Benachrichtigung ab, wenn alle Downloads abgeschlossen sind
- CSV-Protokollierung: Fehlgeschlagene Downloads werden in einer separaten CSV-Datei für einfache Nachverfolgung protokolliert

## Anforderungen

- Python 3.6 oder höher
- Erforderliche Python-Pakete (Installation über `pip install -r requirements.txt`):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## Installation

1. Klonen Sie dieses Repository:

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. Installieren Sie die erforderlichen Pakete:

```bash
pip install -r requirements.txt
```

## Verwendung

1. Bereiten Sie eine CSV-Datei vor, die eine Spalte namens 'DOI' mit den Digital Object Identifiers der Artikel enthält, die Sie herunterladen möchten.
   Sie können diese Daten von folgenden Quellen exportieren:

   - Scopus: Exportieren Sie die Suchergebnisse als CSV und stellen Sie sicher, dass DOI enthalten ist
   - Web of Science: Exportieren Sie die Suchergebnisse als CSV und stellen Sie sicher, dass DOI enthalten ist

2. Konfigurieren Sie das Skript, indem Sie diese Variablen in `UnpaywallPDFDownloader.py` ändern:

   ```python
   # Ihre E-Mail-Adresse für die Unpaywall API
   api_email = "your.email@example.com"  # Ersetzen Sie durch Ihre E-Mail

   # Verzeichnis, in dem Sie die heruntergeladenen PDFs speichern möchten
   download_dir = "path/to/your/download/directory"  # Ersetzen Sie durch Ihren gewünschten Pfad

   # Pfad zu Ihrer CSV-Datei
   csv_file_path = "path/to/your/dois.csv"  # Ersetzen Sie durch den Pfad zu Ihrer CSV-Datei
   ```

3. Führen Sie das Skript aus:

```bash
python UnpaywallPDFDownloader.py
```

## Ausgabe

- Erfolgreich heruntergeladene PDFs werden im angegebenen Download-Verzeichnis gespeichert
- Fehlgeschlagene Downloads werden in einer neuen CSV-Datei namens 'rest_articles.csv' protokolliert, die sich im selben Verzeichnis wie die Eingabe-CSV befindet
- Eine Benachrichtigung wird abgespielt, wenn der Prozess abgeschlossen ist
- Fortschritts- und Fehlermeldungen werden in der Konsole angezeigt

## Fehlerbehandlung

Das Skript behandelt verschiedene Fehlerfälle:

- Fehlende oder ungültige DOIs
- Netzwerkverbindungsprobleme
- Nicht verfügbare Open-Access-Versionen
- Fehlgeschlagene PDF-Downloads

Alle Fehler werden mit entsprechenden Nachrichten in der Konsole protokolliert.

## Zitierung

Wenn Sie dieses Tool in Ihrer Forschung verwenden, zitieren Sie es bitte wie folgt:

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

Verwandte DOI: https://doi.org/10.25500/edata.bham.00001292

## Lizenz

Creative Commons Namensnennung 4.0 International Lizenz (CC BY 4.0)

Sie dürfen frei:

- Teilen — das Material in jedem Medium oder Format vervielfältigen und weiterverbreiten
- Anpassen — das Material neu mischen, verändern und darauf aufbauen, für jeden Zweck, auch kommerziell

Unter folgenden Bedingungen:

- **Namensnennung** — Sie müssen angemessene Urheber- und Rechteangaben machen, einen Link zur Lizenz beifügen und angeben, ob Änderungen vorgenommen wurden.

Keine weiteren Einschränkungen — Sie dürfen keine rechtlichen Bedingungen oder technischen Maßnahmen anwenden, die rechtlich andere daran hindern, alles zu tun, was die Lizenz erlaubt.

Weitere Informationen finden Sie unter der vollständigen Lizenz: https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## Haftungsausschluss

Diese Software ist unter der Creative Commons Namensnennung 4.0 International Lizenz (CC BY 4.0) lizenziert.

Der Autor Dr. Lixu Liu begrüßt Vervielfältigung, Modifikation, Integration und Zusammenarbeit.

Diese Software kann für akademische und kommerzielle Zwecke verwendet werden, aber mit folgenden Erwartungen:

- **Bei allen öffentlichen Nutzungen oder Integrationen ist eine Namensnennung erforderlich.**
- **Direkter Weiterverkauf oder Weiterverbreitung von Code oder Output wird nicht ermutigt, es sei denn, es werden Änderungen vorgenommen oder Wert hinzugefügt.**
- Modifizierte Versionen sollten klar anzeigen, dass sie sich von der ursprünglichen Version unterscheiden.

Für Bestätigung oder Benachrichtigung des Autors kontaktieren Sie: lixu@verdemetrix.com

## Beiträge

Beiträge sind willkommen! Reichen Sie gerne Pull Requests ein.

# Richtlinien für kommerzielle Nutzung

Dieses Projekt ist unter der [Creative Commons Namensnennung 4.0 Lizenz (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) lizenziert.  
Sie können das Material frei verwenden, teilen und anpassen — auch in kommerziellen Projekten — solange Sie angemessene Namensnennung leisten.

## Anforderungen an die Namensnennung

Wenn Sie dieses Projekt verwenden (einschließlich als Teil eines kostenpflichtigen Produkts oder einer Dienstleistung), müssen Sie deutlich kennzeichnen:

> Dr. Lixu Liu, Universität Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## Respektvolle Nutzung

Obwohl die Lizenz kommerzielle Nutzung erlaubt, **ermutigt der Autor nicht zum direkten Weiterverkauf oder zur Weiterverbreitung** dieses Projekts, es sei denn, es werden bedeutende Änderungen vorgenommen oder Wert hinzugefügt.

### ✅ Sie können:

- Das Software in Ihrer kostenpflichtigen Plattform oder Dienstleistung verwenden oder anpassen
- Modifizierte Versionen bei angemessener Namensnennung teilen
- Diese Arbeit in akademischen, beratenden oder öffentlichen Sektorprojekten zitieren oder einbeziehen

### ❌ Bitte nicht:

- Code "wie er ist" verkaufen oder verpacken
- ZIP als kostenpflichtigen Download neu veröffentlichen
- Autorenangaben aus dem Output entfernen

Für bedeutende kommerzielle Nutzung oder Partnerschaftsdiskussionen kontaktieren Sie: info@verdemetrix.com

---

**🌍 [Zurück zur Sprachauswahl / Back to Language Selection / Volver a Selección de Idioma / Retour à la Sélection de Langue](README.md)**
