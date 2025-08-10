# UnpaywallPDFDownloader

Un script de Python que automatiza el proceso de descarga de artículos de investigación de acceso abierto en formato PDF usando DOIs (Identificadores de Objetos Digitales) recuperados de un archivo CSV. El script utiliza la API de Unpaywall para verificar la disponibilidad de versiones de acceso abierto de los artículos y los descarga a un directorio especificado.

## Aplicación Web

**🌐 Prueba la versión en línea:** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

Para una aplicación web fácil de usar que no requiere instalación de Python, visita la versión en línea de esta herramienta. Simplemente sube tu archivo CSV con DOIs y descarga los PDFs directamente desde tu navegador.

## Apoya Este Proyecto

Este proyecto está disponible tanto como **aplicación web** en [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com) como código de código abierto para uso local. Si encuentras útil esta herramienta para tu investigación o trabajo, por favor considera apoyar su desarrollo y mantenimiento continuo:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

Tus donaciones ayudan a apoyar:

- 🌐 **Mantenimiento de la aplicación web** - Costos del servidor, actualizaciones y confiabilidad
- 💻 **Desarrollo de la interfaz de la aplicación local** - Nuevas características y mejoras para la versión de escritorio
- 🔧 Desarrollo continuo y corrección de errores para ambas plataformas
- 📚 Mantener la documentación actualizada
- ⚡ Asegurar compatibilidad con las últimas APIs

¡Incluso las pequeñas contribuciones hacen una gran diferencia en mantener este proyecto vivo y útil para la comunidad de investigación!

## Características

- Descarga de PDF basada en DOI: Automáticamente obtiene y descarga PDFs usando la API de Unpaywall
- Seguimiento del progreso: Visualiza el progreso de descarga con una barra de progreso usando tqdm
- Manejo de errores: Registra y maneja errores como DOIs faltantes, descargas fallidas y versiones de acceso abierto no disponibles
- Notificación de sonido: Reproduce un sonido de notificación al completar todas las descargas
- Registro CSV: Las descargas fallidas se registran en un archivo CSV separado para un seguimiento fácil

## Requisitos

- Python 3.6 o superior
- Paquetes de Python requeridos (instalar vía `pip install -r requirements.txt`):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. Instala los paquetes requeridos:

```bash
pip install -r requirements.txt
```

## Uso

1. Prepara un archivo CSV que contenga una columna llamada 'DOI' con los Identificadores de Objetos Digitales de los artículos que quieres descargar.
   Puedes exportar estos datos desde:

   - Scopus: Exporta los resultados de búsqueda como CSV, asegurándote de que DOI esté incluido
   - Web of Science: Exporta los resultados de búsqueda como CSV, asegurándote de que DOI esté incluido

2. Configura el script modificando estas variables en `UnpaywallPDFDownloader.py`:

   ```python
   # Tu dirección de correo electrónico para la API de Unpaywall
   api_email = "your.email@example.com"  # Reemplaza con tu correo

   # Directorio donde quieres guardar los PDFs descargados
   download_dir = "path/to/your/download/directory"  # Reemplaza con tu ruta deseada

   # Ruta a tu archivo CSV
   csv_file_path = "path/to/your/dois.csv"  # Reemplaza con la ruta de tu archivo CSV
   ```

3. Ejecuta el script:

```bash
python UnpaywallPDFDownloader.py
```

## Salida

- Los PDFs descargados exitosamente se guardarán en el directorio de descarga especificado
- Las descargas fallidas se registrarán en un nuevo archivo CSV llamado 'rest_articles.csv' en el mismo directorio que el CSV de entrada
- Se reproducirá un sonido de notificación cuando el proceso esté completo
- Los mensajes de progreso y error se mostrarán en la consola

## Manejo de Errores

El script maneja varios casos de error:

- DOIs faltantes o inválidos
- Problemas de conexión de red
- Versiones de acceso abierto no disponibles
- Descargas de PDF fallidas

Todos los errores se registran con mensajes apropiados en la consola.

## Cita

Si usas esta herramienta en tu investigación, por favor cítala de la siguiente manera:

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

DOI relacionado: https://doi.org/10.25500/edata.bham.00001292

## LICENCIA

Creative Commons Attribution 4.0 International (CC BY 4.0)

Eres libre de:

- Compartir — copiar y redistribuir el material en cualquier medio o formato
- Adaptar — remezclar, transformar y construir sobre el material para cualquier propósito, incluso comercialmente

Bajo los siguientes términos:

- **Atribución** — Debes dar crédito apropiado, proporcionar un enlace a la licencia e indicar si se realizaron cambios.

Sin restricciones adicionales — no puedes aplicar términos legales o medidas tecnológicas que legalmente restrinjan a otros de hacer cualquier cosa que la licencia permita.

Para más detalles, consulta la licencia completa en: https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## AVISO

Este software está licenciado bajo la Licencia Creative Commons Attribution 4.0 International (CC BY 4.0).

El autor, Dr. Lixu Liu, da la bienvenida a la copia, modificación, integración y colaboración.

Este software está disponible tanto para uso académico como comercial, con las siguientes expectativas:

- **Se requiere atribución** en todos los usos o integraciones públicos.
- **No se recomienda la reventa o redistribución directa del código o salidas sin modificación o valor agregado.**
- Las versiones modificadas deben indicar claramente que difieren del original.

Para reconocer o notificar al autor, por favor contacta: lixu@verdemetrix.com

## Contribuir

¡Las contribuciones son bienvenidas! Por favor, no dudes en enviar una Pull Request.

# Pautas de Uso Comercial

Este proyecto está licenciado bajo la [Licencia Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).  
Eres libre de usar, compartir y adaptar el material — incluyendo en proyectos comerciales — siempre que des el crédito apropiado.

## Requisitos de Atribución

Si usas este proyecto (incluyendo como parte de un producto o servicio pagado), debes dar crédito visiblemente:

> Dr. Lixu Liu, Universidad de Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## Uso Respetuoso

Aunque el uso comercial está permitido por la licencia, **el autor desaconseja la reventa o redistribución directa** de este proyecto sin modificación significativa o valor agregado.

### ✅ Puedes:

- Usar o adaptar el software en tu plataforma o servicio pagado
- Compartir versiones modificadas con crédito apropiado
- Referenciar o incluir el trabajo en proyectos académicos, de consultoría o del sector público

### ❌ Por favor no:

- Vendas o empaquetes el código "tal como está"
- Republiques el ZIP como una descarga pagada
- Elimines la atribución del autor de las salidas

Para uso comercial importante o discusiones de asociación, por favor contacta: info@verdemetrix.com

---

**🌍 [Volver a Selección de Idioma / Back to Language Selection / 返回语言选择 / Retour à la Sélection de Langue](README.md)**
