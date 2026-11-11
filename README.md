# 사진편집기 앱

[https://unatavel.github.io/doyun/](https://unatavel.github.io/doyun/) 사이트를 전체 화면 WebView로 보여주는 안드로이드 앱입니다.

안드로이드 스튜디오 없이 GitHub Actions로 APK를 빌드할 수 있습니다.

## 앱 구성

- 앱 이름: **사진편집기**
- 패키지: `com.doyun.photoeditor`
- 사이트 주소: `https://unatavel.github.io/doyun/`
- 아이콘: 밝은 하늘색 사진 프레임 디자인 (`art/app-icon.png`)

사진 선택, 여러 장 업로드, 편집 결과 다운로드가 WebView에서도 동작하도록 파일 선택창과 다운로드를 연결해 두었습니다. 한국해양대학교 홈페이지처럼 외부 링크는 기본 브라우저에서 엽니다.

## GitHub Actions로 APK 받기

1. GitHub에서 새 저장소를 만듭니다. 비공개여도 됩니다.
2. 이 폴더를 저장소에 올립니다.

```bash
git init -b main
git add .
git commit -m "Add Android WebView app and GitHub Actions build"
git remote add origin https://github.com/USER/REPO.git
git push -u origin main
```

3. GitHub 저장소의 **Actions** 탭에서 `Build APK` 워크플로가 끝날 때까지 기다립니다.
4. 성공한 실행을 연 뒤 **Artifacts**에서 `PhotoEditor-apk`를 받습니다.
   - `PhotoEditor-debug.apk`: 바로 설치해서 쓰는 용도
   - `PhotoEditor-release.apk`: 같은 서명으로 만든 릴리스 빌드
5. 휴대폰에서 **알 수 없는 출처** 설치를 허용한 뒤 APK를 설치합니다.

Actions 탭의 **Run workflow**로 언제든 다시 빌드할 수 있습니다.

## 아이콘

원본 이미지는 `art/`에 있습니다. 아이콘을 바꾼 뒤에는 아래 명령으로 런처 아이콘을 다시 만들 수 있습니다.

```bash
py -3 scripts/generate_icons.py
```
