#!/usr/bin/env python3
"""Generate the 4-language Tenra landing pages (/, /en/, /ja/, /ko/).

Usage:  python3 tool/gen.py [path/to/filmstocks.json]
Run from the repo root. Edit STRINGS below, re-run, commit the output.
"""
import json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
STOCKS_JSON = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "tool" / "filmstocks.json"

LANGS = ["zh", "en", "ja", "ko"]
HTML_LANG = {"zh": "zh-Hant", "en": "en", "ja": "ja", "ko": "ko"}
OUT_DIR = {"zh": ROOT, "en": ROOT / "en", "ja": ROOT / "ja", "ko": ROOT / "ko"}
URL = {"zh": "https://moooo-works.github.io/", "en": "https://moooo-works.github.io/en/",
       "ja": "https://moooo-works.github.io/ja/", "ko": "https://moooo-works.github.io/ko/"}
SHOT_DIR = {"zh": "/assets/tenra", "en": "/assets/tenra/en", "ja": "/assets/tenra/ja", "ko": "/assets/tenra/ko"}
OG_LOCALE = {"zh": "zh_TW", "en": "en_US", "ja": "ja_JP", "ko": "ko_KR"}

SWITCHER = [("zh", "繁體中文"), ("en", "English"), ("ja", "日本語"), ("ko", "한국어")]

