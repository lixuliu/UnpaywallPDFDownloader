# UnpaywallPDFDownloader

Um script Python que automatiza o processo de download de artigos de pesquisa de acesso aberto em formato PDF usando DOIs (Identificadores de Objetos Digitais) recuperados de um arquivo CSV. O script utiliza a API Unpaywall para verificar a disponibilidade de versões de acesso aberto dos artigos e os baixa para um diretório especificado.

## Aplicação Web

**🌐 Experimente a versão online:** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

Para uma aplicação web amigável que não requer instalação do Python, visite a versão online desta ferramenta. Simplesmente faça upload do seu arquivo CSV com DOIs e baixe os PDFs diretamente do seu navegador.

## Apoie Este Projeto

Este projeto está disponível tanto como uma **aplicação web** em [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com) quanto como código de código aberto para uso local. Se você achar esta ferramenta útil para sua pesquisa ou trabalho, por favor considere apoiar seu desenvolvimento e manutenção contínuos:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

Suas doações ajudam a apoiar:

- 🌐 **Manutenção da aplicação web** - Custos de servidor, atualizações e confiabilidade
- 💻 **Desenvolvimento da interface do aplicativo local** - Novos recursos e melhorias para a versão desktop
- 🔧 Desenvolvimento contínuo e correções de bugs para ambas as plataformas
- 📚 Manter a documentação atualizada
- ⚡ Garantir compatibilidade com as APIs mais recentes

Mesmo pequenas contribuições fazem uma grande diferença para manter este projeto vivo e útil para a comunidade de pesquisa!

## Recursos

- Busca de PDFs baseada em DOI: Busca e baixa automaticamente PDFs usando a API Unpaywall
- Rastreamento de progresso: Visualiza o progresso do download com uma barra de progresso usando tqdm
- Tratamento de erros: Registra e trata erros como DOIs ausentes, downloads falhados e versões de acesso aberto indisponíveis
- Notificação sonora: Toca um som de notificação após a conclusão de todos os downloads
- Registro em CSV: Downloads falhados são registrados em um arquivo CSV separado para fácil acompanhamento

## Requisitos

- Python 3.6 ou superior
- Pacotes Python necessários (instale via `pip install -r requirements.txt`):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. Instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

## Uso

1. Prepare um arquivo CSV contendo uma coluna chamada 'DOI' com os Identificadores de Objetos Digitais dos artigos que você deseja baixar.
   Você pode exportar esses dados de:

   - Scopus: Exporte os resultados da pesquisa como CSV, garantindo que o DOI esteja incluído
   - Web of Science: Exporte os resultados da pesquisa como CSV, garantindo que o DOI esteja incluído

2. Configure o script modificando estas variáveis em `UnpaywallPDFDownloader.py`:

   ```python
   # Seu endereço de email para a API Unpaywall
   api_email = "seu.email@exemplo.com"  # Substitua pelo seu email

   # Diretório onde você quer salvar os PDFs baixados
   download_dir = "caminho/para/seu/diretorio/de/download"  # Substitua pelo caminho desejado

   # Caminho para seu arquivo CSV
   csv_file_path = "caminho/para/seu/dois.csv"  # Substitua pelo caminho do seu arquivo CSV
   ```

3. Execute o script:

```bash
python UnpaywallPDFDownloader.py
```

## Saída

- PDFs baixados com sucesso serão salvos no diretório de download especificado
- Downloads falhados serão registrados em um novo arquivo CSV chamado 'rest_articles.csv' no mesmo diretório do CSV de entrada
- Um som de notificação será reproduzido quando o processo estiver completo
- Mensagens de progresso e erro serão exibidas no console

## Tratamento de Erros

O script trata vários casos de erro:

- DOIs ausentes ou inválidos
- Problemas de conexão de rede
- Versões de acesso aberto indisponíveis
- Downloads de PDF falhados

Todos os erros são registrados com mensagens apropriadas no console.

## Citação

Se você usar esta ferramenta em sua pesquisa, por favor cite-a da seguinte forma:

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

DOI relacionado: https://doi.org/10.25500/edata.bham.00001292

## LICENÇA

Creative Commons Attribution 4.0 International (CC BY 4.0)

Você é livre para:

- Compartilhar — copiar e redistribuir o material em qualquer meio ou formato
- Adaptar — remixar, transformar e construir sobre o material para qualquer propósito, mesmo comercialmente

Sob os seguintes termos:

- **Atribuição** — Você deve dar o crédito apropriado, fornecer um link para a licença e indicar se foram feitas alterações.

Sem restrições adicionais — você não pode aplicar termos legais ou medidas tecnológicas que restrinjam legalmente outros de fazer qualquer coisa que a licença permita.

Para detalhes, veja a licença completa em: https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## AVISO

Este software está licenciado sob a Licença Creative Commons Attribution 4.0 International (CC BY 4.0).

O autor, Dr. Lixu Liu, acolhe cópia, modificação, integração e colaboração.

Este software está disponível tanto para uso acadêmico quanto comercial, com as seguintes expectativas:

- **A atribuição é obrigatória** em todos os usos ou integrações públicas.
- **A revenda direta ou redistribuição do código ou saídas sem modificação ou valor agregado é desencorajada.**
- Versões modificadas devem indicar claramente que diferem do original.

Para reconhecer ou notificar o autor, por favor entre em contato: lixu@verdemetrix.com

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar um Pull Request.

# Diretrizes de Uso Comercial

Este projeto está licenciado sob a [Licença Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).  
Você é livre para usar, compartilhar e adaptar o material — incluindo em projetos comerciais — desde que dê o crédito apropriado.

## Requisitos de Atribuição

Se você usar este projeto (incluindo como parte de um produto ou serviço pago), você deve creditar visivelmente:

> Dr. Lixu Liu, University of Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## Uso Respeitoso

Embora o uso comercial seja permitido pela licença, **o autor desencoraja a revenda direta ou redistribuição** deste projeto sem modificação significativa ou valor agregado.

### ✅ Você pode:

- Usar ou adaptar o software em sua plataforma ou serviço pago
- Compartilhar versões modificadas com o crédito apropriado
- Referenciar ou incluir o trabalho em projetos acadêmicos, de consultoria ou do setor público

### ❌ Por favor, não:

- Venda ou empacote o código "como está"
- Reposte o ZIP como um download pago
- Remova a atribuição do autor das saídas

Para uso comercial importante ou discussões de parceria, por favor entre em contato: info@verdemetrix.com
