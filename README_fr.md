# UnpaywallPDFDownloader

Un script Python qui automatise le processus de téléchargement d'articles de recherche en accès libre au format PDF en utilisant des DOIs (Identifiants d'Objets Numériques) récupérés depuis un fichier CSV. Le script utilise l'API Unpaywall pour vérifier la disponibilité des versions en accès libre des articles et les télécharge dans un répertoire spécifié.

## Application Web

**🌐 Essayez la version en ligne :** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

Pour une application web conviviale qui ne nécessite pas l'installation de Python, visitez la version en ligne de cet outil. Téléchargez simplement votre fichier CSV avec les DOIs et téléchargez les PDF directement depuis votre navigateur.

## Soutenez Ce Projet

Ce projet est disponible à la fois comme **application web** sur [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com) et comme code open-source pour un usage local. Si vous trouvez cet outil utile pour votre recherche ou votre travail, veuillez considérer soutenir son développement et sa maintenance continus :

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

Votre soutien aide à maintenir le projet :

- 🌐 **Maintenance de l'application web** - Coûts des serveurs, mises à jour et stabilité
- 💻 **Développement de l'interface de l'application locale** - Nouvelles fonctionnalités et améliorations pour la version bureau
- 🔧 Développement continu et correction de problèmes pour les deux plateformes
- 📚 Maintenir la documentation à jour
- ⚡ Assurer la compatibilité avec les dernières APIs

Chaque contribution est précieuse pour maintenir ce projet actif et utile pour la communauté de recherche !

## Fonctionnalités

- Téléchargement de PDF basé sur DOI : Récupère et télécharge automatiquement les PDF en utilisant l'API Unpaywall
- Suivi du progrès : Visualise le progrès du téléchargement avec une barre de progression utilisant tqdm
- Gestion des erreurs : Enregistre et gère les erreurs telles que les DOIs manquants, les téléchargements échoués et les versions en accès libre indisponibles
- Notification sonore : Joue un son de notification à la fin de tous les téléchargements
- Journalisation CSV : Les téléchargements échoués sont enregistrés dans un fichier CSV séparé pour un suivi facile

## Prérequis

- Python 3.6 ou supérieur
- Packages Python requis (installer via `pip install -r requirements.txt`) :
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## Installation

1. Clonez ce dépôt :

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. Installez les packages requis :

```bash
pip install -r requirements.txt
```

## Utilisation

1. Préparez un fichier CSV contenant une colonne nommée 'DOI' avec les Identifiants d'Objets Numériques des articles que vous souhaitez télécharger.
   Vous pouvez exporter ces données depuis :

   - Scopus : Exportez les résultats de recherche en CSV, en vous assurant que DOI est inclus
   - Web of Science : Exportez les résultats de recherche en CSV, en vous assurant que DOI est inclus

2. Configurez le script en modifiant ces variables dans `UnpaywallPDFDownloader.py` :

   ```python
   # Votre adresse email pour l'API Unpaywall
   api_email = "your.email@example.com"  # Remplacez par votre email

   # Répertoire où vous voulez sauvegarder les PDF téléchargés
   download_dir = "path/to/your/download/directory"  # Remplacez par votre chemin souhaité

   # Chemin vers votre fichier CSV
   csv_file_path = "path/to/your/dois.csv"  # Remplacez par le chemin de votre fichier CSV
   ```

3. Exécutez le script :

```bash
python UnpaywallPDFDownloader.py
```

## Sortie

- Les PDF téléchargés avec succès seront sauvegardés dans le répertoire de téléchargement spécifié
- Les téléchargements échoués seront enregistrés dans un nouveau fichier CSV nommé 'rest_articles.csv' dans le même répertoire que le CSV d'entrée
- Un son de notification sera joué lorsque le processus sera terminé
- Les messages de progrès et d'erreur seront affichés dans la console

## Gestion des Erreurs

Le script gère divers cas d'erreur :

- DOIs manquants ou invalides
- Problèmes de connexion réseau
- Versions en accès libre indisponibles
- Échecs de téléchargement de PDF

Toutes les erreurs sont enregistrées avec des messages appropriés dans la console.

## Citation

Si vous utilisez cet outil dans votre recherche, veuillez le citer comme suit :

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

DOI associé : https://doi.org/10.25500/edata.bham.00001292

## LICENCE

Creative Commons Attribution 4.0 International (CC BY 4.0)

Vous êtes libre de :

- Partager — copier et redistribuer le matériel sous n'importe quel format ou support
- Adapter — remixer, transformer et construire sur le matériel pour n'importe quel but, même commercialement

Sous les conditions suivantes :

- **Attribution** — Vous devez donner un crédit approprié, fournir un lien vers la licence et indiquer si des modifications ont été apportées.

Aucune restriction supplémentaire — vous ne pouvez pas appliquer de termes légaux ou de mesures technologiques qui restreignent légalement les autres de faire quoi que ce soit que la licence permet.

Pour plus de détails, consultez la licence complète à : https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## AVIS

Ce logiciel est sous licence Creative Commons Attribution 4.0 International (CC BY 4.0).

L'auteur, Dr. Lixu Liu, accueille la copie, la modification, l'intégration et la collaboration.

Ce logiciel est disponible pour un usage à la fois académique et commercial, avec les attentes suivantes :

- **L'attribution est requise** dans tous les usages ou intégrations publics.
- **La revente ou redistribution directe du code ou des sorties sans modification ou valeur ajoutée est découragée.**
- Les versions modifiées doivent clairement indiquer qu'elles diffèrent de l'original.

Pour reconnaître ou notifier l'auteur, veuillez contacter : lixu@verdemetrix.com

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.

# Directives d'Usage Commercial

Ce projet est sous licence [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).  
Vous êtes libre d'utiliser, partager et adapter le matériel — y compris dans des projets commerciaux — à condition de donner le crédit approprié.

## Exigences d'Attribution

Si vous utilisez ce projet (y compris comme partie d'un produit ou service payant), vous devez donner un crédit visiblement :

> Dr. Lixu Liu, Université de Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## Usage Respectueux

Bien que l'usage commercial soit permis par la licence, **l'auteur décourage la revente ou redistribution directe** de ce projet sans modification significative ou valeur ajoutée.

### ✅ Vous pouvez :

- Utiliser ou adapter le logiciel dans votre plateforme ou service payant
- Partager des versions modifiées avec un crédit approprié
- Référencer ou inclure le travail dans des projets académiques, de conseil ou du secteur public

### ❌ Veuillez ne pas :

- Vendre ou empaqueter le code "tel quel"
- Republier le ZIP comme un téléchargement payant
- Supprimer l'attribution de l'auteur des sorties

Pour un usage commercial majeur ou des discussions de partenariat, veuillez contacter : info@verdemetrix.com

---

**🌍 [Retour à la Sélection de Langue / Back to Language Selection / 返回语言选择 / Volver a Selección de Idioma](README.md)**
