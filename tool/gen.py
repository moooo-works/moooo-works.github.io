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
  "desc": "Tenra 是一台裝在手機裡的底片相機：裝一捲底片、拍完 36 張、等待沖洗，才看得到照片。八款經典底片色調，附光暈、顆粒與漏光。iOS 與 Android 皆已上架。",
  "og_title": "Tenra — 底片相機與暗房",
  "og_desc": "裝一捲底片，拍完 36 張，等它沖洗。手機裡的真實底片體驗。",
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
  "stocks_h2": "八支底片，八種個性",
  "stocks_lede": "色調靈感取自經典底片，以 3D LUT 忠實重現——不是套個濾鏡，而是整條顯影管線：色彩、光暈、銀鹽顆粒。",
  "cta_h2": "準備好裝上第一捲了嗎？",
  "cta_lede": "免費下載，內建三支底片。iOS 與 Android 皆已上架。",
  "appstore_aria": "於 App Store 下載 Tenra", "play_aria": "於 Google Play 下載 Tenra",
  "f_support": "支援 Support", "f_privacy": "隱私權政策 Privacy", "f_terms": "使用條款 Terms",
  "trademark": "Kodak、Ilford、Fujifilm、CineStill 為其各自所有者之商標。Tenra 為獨立開發作品，與上述品牌無關。",
},
"en": {
  "title": "Tenra — Film Camera & Darkroom",
  "desc": "Tenra is a film camera that lives in your phone: load a roll, shoot 36 frames, and wait for the develop before you see a single photo. Eight classic film stocks with halation, grain and light leaks. On iOS and Android.",
  "og_title": "Tenra — Film Camera & Darkroom",
  "og_desc": "Load a roll, shoot 36 frames, wait for the develop. A real film experience, in your pocket.",
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
  "stocks_h2": "Eight film stocks, eight personalities",
  "stocks_lede": "Color inspired by classic film stocks, faithfully rebuilt as 3D LUTs — not a filter slapped on top, but a full develop pipeline: color, halation, silver-halide grain.",
  "cta_h2": "Ready to load your first roll?",
  "cta_lede": "Free to download, three film stocks included. Available on iOS and Android.",
  "appstore_aria": "Download Tenra on the App Store", "play_aria": "Get Tenra on Google Play",
  "f_support": "Support", "f_privacy": "Privacy Policy", "f_terms": "Terms of Use",
  "trademark": "Kodak, Ilford, Fujifilm and CineStill are trademarks of their respective owners. Tenra is an independent app, not affiliated with any of these brands.",
},
"ja": {
  "title": "Tenra — フィルムカメラと暗室",
  "desc": "Tenra はスマホの中のフィルムカメラ。フィルムを装填し、36枚撮りきって、現像を待つまで写真は見られません。クラシックフィルム8本の色調に、ハレーション・粒子・光漏れ。iOS / Android で配信中。",
  "og_title": "Tenra — フィルムカメラと暗室",
  "og_desc": "フィルムを装填して、36枚撮りきって、現像を待つ。ポケットの中の本物のフィルム体験。",
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
  "stocks_h2": "8本のフィルム、8つの個性",
  "stocks_lede": "クラシックフィルムに着想を得た色を、3D LUT で忠実に再現。上から被せるフィルターではなく、色・ハレーション・銀塩粒子まで含めた現像パイプラインです。",
  "cta_h2": "最初の1本、装填してみませんか？",
  "cta_lede": "ダウンロード無料、フィルム3本入り。iOS / Android で配信中。",
  "appstore_aria": "App Store で Tenra をダウンロード", "play_aria": "Google Play で Tenra を入手",
  "f_support": "サポート", "f_privacy": "プライバシーポリシー", "f_terms": "利用規約",
  "trademark": "Kodak、Ilford、Fujifilm、CineStill は各社の商標です。Tenra は独立した個人開発アプリであり、上記ブランドとは関係ありません。",
},
"ko": {
  "title": "Tenra — 필름 카메라와 암실",
  "desc": "Tenra는 폰 속의 필름 카메라입니다. 필름 한 롤을 장전하고, 36장을 다 찍고, 현상이 끝나야 사진을 볼 수 있습니다. 클래식 필름 8종의 색감에 헐레이션·그레인·빛샘까지. iOS와 Android 모두 출시.",
  "og_title": "Tenra — 필름 카메라와 암실",
  "og_desc": "필름 한 롤을 장전하고, 36장을 다 찍고, 현상을 기다리세요. 주머니 속 진짜 필름 경험.",
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
  "stocks_h2": "여덟 가지 필름, 여덟 가지 개성",
  "stocks_lede": "클래식 필름에서 영감을 받은 색을 3D LUT로 충실히 재현 — 위에 씌우는 필터가 아니라 색, 헐레이션, 은염 그레인까지 아우르는 현상 파이프라인입니다.",
  "cta_h2": "첫 번째 롤, 장전할 준비되셨나요?",
  "cta_lede": "무료 다운로드, 필름 3종 기본 제공. iOS와 Android 모두 출시.",
  "appstore_aria": "App Store에서 Tenra 다운로드", "play_aria": "Google Play에서 Tenra 받기",
  "f_support": "지원", "f_privacy": "개인정보처리방침", "f_terms": "이용약관",
  "trademark": "Kodak, Ilford, Fujifilm, CineStill은 각 소유자의 상표입니다. Tenra는 독립 개발 앱으로 위 브랜드와 무관합니다.",
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


def page(lang, stocks):
    t = STRINGS[lang]
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
