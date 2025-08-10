# UnpaywallPDFDownloader

Uno script Python che automatizza il processo di download di articoli di ricerca ad accesso aperto in formato PDF utilizzando DOI (Identificatori di Oggetti Digitali) recuperati da un file CSV. Lo script utilizza l'API Unpaywall per verificare la disponibilità di versioni ad accesso aperto degli articoli e li scarica in una directory specificata.

## Applicazione Web

**🌐 Prova la versione online:** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

Per un'applicazione web user-friendly che non richiede l'installazione di Python, visita la versione online di questo strumento. Carica semplicemente il tuo file CSV con i DOI e scarica i PDF direttamente dal tuo browser.

## Supporta Questo Progetto

Questo progetto è disponibile sia come **applicazione web** su [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com) che come codice open-source per uso locale. Se trovi utile questo strumento per la tua ricerca o il tuo lavoro, considera di supportare il suo sviluppo e mantenimento continui:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

Il tuo supporto aiuta a mantenere il progetto:

- 🌐 **Manutenzione dell'applicazione web** - Costi del server, aggiornamenti e stabilità
- 💻 **Sviluppo dell'interfaccia dell'applicazione locale** - Nuove funzionalità e miglioramenti per la versione desktop
- 🔧 Sviluppo continuo e correzione di problemi per entrambe le piattaforme
- 📚 Mantenere la documentazione aggiornata
- ⚡ Garantire la compatibilità con le ultime API

Ogni contributo è prezioso per mantenere questo progetto attivo e utile per la comunità di ricerca!

## Caratteristiche

- Download di PDF basato su DOI: Recupera e scarica automaticamente i PDF utilizzando l'API Unpaywall
- Tracciamento del progresso: Visualizza il progresso del download con una barra di progresso utilizzando tqdm
- Gestione degli errori: Registra e gestisce errori come DOI mancanti, download falliti e versioni ad accesso aperto non disponibili
- Notifica sonora: Riproduce un suono di notifica al completamento di tutti i download
- Logging CSV: I download falliti vengono registrati in un file CSV separato per un facile follow-up

## Requisiti

- Python 3.6 o superiore
- Pacchetti Python richiesti (installa tramite `pip install -r requirements.txt`):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## Installazione

1. Clona questo repository:

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. Installa i pacchetti richiesti:

```bash
pip install -r requirements.txt
```

## Utilizzo

1. Prepara un file CSV contenente una colonna chiamata 'DOI' con gli Identificatori di Oggetti Digitali degli articoli che vuoi scaricare.
   Puoi esportare questi dati da:

   - Scopus: Esporta i risultati di ricerca come CSV, assicurandoti che DOI sia incluso
   - Web of Science: Esporta i risultati di ricerca come CSV, assicurandoti che DOI sia incluso

2. Configura lo script modificando queste variabili in `UnpaywallPDFDownloader.py`:

   ```python
   # Il tuo indirizzo email per l'API Unpaywall
   api_email = "your.email@example.com"  # Sostituisci con la tua email

   # Directory dove vuoi salvare i PDF scaricati
   download_dir = "path/to/your/download/directory"  # Sostituisci con il tuo percorso desiderato

   # Percorso al tuo file CSV
   csv_file_path = "path/to/your/dois.csv"  # Sostituisci con il percorso del tuo file CSV
   ```

3. Esegui lo script:

```bash
python UnpaywallPDFDownloader.py
```

## Output

- I PDF scaricati con successo verranno salvati nella directory di download specificata
- I download falliti verranno registrati in un nuovo file CSV chiamato 'rest_articles.csv' nella stessa directory del CSV di input
- Un suono di notifica verrà riprodotto quando il processo sarà completato
- I messaggi di progresso e di errore verranno visualizzati nella console

## Gestione degli Errori

Lo script gestisce vari casi di errore:

- DOI mancanti o non validi
- Problemi di connessione di rete
- Versioni ad accesso aperto non disponibili
- Download di PDF falliti

Tutti gli errori vengono registrati con messaggi appropriati nella console.

## Citazione

Se utilizzi questo strumento nella tua ricerca, citalo come segue:

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

DOI correlato: https://doi.org/10.25500/edata.bham.00001292

## LICENZA

Creative Commons Attribution 4.0 International (CC BY 4.0)

Puoi liberamente:

- Condividere — copiare e ridistribuire il materiale in qualsiasi mezzo o formato
- Adattare — remixare, trasformare e costruire sul materiale per qualsiasi scopo, anche commerciale

Sotto i seguenti termini:

- **Attribuzione** — Devi fornire un credito appropriato, fornire un link alla licenza e indicare se sono state apportate modifiche.

Nessuna restrizione aggiuntiva — non puoi applicare termini legali o misure tecnologiche che limitano legalmente gli altri dal fare qualsiasi cosa la licenza permetta.

Per i dettagli, vedi la licenza completa su: https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## AVVISO

Questo software è concesso in licenza sotto la Creative Commons Attribution 4.0 International License (CC BY 4.0).

L'autore, Dr. Lixu Liu, accoglie la copia, la modifica, l'integrazione e la collaborazione.

Questo software è reso disponibile sia per uso accademico che commerciale, con le seguenti aspettative:

- **L'attribuzione è richiesta** in tutti gli usi pubblici o integrazioni.
- **La rivendita diretta o la ridistribuzione del codice o degli output senza modifica o valore aggiunto è scoraggiata.**
- Le versioni modificate dovrebbero indicare chiaramente che differiscono dall'originale.

Per riconoscere o notificare l'autore, contatta: lixu@verdemetrix.com

## Contribuire

I contributi sono benvenuti! Non esitare a inviare una Pull Request.

# Linee Guida per l'Uso Commerciale

Questo progetto è concesso in licenza sotto la [Creative Commons Attribution 4.0 License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).  
Puoi liberamente usare, condividere e adattare il materiale — incluso nei progetti commerciali — a condizione di fornire il credito appropriato.

## Requisiti di Attribuzione

Se utilizzi questo progetto (incluso come parte di un prodotto o servizio a pagamento), devi visibilmente accreditare:

> Dr. Lixu Liu, Università di Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## Uso Rispettoso

Sebbene l'uso commerciale sia permesso dalla licenza, **l'autore scoraggia la rivendita diretta o la ridistribuzione** di questo progetto senza modifiche significative o valore aggiunto.

### ✅ Puoi:

- Utilizzare o adattare il software nella tua piattaforma o servizio a pagamento
- Condividere versioni modificate con il credito appropriato
- Riferire o includere il lavoro in progetti accademici, di consulenza o del settore pubblico

### ❌ Per favore non:

- Vendere o impacchettare il codice "così com'è"
- Ripubblicare lo ZIP come download a pagamento
- Rimuovere l'attribuzione dell'autore dagli output

Per uso commerciale importante o discussioni di partnership, contatta: info@verdemetrix.com
