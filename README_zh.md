# UnpaywallPDFDownloader

一个 Python 脚本，使用从 CSV 文件检索的 DOI（数字对象标识符）自动下载开放获取研究文章的 PDF 格式。该脚本利用 Unpaywall API 检查文章的开放获取版本的可用性，并将它们下载到指定目录。

## Web 应用程序

**🌐 尝试在线版本：** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

对于不需要 Python 安装的用户友好 Web 应用程序，请访问此工具的在线版本。只需上传包含 DOI 的 CSV 文件，即可直接从浏览器下载 PDF。

## 支持此项目

此项目既可作为[openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com)的**Web 应用程序**使用，也可作为本地使用的开源代码。如果您发现此工具对您的研究或工作有用，请考虑支持其持续开发和维护：

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

您的支持有助于维持项目发展：

- 🌐 **Web 应用程序维护** - 服务器成本、更新和稳定性
- 💻 **本地应用程序界面开发** - 桌面版本的新功能和改进
- 🔧 两个平台的持续开发和问题修复
- 📚 保持文档最新状态
- ⚡ 确保与最新 API 的兼容性

每一份支持都对保持此项目活力并为研究社区提供优质服务具有重要意义！

## 功能特点

- 基于 DOI 的 PDF 获取：使用 Unpaywall API 自动获取和下载 PDF
- 进度跟踪：使用 tqdm 可视化下载进度
- 错误处理：记录和处理错误，如缺失的 DOI、下载失败和不可用的开放获取版本
- 声音通知：所有下载完成后播放通知声音
- CSV 日志记录：失败的下载记录在单独的 CSV 文件中，便于后续处理

## 系统要求

- Python 3.6 或更高版本
- 必需的 Python 包（通过`pip install -r requirements.txt`安装）：
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## 安装

1. 克隆此仓库：

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. 安装必需的包：

```bash
pip install -r requirements.txt
```

## 使用方法

1. 准备一个 CSV 文件，其中包含名为'DOI'的列，包含您要下载的文章的数字对象标识符。
   您可以从以下来源导出此数据：

   - Scopus：将搜索结果导出为 CSV，确保包含 DOI
   - Web of Science：将搜索结果导出为 CSV，确保包含 DOI

2. 通过修改`UnpaywallPDFDownloader.py`中的这些变量来配置脚本：

   ```python
   # 您的Unpaywall API邮箱地址
   api_email = "your.email@example.com"  # 替换为您的邮箱

   # 您要保存下载PDF的目录
   download_dir = "path/to/your/download/directory"  # 替换为您所需的路径

   # 您的CSV文件路径
   csv_file_path = "path/to/your/dois.csv"  # 替换为您的CSV文件路径
   ```

3. 运行脚本：

```bash
python UnpaywallPDFDownloader.py
```

## 输出

- 成功下载的 PDF 将保存在指定的下载目录中
- 失败的下载将记录在名为'rest_articles.csv'的新 CSV 文件中，该文件位于输入 CSV 的同一目录中
- 过程完成时将播放通知声音
- 进度和错误消息将显示在控制台中

## 错误处理

脚本处理各种错误情况：

- 缺失或无效的 DOI
- 网络连接问题
- 不可用的开放获取版本
- PDF 下载失败

所有错误都会在控制台中记录相应的消息。

## 引用

如果您在研究中使用此工具，请按以下方式引用：

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

相关 DOI：https://doi.org/10.25500/edata.bham.00001292

## 许可证

知识共享署名 4.0 国际许可协议（CC BY 4.0）

您可以自由：

- 分享 — 以任何媒介或格式复制和重新分发材料
- 改编 — 重新混合、转换和基于材料构建，用于任何目的，甚至商业目的

在以下条件下：

- **署名** — 您必须给予适当的署名，提供许可证链接，并说明是否进行了更改。

没有额外限制 — 您不得应用法律条款或技术措施，在法律上限制他人做许可证允许的任何事情。

有关详细信息，请参阅完整许可证：https://creativecommons.org/licenses/by/4.0/

版权所有 © 2025 刘立旭博士

## 声明

本软件根据知识共享署名 4.0 国际许可协议（CC BY 4.0）获得许可。

作者刘立旭博士欢迎复制、修改、集成和协作。

本软件可用于学术和商业用途，但有以下期望：

- **在所有公共使用或集成中都需要署名。**
- **不鼓励直接转售或重新分发代码或输出，除非进行修改或增加价值。**
- 修改版本应清楚表明它们与原始版本不同。

要确认或通知作者，请联系：lixu@verdemetrix.com

## 贡献

欢迎贡献！请随时提交拉取请求。

# 商业使用指南

本项目根据[知识共享署名 4.0 许可协议（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/)获得许可。  
您可以自由使用、分享和改编材料 — 包括在商业项目中 — 只要您给予适当的署名。

## 署名要求

如果您使用此项目（包括作为付费产品或服务的一部分），您必须明显署名：

> 刘立旭博士，伯明翰大学  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## 尊重使用

虽然许可证允许商业使用，但**作者不鼓励直接转售或重新分发**此项目，除非进行有意义的修改或增加价值。

### ✅ 您可以：

- 在您的付费平台或服务中使用或改编软件
- 在适当署名的情况下分享修改版本
- 在学术、咨询或公共部门项目中引用或包含此工作

### ❌ 请不要：

- "按原样"销售或打包代码
- 将 ZIP 作为付费下载重新发布
- 从输出中删除作者署名

对于重大商业使用或合作伙伴讨论，请联系：info@verdemetrix.com

---

**🌍 [返回语言选择 / Back to Language Selection / Volver a Selección de Idioma / Retour à la Sélection de Langue](README.md)**
