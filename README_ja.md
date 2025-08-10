# UnpaywallPDFDownloader

CSV ファイルから取得した DOI（デジタルオブジェクト識別子）を使用して、オープンアクセス研究論文を PDF 形式で自動的にダウンロードする Python スクリプトです。このスクリプトは Unpaywall API を使用して、論文のオープンアクセス版の可用性をチェックし、指定されたディレクトリにダウンロードします。

## Web アプリケーション

**🌐 オンライン版をお試しください：** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

Python のインストールが不要なユーザーフレンドリーな Web アプリケーションについては、このツールのオンライン版をご覧ください。DOI を含む CSV ファイルをアップロードするだけで、ブラウザから直接 PDF をダウンロードできます。

## このプロジェクトをサポート

このプロジェクトは、[openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com)の**Web アプリケーション**として、またローカル使用のためのオープンソースコードとして利用できます。このツールがあなたの研究や仕事に役立つと思われる場合は、継続的な開発とメンテナンスをサポートすることをご検討ください：

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

あなたのサポートがプロジェクトを支えます：

- 🌐 **Web アプリケーションのメンテナンス** - サーバーコスト、更新、安定性
- 💻 **ローカルアプリインターフェースの開発** - デスクトップ版の新機能と改善
- 🔧 両プラットフォームの継続的な開発と問題修正
- 📚 ドキュメントの最新化
- ⚡ 最新 API との互換性の確保

各サポートが、このプロジェクトを活発に保ち、研究コミュニティにとって有用なものにするために重要です！

## 機能

- DOI ベースの PDF 取得：Unpaywall API を使用して PDF を自動的に取得・ダウンロード
- 進捗追跡：tqdm を使用してダウンロードの進捗を視覚化
- エラーハンドリング：不足している DOI、ダウンロードの失敗、利用できないオープンアクセス版などのエラーを記録・処理
- サウンド通知：すべてのダウンロード完了時に通知音を再生
- CSV ログ記録：失敗したダウンロードは別の CSV ファイルに記録され、簡単なフォローアップが可能

## 要件

- Python 3.6 以上
- 必要な Python パッケージ（`pip install -r requirements.txt`でインストール）：
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## インストール

1. このリポジトリをクローン：

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. 必要なパッケージをインストール：

```bash
pip install -r requirements.txt
```

## 使用方法

1. ダウンロードしたい論文のデジタルオブジェクト識別子を含む「DOI」という名前の列を持つ CSV ファイルを準備します。
   このデータは以下からエクスポートできます：

   - Scopus：検索結果を CSV としてエクスポートし、DOI が含まれていることを確認
   - Web of Science：検索結果を CSV としてエクスポートし、DOI が含まれていることを確認

2. `UnpaywallPDFDownloader.py`のこれらの変数を変更してスクリプトを設定：

   ```python
   # Unpaywall API用のメールアドレス
   api_email = "your.email@example.com"  # あなたのメールに置き換えてください

   # ダウンロードしたPDFを保存したいディレクトリ
   download_dir = "path/to/your/download/directory"  # 希望するパスに置き換えてください

   # CSVファイルへのパス
   csv_file_path = "path/to/your/dois.csv"  # CSVファイルのパスに置き換えてください
   ```

3. スクリプトを実行：

```bash
python UnpaywallPDFDownloader.py
```

## 出力

- 正常にダウンロードされた PDF は指定されたダウンロードディレクトリに保存されます
- 失敗したダウンロードは、入力 CSV と同じディレクトリの「rest_articles.csv」という名前の新しい CSV ファイルに記録されます
- プロセス完了時に通知音が再生されます
- 進捗とエラーメッセージがコンソールに表示されます

## エラーハンドリング

スクリプトは様々なエラーケースを処理します：

- 不足または無効な DOI
- ネットワーク接続の問題
- 利用できないオープンアクセス版
- PDF ダウンロードの失敗

すべてのエラーはコンソールに適切なメッセージで記録されます。

## 引用

このツールを研究で使用する場合は、以下のように引用してください：

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

関連 DOI：https://doi.org/10.25500/edata.bham.00001292

## ライセンス

Creative Commons Attribution 4.0 International (CC BY 4.0)

あなたは以下を自由に行えます：

- 共有 — 任意の媒体または形式で材料をコピーおよび再配布
- 適応 — 任意の目的で材料をリミックス、変換、構築（商業目的も含む）

以下の条件の下で：

- **帰属表示** — 適切なクレジットを与え、ライセンスへのリンクを提供し、変更が行われたかどうかを示す必要があります。

追加の制限はありません — ライセンスが許可することを他の人が行うことを法的に制限する法的条件または技術的措置を適用することはできません。

詳細については、完全なライセンスを参照してください：https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## 注意事項

このソフトウェアは Creative Commons Attribution 4.0 International License (CC BY 4.0)の下でライセンスされています。

著者である劉立旭博士は、コピー、修正、統合、協力を歓迎します。

このソフトウェアは学術的および商業的用途の両方で利用可能ですが、以下の期待があります：

- **すべての公的使用または統合で帰属表示が必要です。**
- **修正や付加価値なしでのコードや出力の直接的な再販または再配布は推奨されません。**
- 修正版は元の版と異なることを明確に示す必要があります。

著者を確認または通知するには、以下にお問い合わせください：lixu@verdemetrix.com

## 貢献

貢献を歓迎します！プルリクエストを自由に送信してください。

# 商業利用ガイドライン

このプロジェクトは[Creative Commons Attribution 4.0 License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)の下でライセンスされています。  
適切なクレジットを与える限り、材料を使用、共有、適応する自由があります — 商業プロジェクトを含む。

## 帰属表示要件

このプロジェクトを使用する場合（有料製品またはサービスの一部として含む）、以下のように明示的にクレジットを表示する必要があります：

> Dr. Lixu Liu, University of Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## 尊重ある使用

ライセンスによって商業利用が許可されているにもかかわらず、**著者は意味のある修正や付加価値なしでのこのプロジェクトの直接的な再販または再配布を推奨しません**。

### ✅ あなたは以下を行うことができます：

- 有料プラットフォームまたはサービスでソフトウェアを使用または適応
- 適切なクレジットで修正版を共有
- 学術、コンサルティング、または公共セクターのプロジェクトで作業を参照または含める

### ❌ 以下は行わないでください：

- コードを「そのまま」販売またはパッケージ化
- ZIP を有料ダウンロードとして再投稿
- 出力から著者の帰属表示を削除

重要な商業利用やパートナーシップの議論については、以下にお問い合わせください：info@verdemetrix.com

---

**🌍 [言語選択に戻る / Back to Language Selection / 返回语言选择 / Volver a Selección de Idioma / Retour à la Sélection de Langue](README.md)**
