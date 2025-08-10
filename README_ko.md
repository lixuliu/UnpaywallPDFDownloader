# UnpaywallPDFDownloader

- 🇺🇸 [English](README_en.md) - 🇨🇳 [中文](README_zh.md) - 🇪🇸 [Español](README_es.md) - 🇫🇷 [Français](README_fr.md) - 🇯🇵 [日本語](README_ja.md) - 🇷🇺 [Русский](README_ru.md) - 🇮🇹 [Italiano](README_it.md) - 🇩🇪 [Deutsch](README_de.md) - 🇵🇹 [Português](README_pt.md) - 🇰🇷 [한국어](README_ko.md)

---

CSV 파일에서 검색된 DOI(디지털 객체 식별자)를 사용하여 오픈 액세스 연구 논문을 PDF 형식으로 다운로드하는 과정을 자동화하는 Python 스크립트입니다. 이 스크립트는 Unpaywall API를 사용하여 논문의 오픈 액세스 버전 가용성을 확인하고 지정된 디렉토리에 다운로드합니다.

## 웹 애플리케이션

**🌐 온라인 버전을 사용해보세요:** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

Python 설치가 필요 없는 사용자 친화적인 웹 애플리케이션을 위해 이 도구의 온라인 버전을 방문하세요. DOI가 포함된 CSV 파일을 업로드하고 브라우저에서 직접 PDF를 다운로드하세요.

## 이 프로젝트 지원하기

이 프로젝트는 [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com)의 **웹 애플리케이션**과 로컬 사용을 위한 오픈소스 코드로 모두 제공됩니다. 연구나 업무에 이 도구가 유용하다고 생각되시면 지속적인 개발과 유지보수를 지원해 주시기 바랍니다:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

기부금은 다음을 지원합니다:

- 🌐 **웹 애플리케이션 유지보수** - 서버 비용, 업데이트 및 안정성
- 💻 **로컬 앱 인터페이스 개발** - 데스크톱 버전의 새로운 기능 및 개선사항
- 🔧 두 플랫폼 모두를 위한 지속적인 개발 및 버그 수정
- 📚 문서 최신 상태 유지
- ⚡ 최신 API와의 호환성 보장

작은 기여도 연구 커뮤니티를 위해 이 프로젝트를 살아있고 유용하게 유지하는 데 큰 도움이 됩니다!

## 주요 기능

- DOI 기반 PDF 가져오기: Unpaywall API를 사용하여 PDF를 자동으로 가져오고 다운로드
- 진행 상황 추적: tqdm을 사용한 진행 막대로 다운로드 진행 상황을 시각화
- 오류 처리: 누락된 DOI, 실패한 다운로드, 사용할 수 없는 오픈 액세스 버전과 같은 오류를 로깅하고 처리
- 소리 알림: 모든 다운로드 완료 시 알림 소리 재생
- CSV 로깅: 실패한 다운로드는 별도의 CSV 파일에 기록되어 후속 조치가 용이

## 요구사항

- Python 3.6 이상
- 필요한 Python 패키지 (`pip install -r requirements.txt`로 설치):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## 설치

1. 이 저장소를 클론합니다:

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. 필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

## 사용법

1. 다운로드하려는 논문의 디지털 객체 식별자가 포함된 'DOI'라는 열이 있는 CSV 파일을 준비합니다.
   다음에서 이 데이터를 내보낼 수 있습니다:

   - Scopus: 검색 결과를 CSV로 내보내기, DOI 포함 확인
   - Web of Science: 검색 결과를 CSV로 내보내기, DOI 포함 확인

2. `UnpaywallPDFDownloader.py`에서 다음 변수를 수정하여 스크립트를 구성합니다:

   ```python
   # Unpaywall API용 이메일 주소
   api_email = "your.email@example.com"  # 이메일로 교체

   # 다운로드한 PDF를 저장할 디렉토리
   download_dir = "path/to/your/download/directory"  # 원하는 경로로 교체

   # CSV 파일 경로
   csv_file_path = "path/to/your/dois.csv"  # CSV 파일 경로로 교체
   ```