STRINGS = {
"zh": {
  "title": "Tenra — 底片相機與暗房 | Film Camera & Darkroom",
  "desc": "Tenra 是手機裡的底片相機與暗房。{count} 款經典底片色調，包含 Ektachrome E100 與正片負沖，還能重曝、選擇齒孔片邊。拍完一捲，等待沖洗後揭曉。iOS 與 Android 皆已上架。",
  "og_title": "Tenra — 底片相機與暗房",
  "og_desc": "{count} 款底片，包含 Ektachrome E100 與正片負沖。裝片、拍攝、等待沖洗，讓照片值得期待。",
  "tagline": "裝一捲底片，拍完 36 張，等它沖洗——<br>照片值得等待。",
  "tagline_sub": "A real film experience, in your pocket.",
  "strip_label": "App 畫面截圖",
  "captions": ["裝片", "拍攝", "沖洗", "揭曉", "成品"],
  "alts": ["裝片畫面：選擇底片並裝入相機", "拍攝畫面：底片相機觀景窗", "沖洗等待畫面",
           "揭曉畫面：整捲照片一次呈現", "成品照片：底片色調與顆粒"],
  "how_h2": "不是濾鏡，是一捲底片",
  "how_lede": "拍立得看、隨拍隨刪的年代，Tenra 把「等待」還給攝影。每一捲有 36 張的額度、鎖定的底片與畫幅——按下快門之後，得等沖洗完成才見得到照片。",
  "steps": [
    ("裝片", "挑一支底片、選好畫幅比例。裝上之後整捲鎖定，就跟真的底片一樣。"),
    ("拍攝", "36 張的額度讓每次快門都算數。拍壞的那格也不會退回——底片不重來。"),
    ("沖洗", "選擇立即、一小時或隔天沖洗。等待的期間，照片在暗房裡慢慢成形。"),
    ("揭曉", "整捲一次揭曉。光暈、顆粒、偶爾的漏光——每一捲都是一份小驚喜。"),
  ],
  "stocks_h2": "{count} 款底片，{count} 種個性",
  "stocks_lede": "參考經典底片的實拍色彩調製，結合色調、光暈與顆粒，呈現各自的影像個性。標示 PRO 的底片需使用 Tenra Pro 送洗。",
  "cta_h2": "準備好裝上第一捲了嗎？",
  "cta_lede": "免費下載，內建三支底片。iOS 與 Android 皆已上架。",
  "appstore_aria": "於 App Store 下載 Tenra", "play_aria": "於 Google Play 下載 Tenra",
  "f_support": "支援 Support", "f_privacy": "隱私權政策 Privacy", "f_terms": "使用條款 Terms",
  "trademark": "Kodak、Ilford、Fujifilm、CineStill 為其各自所有者之商標。Tenra 為獨立開發作品，與上述品牌無關。",
  "process_h2": "同一支 E100，兩種沖法",
  "process_lede": "拍完再決定。送洗 E100 時，選擇標準沖洗或正片負沖；兩種方式都使用 Tenra Pro 送洗。",
  "process_cards": [["E100 · 標準", "自然膚色、清亮色彩，保留細緻通透的正片感。適合想留下現場光線與色彩的那一捲。"], ["E100 · 正片負沖", "暗部偏紫、天空偏青綠，亮部帶黃綠，膚色也會跟著改變。不同照片會呈現不同程度的偏色，讓同一支底片多一種脾氣。"]],
  "process_note": "樣片與匯入預覽顯示標準發色。送洗開始後，整捲沖法即鎖定；沖洗失敗重試也沿用原本的選擇。",
  "features_h2": "一捲底片，也有自己的玩法",
  "features_lede": "從按下快門到找回舊照片，讓拍一捲的每一步更順手。",
  "features": [["重曝，不過片", "拍完一格後撥起不過片撥桿，下一次快門就疊在同一格，張數不增加。想再疊一次，就再撥一次；也可開啟殘影輔助構圖。"], ["齒孔片邊", "裝片時選好片邊樣式，讓齒孔與底片邊緣成為照片的一部分。畫幅與片邊設定會沿用整捲。"], ["底片庫搜尋", "捲名、底片名稱，或「正片負沖」都能找。底片越拍越多，也能找回想看的那一捲。"]],
  "volume_title": "音量鍵快門 · 1.6.1 即將推出",
  "volume_desc": "在相機裡，音量加、減放開各拍一張，長按不連拍，也能用來重曝。Android 支援；iPhone 需 iOS 17.2 以上，較舊系統仍可使用畫面快門。",
  "support_link": "查看使用說明與常見問題",
},
"en": {
  "title": "Tenra — Film Camera & Darkroom",
  "desc": "A film camera and darkroom in your phone. {count} classic film looks, including Ektachrome E100 with optional cross-processing, plus multiple exposures and sprocket borders. Shoot a roll, wait, then reveal. Available on iOS and Android.",
  "og_title": "Tenra — Film Camera & Darkroom",
  "og_desc": "{count} film looks, including Ektachrome E100 and cross-processing. Load, shoot, wait, and reveal your roll.",
  "tagline": "Load a roll, shoot 36 frames,<br>wait for the develop.",
  "tagline_sub": "A real film experience, in your pocket.",
  "strip_label": "App screenshots",
  "captions": ["Load", "Shoot", "Develop", "Reveal", "The frame"],
  "alts": ["Load screen: choosing a film stock", "Shooting screen: film camera viewfinder", "Develop wait screen",
           "Reveal screen: the whole roll at once", "A finished frame: film color and grain"],
  "how_h2": "Not a filter. A roll of film.",
  "how_lede": "In an age of shoot-and-delete, Tenra gives photography its waiting back. Every roll has 36 frames, a locked film stock and aspect ratio — after the shutter clicks, you won't see the photo until the roll is developed.",
  "steps": [
    ("Load", "Pick a film stock and an aspect ratio. Once loaded, the roll is locked in — just like real film."),
    ("Shoot", "36 frames make every shutter count. Botched frames don't come back — film doesn't do retakes."),
    ("Develop", "Develop instantly, in an hour, or overnight. While you wait, the photos take shape in the darkroom."),
    ("Reveal", "The whole roll is revealed at once. Halation, grain, the occasional light leak — every roll is a small surprise."),
  ],
  "stocks_h2": "{count} film stocks, {count} personalities",
  "stocks_lede": "Color tuned with reference to real film photographs, combined with halation and grain to give each stock its own character. Stocks marked PRO require Tenra Pro for development.",
  "cta_h2": "Ready to load your first roll?",
  "cta_lede": "Free to download, three film stocks included. Available on iOS and Android.",
  "appstore_aria": "Download Tenra on the App Store", "play_aria": "Get Tenra on Google Play",
  "f_support": "Support", "f_privacy": "Privacy Policy", "f_terms": "Terms of Use",
  "trademark": "Kodak, Ilford, Fujifilm and CineStill are trademarks of their respective owners. Tenra is an independent app, not affiliated with any of these brands.",
  "process_h2": "One E100, two ways to develop",
  "process_lede": "Decide after shooting. Choose standard development or cross-processing when sending your E100 roll to the darkroom. Both options require Tenra Pro.",
  "process_cards": [["E100 · Standard", "Natural skin tones, luminous color, and fine slide-film detail. For a roll that keeps the light and color of the scene."], ["E100 · Cross-process", "Purple shadows, teal skies, and yellow-green highlights — skin tones shift too. The strength of the color shift varies with the photo, giving the same stock a different character."]],
  "process_note": "Samples and import previews show the standard look. Your choice applies to the whole roll and locks when development starts, including retries after a failed development.",
  "features_h2": "Make each roll your own",
  "features_lede": "From taking the shot to finding an old favorite, a few more ways to enjoy your roll.",
  "features": [["Multiple exposures", "Flip the no-advance lever after a shot to expose the same frame again without using another frame. Flip it again for each extra exposure, and use the ghost overlay to help compose."], ["Sprocket borders", "Choose a border style when loading film to bring sprocket holes and film edges into the finished image. The aspect ratio and border settings stay with the whole roll."], ["Search your library", "Find rolls by title, film name, or the cross-process label. More rolls to enjoy, less searching through them one by one."]],
  "volume_title": "Volume-button shutter · Coming in 1.6.1",
  "volume_desc": "In the camera, release either volume button to take one shot, including multiple exposures. Holding a button will not shoot a burst. Supported on Android and iOS 17.2 or later; older iOS versions keep the on-screen shutter.",
  "support_link": "Read the guide and frequently asked questions",
},
"ja": {
  "title": "Tenra — フィルムカメラと暗室",
  "desc": "スマホの中のフィルムカメラと暗室。Ektachrome E100 とクロスプロセスを含む {count} 種類のフィルムの色調に、多重露光とパーフォレーション付きのフィルム枠。撮り終えたら現像を待って、一枚ずつ楽しむ。iOS / Android で配信中。",
  "og_title": "Tenra — フィルムカメラと暗室",
  "og_desc": "Ektachrome E100 とクロスプロセスを含む{count}種類のフィルム。装填して、撮って、現像を待つ楽しみを。",
  "tagline": "フィルムを装填して、36枚撮りきって、<br>現像を待つ。",
  "tagline_sub": "A real film experience, in your pocket.",
  "strip_label": "アプリのスクリーンショット",
  "captions": ["装填", "撮影", "現像", "現像上がり", "仕上がり"],
  "alts": ["装填画面：フィルムを選んで装填", "撮影画面：フィルムカメラのファインダー", "現像待ち画面",
           "現像上がり画面：1本まるごと一気に表示", "仕上がった1枚：フィルムの色と粒子"],
  "how_h2": "フィルターじゃない、一本のフィルム。",
  "how_lede": "撮っては消せる時代に、Tenra は写真に「待つ時間」を取り戻します。1本のロールは36枚。フィルムと画角は装填時に固定——シャッターを切ったら、現像が終わるまで写真は見られません。",
  "steps": [
    ("装填", "フィルムと画角を選んで装填。装填したら1本まるごとロック、本物のフィルムと同じです。"),
    ("撮影", "36枚だからこそ、1枚1枚が真剣勝負。失敗したコマも戻ってきません——フィルムにやり直しはなし。"),
    ("現像", "すぐ現像、1時間後、または翌日。待っている間、写真は暗室の中でゆっくり形になります。"),
    ("現像上がり", "1本まるごと一気にご対面。ハレーション、粒子、ときどき光漏れ——どのロールも小さなサプライズ。"),
  ],
  "stocks_h2": "{count}本のフィルム、{count}つの個性",
  "stocks_lede": "実際のフィルム写真の色を参考に調整し、ハレーションや粒子と組み合わせて、それぞれの個性を表現しました。PRO 表示のフィルムの現像には Tenra Pro が必要です。",
  "cta_h2": "最初の1本、装填してみませんか？",
  "cta_lede": "ダウンロード無料、フィルム3本入り。iOS / Android で配信中。",
  "appstore_aria": "App Store で Tenra をダウンロード", "play_aria": "Google Play で Tenra を入手",
  "f_support": "サポート", "f_privacy": "プライバシーポリシー", "f_terms": "利用規約",
  "trademark": "Kodak、Ilford、Fujifilm、CineStill は各社の商標です。Tenra は独立した個人開発アプリであり、上記ブランドとは関係ありません。",
  "process_h2": "同じ E100 に、ふたつの現像",
  "process_lede": "撮り終えてから選べます。E100 を現像に出すときに、標準現像かクロスプロセスを選択。どちらも Tenra Pro が必要です。",
  "process_cards": [["E100 · 標準現像", "自然な肌色と澄んだ発色、きめ細かなリバーサルの質感。その場の光や色を残したい一本に。"], ["E100 · クロスプロセス", "紫がかった暗部、青緑の空、黄緑を帯びたハイライト。肌色も変化します。写真によって色の変わり方が異なり、同じフィルムに別の表情が生まれます。"]],
  "process_note": "サンプルと読み込み時のプレビューは標準現像の色です。選んだ現像方法は一本全体に適用され、現像開始後は変更できません。失敗時の再試行でも同じ方法を使います。",
  "features_h2": "一本のフィルムに、自分らしい楽しみ方を",
  "features_lede": "シャッターを切るときも、昔の写真を探すときも。フィルムを楽しむ機能を揃えました。",
  "features": [["多重露光", "撮影後に MX レバーを入れると、次の露光を同じコマに重ねられます。残り枚数は減りません。重ねるたびにレバーを入れ直し、残像表示で構図を合わせることもできます。"], ["フィルムの縁とパーフォレーション", "装填時に枠のスタイルを選び、フィルムの縁や送り穴を写真の一部に。画角と枠の設定は一本を通して固定されます。"], ["ライブラリ検索", "ロール名、フィルム名、クロスプロセスの表示で検索。ロールが増えても、お気に入りの一本を見つけられます。"]],
  "volume_title": "音量ボタンで撮影 · 1.6.1 で近日対応",
  "volume_desc": "カメラ画面では音量ボタンの上下どちらも、離すと一枚撮影。長押しで連写はせず、多重露光にも使えます。Android と iOS 17.2 以降に対応予定。それ以前の iOS では画面のシャッターを使えます。",
  "support_link": "使い方とよくある質問",
},
"ko": {
  "title": "Tenra — 필름 카메라와 암실",
  "desc": "폰 속의 필름 카메라와 암실. Ektachrome E100과 크로스 프로세스를 포함한 필름 {count}종의 색감, 다중 노출과 필름 테두리까지. 한 롤을 촬영하고 현상을 기다린 뒤 사진을 만나세요. iOS와 Android 모두 출시.",
  "og_title": "Tenra — 필름 카메라와 암실",
  "og_desc": "Ektachrome E100과 크로스 프로세스를 포함한 필름 {count}종. 장전하고, 촬영하고, 현상을 기다리는 즐거움.",
  "tagline": "필름 한 롤을 장전하고, 36장을 다 찍고,<br>현상을 기다리세요.",
  "tagline_sub": "A real film experience, in your pocket.",
  "strip_label": "앱 스크린샷",
  "captions": ["장전", "촬영", "현상", "공개", "결과물"],
  "alts": ["장전 화면: 필름 고르기", "촬영 화면: 필름 카메라 뷰파인더", "현상 대기 화면",
           "공개 화면: 롤 전체를 한 번에", "완성된 한 장: 필름 색감과 그레인"],
  "how_h2": "필터가 아니라, 필름 한 롤.",
  "how_lede": "찍고 바로 지우는 시대에, Tenra는 사진에 '기다림'을 돌려줍니다. 한 롤은 36장, 필름과 화면 비율은 장전 시 고정 — 셔터를 누른 뒤에는 현상이 끝나야 사진을 볼 수 있습니다.",
  "steps": [
    ("장전", "필름과 화면 비율을 골라 장전하세요. 장전하면 롤 전체가 고정 — 진짜 필름처럼."),
    ("촬영", "36장이기에 셔터 한 번 한 번이 소중합니다. 망친 컷도 돌아오지 않아요 — 필름은 다시 찍기가 없으니까."),
    ("현상", "즉시, 1시간 후, 또는 다음 날 현상. 기다리는 동안 사진은 암실에서 천천히 완성됩니다."),
    ("공개", "롤 전체가 한 번에 공개됩니다. 헐레이션, 그레인, 가끔의 빛샘 — 모든 롤이 작은 서프라이즈."),
  ],
  "stocks_h2": "{count}가지 필름, {count}가지 개성",
  "stocks_lede": "실제 필름 사진의 색감을 참고해 조정하고 헐레이션과 그레인을 더해 각 필름의 개성을 표현했습니다. PRO 표시 필름의 현상에는 Tenra Pro가 필요합니다.",
  "cta_h2": "첫 번째 롤, 장전할 준비되셨나요?",
  "cta_lede": "무료 다운로드, 필름 3종 기본 제공. iOS와 Android 모두 출시.",
  "appstore_aria": "App Store에서 Tenra 다운로드", "play_aria": "Google Play에서 Tenra 받기",
  "f_support": "지원", "f_privacy": "개인정보처리방침", "f_terms": "이용약관",
  "trademark": "Kodak, Ilford, Fujifilm, CineStill은 각 소유자의 상표입니다. Tenra는 독립 개발 앱으로 위 브랜드와 무관합니다.",
  "process_h2": "같은 E100, 두 가지 현상",
  "process_lede": "촬영을 마친 뒤 결정하세요. E100을 현상할 때 표준 현상과 크로스 프로세스 중에서 선택할 수 있습니다. 두 방식 모두 Tenra Pro가 필요합니다.",
  "process_cards": [["E100 · 표준 현상", "자연스러운 피부톤과 맑은 색감, 섬세한 슬라이드 필름의 질감. 현장의 빛과 색을 간직하고 싶은 롤에 어울립니다."], ["E100 · 크로스 프로세스", "보라색 그림자, 청록색 하늘, 황록색 하이라이트에 피부색도 달라집니다. 사진에 따라 색이 변하는 정도가 달라져 같은 필름에 또 다른 표정이 생깁니다."]],
  "process_note": "샘플과 가져오기 미리보기에는 표준 색감이 표시됩니다. 선택한 현상 방식은 롤 전체에 적용되며, 현상을 시작하면 바꿀 수 없습니다. 현상 실패 후 재시도할 때도 같은 방식을 유지합니다.",
  "features_h2": "한 롤을 나만의 방식으로",
  "features_lede": "셔터를 누르는 순간부터 예전 사진을 다시 찾을 때까지, 필름을 즐기는 방법을 더했습니다.",
  "features": [["다중 노출", "한 장을 찍고 필름 이송 방지 레버를 올리면 다음 노출이 같은 프레임에 겹쳐집니다. 남은 장수는 줄지 않습니다. 더 겹칠 때마다 레버를 다시 올리고, 잔상 표시로 구도를 맞출 수도 있습니다."], ["필름 테두리", "장전할 때 테두리 스타일을 선택해 필름 가장자리와 퍼포레이션을 사진에 담으세요. 화면 비율과 테두리 설정은 롤 전체에 유지됩니다."], ["라이브러리 검색", "롤 이름, 필름 이름, 크로스 프로세스 표시로 검색하세요. 롤이 쌓여도 다시 보고 싶은 한 롤을 찾을 수 있습니다."]],
  "volume_title": "볼륨 버튼 셔터 · 1.6.1에서 곧 제공",
  "volume_desc": "카메라에서 볼륨 위·아래 버튼을 놓으면 한 장을 촬영하며 다중 노출도 가능합니다. 길게 눌러도 연사하지 않습니다. Android와 iOS 17.2 이상에서 지원 예정이며, 이전 iOS에서는 화면 셔터를 사용할 수 있습니다.",
  "support_link": "사용법과 자주 묻는 질문",
},
}

SHOTS = ["01_01_load_film", "02_02_capture_roll", "03_03_develop_wait", "04_04_reveal_roll", "05_05_final_frame"]

APPLE_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>'
PLAY_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 20.5v-17c0-.59.34-1.11.84-1.35L13.69 12l-9.85 9.85c-.5-.25-.84-.76-.84-1.35m13.81-5.38L6.05 21.34l8.49-8.49 2.27 2.27m3.35-4.31c.34.27.59.69.59 1.19s-.22.9-.57 1.18l-2.29 1.32-2.5-2.5 2.5-2.5 2.27 1.31M6.05 2.66l10.76 6.22-2.27 2.27-8.49-8.49z"/></svg>'

CSS = """
:root{
  --bg:#0f0c09;
  --bg-2:#171310;
  --card:#1d1814;
  --line:#332a22;
  --amber:#e8a33d;
  --amber-dim:#b97f2c;
  --ink:#f2e9dc;
  --ink-dim:#b0a494;
  --radius:14px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important;animation:none!important}}
body{
  background:var(--bg);
  color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Noto Sans TC","Hiragino Kaku Gothic ProN","Apple SD Gothic Neo","Microsoft JhengHei",sans-serif;
  line-height:1.7;
  -webkit-font-smoothing:antialiased;
}
a{color:var(--amber);text-decoration:none}
a:hover{text-decoration:underline}
a:focus-visible,button:focus-visible{outline:2px solid var(--amber);outline-offset:3px;border-radius:4px}
.wrap{max-width:1060px;margin:0 auto;padding:0 24px}
.langs{display:flex;gap:18px;justify-content:center;padding:18px 24px 0;font-size:.85rem}
.langs a{color:var(--ink-dim)}
.langs a:hover{color:var(--amber)}
.langs .cur{color:var(--amber);font-weight:600}
.perf{
  height:26px;
  background:
    repeating-linear-gradient(90deg,
      transparent 0 14px,
      var(--bg-2) 14px 24px,
      transparent 24px 38px);
  background-color:#000;
  border-top:1px solid var(--line);
  border-bottom:1px solid var(--line);
}
header{padding:44px 0 56px;text-align:center;background:radial-gradient(ellipse 80% 60% at 50% -10%,#2a1f12 0%,var(--bg) 70%)}
.icon{width:96px;height:96px;border-radius:22px;box-shadow:0 8px 40px rgba(232,163,61,.25)}
h1{font-size:clamp(2.4rem,6vw,3.6rem);letter-spacing:.08em;margin:20px 0 4px;font-weight:700}
.sub{color:var(--amber);font-size:.95rem;letter-spacing:.35em;text-transform:uppercase}
.tagline{font-size:clamp(1.1rem,2.6vw,1.4rem);margin:26px auto 8px;max-width:34em;color:var(--ink)}
.tagline-en{color:var(--ink-dim);font-size:.95rem;margin-bottom:34px}
.badges{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.badge{
  display:inline-flex;align-items:center;gap:10px;
  background:#000;border:1px solid var(--line);border-radius:12px;
  padding:12px 22px;min-height:52px;color:var(--ink);cursor:pointer;
  transition:border-color .2s,box-shadow .2s;
}
.badge:hover{border-color:var(--amber);box-shadow:0 0 24px rgba(232,163,61,.18);text-decoration:none}
.badge svg{width:26px;height:26px;flex:none}
.badge small{display:block;font-size:.68rem;color:var(--ink-dim);line-height:1.2;text-align:left}
.badge b{font-size:1rem;line-height:1.25;display:block;text-align:left}
section{padding:72px 0}
section:nth-of-type(even){background:var(--bg-2)}
h2{font-size:clamp(1.5rem,3.6vw,2rem);margin-bottom:8px;text-align:center}
.lede{color:var(--ink-dim);text-align:center;max-width:38em;margin:0 auto 44px}
.strip{
  display:flex;gap:20px;overflow-x:auto;padding:26px 24px;
  background:#000;border-top:1px solid var(--line);border-bottom:1px solid var(--line);
  scroll-snap-type:x mandatory;
}
.strip figure{flex:0 0 auto;scroll-snap-align:center;text-align:center}
.strip img{
  width:min(240px,64vw);border-radius:6px;display:block;
  border:1px solid var(--line);
}
.strip figcaption{margin-top:12px;font-size:.85rem;color:var(--ink-dim)}
.strip figcaption b{color:var(--amber);font-weight:600;margin-right:.5em}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:18px}
.step{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:24px}
.step .no{color:var(--amber);font-size:.8rem;letter-spacing:.2em}
.step h3{margin:6px 0 8px;font-size:1.1rem}
.step p{color:var(--ink-dim);font-size:.92rem}
.stocks{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px}
.stock{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;transition:border-color .2s}
.stock:hover{border-color:var(--amber-dim)}
.stock .meta{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.stock h3{font-size:1.02rem;font-weight:600}
.stock .iso{color:var(--ink-dim);font-size:.78rem;letter-spacing:.08em;flex:none}
.stock p{color:var(--ink-dim);font-size:.9rem;margin-top:8px}
.stock .pro{display:inline-block;font-size:.66rem;color:var(--bg);background:var(--amber);border-radius:4px;padding:1px 7px;margin-left:8px;vertical-align:2px;letter-spacing:.05em}
.processes{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px}
.process{padding:28px;border:1px solid var(--line);border-radius:var(--radius);background:var(--card)}
.process h3{color:var(--amber);margin-bottom:12px}
.process p{color:var(--ink-dim)}
.process:last-child{border-color:#706077}
.process:last-child h3{color:#ceaad8}
.process-note{max-width:56em;margin:24px auto 0;text-align:center;color:var(--ink-dim);font-size:.9rem}
.release-note{margin-top:28px;padding:24px;border-left:3px solid var(--amber);background:var(--card);border-radius:0 var(--radius) var(--radius) 0}
.release-note h3{font-size:1.05rem;margin-bottom:8px}
.release-note p{color:var(--ink-dim);margin-bottom:12px}
footer{padding:56px 0 64px;text-align:center;border-top:1px solid var(--line)}
footer .links{display:flex;gap:26px;justify-content:center;flex-wrap:wrap;margin-bottom:18px}
footer .links a{color:var(--ink-dim)}
footer .links a:hover{color:var(--amber)}
footer p{color:var(--ink-dim);font-size:.85rem}
"""