3. 스크립트를 실행합니다:

```bash
python UnpaywallPDFDownloader.py
```

## 출력

- 성공적으로 다운로드된 PDF는 지정된 다운로드 디렉토리에 저장됩니다
- 실패한 다운로드는 입력 CSV와 같은 디렉토리에 'rest_articles.csv'라는 새 CSV 파일에 기록됩니다
- 프로세스가 완료되면 알림 소리가 재생됩니다
- 진행 상황 및 오류 메시지가 콘솔에 표시됩니다

## 오류 처리

스크립트는 다양한 오류 사례를 처리합니다:

- 누락되거나 잘못된 DOI
- 네트워크 연결 문제
- 사용할 수 없는 오픈 액세스 버전
- 실패한 PDF 다운로드

모든 오류는 콘솔에 적절한 메시지와 함께 로깅됩니다.

## 인용

연구에서 이 도구를 사용하는 경우 다음과 같이 인용해 주세요:

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

관련 DOI: https://doi.org/10.25500/edata.bham.00001292

## 라이선스

Creative Commons Attribution 4.0 International (CC BY 4.0)

다음과 같은 자유가 있습니다:

- 공유 — 어떤 매체나 형식으로든 자료를 복사하고 재배포
- 적응 — 어떤 목적으로든 자료를 리믹스, 변형 및 구축, 상업적 사용도 가능

다음 조건 하에서:

- **저작자 표시** — 적절한 크레딧을 제공하고, 라이선스 링크를 제공하며, 변경사항이 있는 경우 표시해야 합니다.

추가 제한 없음 — 다른 사람이 라이선스가 허용하는 것을 하는 것을 법적으로 제한하는 법적 조건이나 기술적 조치를 적용할 수 없습니다.

자세한 내용은 전체 라이선스를 참조하세요: https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## 공지사항

이 소프트웨어는 Creative Commons Attribution 4.0 International License (CC BY 4.0) 하에 라이선스됩니다.

저자 Dr. Lixu Liu는 복사, 수정, 통합 및 협업을 환영합니다.

이 소프트웨어는 학술 및 상업적 사용을 위해 제공되며, 다음과 같은 기대사항이 있습니다:

- 모든 공개 사용 또는 통합에서 **저작자 표시가 필요**합니다.
- **코드나 출력물의 직접 재판매 또는 수정이나 부가가치 없이 재배포는 권장되지 않습니다.**
- 수정된 버전은 원본과 다르다는 것을 명확히 표시해야 합니다.

저자에게 인정하거나 알리려면 다음으로 연락하세요: lixu@verdemetrix.com

## 기여

기여를 환영합니다! Pull Request를 자유롭게 제출해 주세요.

# 상업적 사용 가이드라인

이 프로젝트는 [Creative Commons Attribution 4.0 License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) 하에 라이선스됩니다.  
적절한 크레딧을 제공하는 한 상업적 프로젝트를 포함하여 자료를 자유롭게 사용, 공유 및 적응할 수 있습니다.

## 저작자 표시 요구사항

이 프로젝트를 사용하는 경우(유료 제품이나 서비스의 일부로 포함) 다음을 명시적으로 크레딧해야 합니다:

> Dr. Lixu Liu, University of Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## 존중하는 사용

라이선스에 의해 상업적 사용이 허용되지만, **저자는 의미 있는 수정이나 부가가치 없이 이 프로젝트를 직접 재판매하거나 재배포하는 것을 권장하지 않습니다.**

### ✅ 할 수 있는 것:

- 유료 플랫폼이나 서비스에서 소프트웨어 사용 또는 적응
- 적절한 크레딧과 함께 수정된 버전 공유
- 학술, 컨설팅 또는 공공 부문 프로젝트에서 작업 참조 또는 포함

### ❌ 하지 말아야 할 것:

- 코드를 "있는 그대로" 판매하거나 패키징
- ZIP을 유료 다운로드로 재게시
- 출력물에서 저자 크레딧 제거

주요 상업적 사용이나 파트너십 논의를 위해 다음으로 연락하세요: info@verdemetrix.com