def badges(t):
    return f'''<div class="badges">
      <a class="badge" href="https://apps.apple.com/app/id6787303638" aria-label="{t['appstore_aria']}">
        {APPLE_SVG}
        <span><small>Download on the</small><b>App Store</b></span>
      </a>
      <a class="badge" href="https://play.google.com/store/apps/details?id=com.mooooworks.tenra" aria-label="{t['play_aria']}">
        {PLAY_SVG}
        <span><small>GET IT ON</small><b>Google Play</b></span>
      </a>
    </div>'''


def hreflang():
    lines = [f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{URL[l]}">' for l in LANGS]
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{URL["zh"]}">')
    return "\n".join(lines)


def switcher(cur):
    parts = []
    for l, label in SWITCHER:
        if l == cur:
            parts.append(f'<span class="cur" aria-current="true">{label}</span>')
        else:
            parts.append(f'<a href="{URL[l].replace("https://moooo-works.github.io", "")}">{label}</a>')
    return '<nav class="langs" aria-label="Language">' + "\n    ".join(parts) + '</nav>'


def stock_cards(stocks, lang):
    cards = []
    for s in sorted(stocks, key=lambda x: x["sortOrder"]):
        p = s["personality"][lang if lang != "zh" else "zh"]
        if lang == "zh":
            p = p.replace(",", "，").replace(" — ", "——")
        pro = '<span class="pro">PRO</span>' if s["isPremium"] else ""
        cards.append(
            f'      <div class="stock"><div class="meta"><h3>{s["displayName"]}{pro}</h3>'
            f'<span class="iso">ISO {s["iso"]}</span></div><p>{p}</p></div>')
    return "\n".join(cards)


def strip(t, lang):
    figs = []
    for i, name in enumerate(SHOTS):
        figs.append(
            f'  <figure><img src="{SHOT_DIR[lang]}/{name}.jpg" alt="{t["alts"][i]}" loading="lazy" width="240">'
            f'<figcaption><b>0{i+1}</b>{t["captions"][i]}</figcaption></figure>')
    return "\n".join(figs)


def steps(t):
    out = []
    for i, (h, p) in enumerate(t["steps"]):
        out.append(f'      <div class="step"><p class="no">STEP 0{i+1}</p><h3>{h}</h3><p>{p}</p></div>')
    return "\n".join(out)


def feature_cards(items, css_class):
    return "\n".join(
        f'      <div class="{css_class}"><h3>{heading}</h3><p>{body}</p></div>'
        for heading, body in items
    )


def page(lang, stocks):
    t = dict(STRINGS[lang])
    for key in ("desc", "og_desc", "stocks_h2"):
        t[key] = t[key].format(count=len(stocks))
    anchor = f'#{lang}'
    return f'''<!DOCTYPE html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<link rel="canonical" href="{URL[lang]}">
{hreflang()}
<link rel="icon" type="image/png" href="/assets/tenra/icon-192.png">
<meta property="og:title" content="{t["og_title"]}">
<meta property="og:description" content="{t["og_desc"]}">
<meta property="og:image" content="https://moooo-works.github.io{SHOT_DIR[lang]}/04_04_reveal_roll.jpg">
<meta property="og:url" content="{URL[lang]}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<style>{CSS}</style>
</head>
<body>

{switcher(lang)}

<header>
  <div class="wrap">
    <img class="icon" src="/assets/tenra/icon-192.png" alt="Tenra" width="96" height="96">
    <p class="sub">Film Camera &amp; Darkroom</p>
    <h1>Tenra</h1>
    <p class="tagline">{t["tagline"]}</p>
    <p class="tagline-en">{t["tagline_sub"]}</p>
    {badges(t)}
  </div>
</header>

<div class="perf" role="presentation"></div>

<div class="strip" aria-label="{t["strip_label"]}">
{strip(t, lang)}
</div>

<div class="perf" role="presentation"></div>

<section>
  <div class="wrap">
    <h2>{t["how_h2"]}</h2>
    <p class="lede">{t["how_lede"]}</p>
    <div class="steps">
{steps(t)}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>{t["stocks_h2"]}</h2>
    <p class="lede">{t["stocks_lede"]}</p>
    <div class="stocks">
{stock_cards(stocks, lang)}
    </div>
  </div>
</section>

<section id="e100-process">
  <div class="wrap">
    <h2>{t["process_h2"]}</h2>
    <p class="lede">{t["process_lede"]}</p>
    <div class="processes">
{feature_cards(t["process_cards"], "process")}
    </div>
    <p class="process-note">{t["process_note"]}</p>
  </div>
</section>

<section id="features">
  <div class="wrap">
    <h2>{t["features_h2"]}</h2>
    <p class="lede">{t["features_lede"]}</p>
    <div class="steps">
{feature_cards(t["features"], "step")}
    </div>
    <div class="release-note">
      <h3>{t["volume_title"]}</h3>
      <p>{t["volume_desc"]}</p>
      <a href="/tenra-support#{lang}">{t["support_link"]}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>{t["cta_h2"]}</h2>
    <p class="lede">{t["cta_lede"]}</p>
    {badges(t)}
  </div>
</section>

<div class="perf" role="presentation"></div>

<footer>
  <div class="wrap">
    <div class="links">
      <a href="/tenra-support">{t["f_support"]}</a>
      <a href="/tenra-privacy{anchor}">{t["f_privacy"]}</a>
      <a href="/tenra-terms{anchor}">{t["f_terms"]}</a>
    </div>
    <p>© 2026 moooo_works · <a href="mailto:moooo.works@gmail.com">moooo.works@gmail.com</a></p>
    <p style="margin-top:6px;font-size:.75rem">{t["trademark"]}</p>
  </div>
</footer>

</body>
</html>
'''


def main():
    stocks = json.loads(STOCKS_JSON.read_text())["filmStocks"]
    for lang in LANGS:
        OUT_DIR[lang].mkdir(exist_ok=True)
        out = OUT_DIR[lang] / "index.html"
        out.write_text(page(lang, stocks))
        print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
