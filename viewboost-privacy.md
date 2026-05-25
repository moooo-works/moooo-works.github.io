---
layout: default
title: ViewBoost Privacy Policy
---

# Privacy Policy / 隱私權政策

**Last updated / 最後更新：2026-05-25**

---

## English

### Overview

ViewBoost ("the App") is developed by moooo_works. This policy explains what information we collect, how we use it, and your rights regarding that information.

### Information We Collect

| Data | Purpose |
|---|---|
| Email address | Account identification via Google Sign-In |
| Points balance | Core reward mechanic — tracking earned and spent points |
| Watch history | Recording completed video views to prevent duplicate rewards |
| Subscription status | Determining VIP plan benefits |
| Ad reward timestamps | Enforcing cooldown period between ad rewards |
| Video campaign data | Storing promotion tasks created by you |
| Referral code & invitee link | Tracking referral relationships to distribute mutual rewards |
| Purchase tokens & SKU IDs | Server-side reconciliation of Google Play purchases to prevent duplicate point grants (stored in our `purchaseClaims` Cloud Functions collection) |
| Play Integrity / App Check token | Anti-abuse verification of device integrity; tokens are anonymous and do not contain personal information |

All data is stored in Google Firebase (Firestore) and is associated with your Google account UID.

### Information We Do NOT Collect

- We do not collect your name, phone number, or physical address.
- We do not collect precise GPS location data.
- We do not access your camera or microphone.
- Beyond Google's ad-serving infrastructure (described below), we do not share your data with other third-party advertisers or data brokers.

### Permissions Used

| Permission | Purpose |
|---|---|
| `INTERNET` | Core functionality — Firebase, AdMob, YouTube |
| `ACCESS_NETWORK_STATE` | Detect connectivity changes to gracefully handle offline state |
| `WAKE_LOCK` | Keep CPU awake while a watch task is in progress so timer accuracy is preserved |
| `com.android.vending.BILLING` | Process in-app purchases through Google Play |
| `SYSTEM_ALERT_WINDOW` | Display a floating HUD overlay (a countdown timer) on top of the YouTube app while a watch task is active. The overlay is only shown during an active task and is dismissed automatically when the task ends or is cancelled. |
| `BIND_NOTIFICATION_LISTENER_SERVICE` | See "YouTube Notification Listener" below |

### YouTube Notification Listener (important disclosure)

To detect whether you are actually watching a YouTube video during a watch task, the App registers a `NotificationListenerService`. We disclose the exact scope here:

- **Apps monitored**: Only the official YouTube family of packages and well-known YouTube mod clients —
  `com.google.android.youtube`, `com.google.android.apps.youtube.music`, `com.google.android.apps.youtube.kids`, `com.google.android.youtube.tv`, `com.google.android.apps.youtube.lite`, `com.google.android.apps.youtube.googletv`, `com.vanced.android.youtube`, `app.rvx.android.youtube`, `app.revanced.android.youtube`. Notifications from any other application are ignored.
- **Data read**: Only the source package name and the media playback state (playing / paused) reported by the standard Android `MediaSession`. We do **not** read notification titles, text, contacts, messages, or any other notification content.
- **Where it goes**: This data is used **only locally on your device** to decide whether to start or stop the countdown overlay. **No notification content is ever uploaded to our servers or shared with any third party.**

You may revoke this permission at any time in Android Settings → Notifications → Special app access → Notification access. The watch-task feature will stop working without it, but other features remain available.

### Third-Party Services

This App uses the following third-party services that may collect data per their own policies:

- **Firebase (Google)** — Authentication, Firestore database, Cloud Functions, Cloud Messaging (FCM), App Check / Play Integrity — [Google Privacy Policy](https://policies.google.com/privacy)
- **Firebase Crashlytics** — Automatically collects diagnostic data when the App crashes, including device model, OS version, App version, locale, anonymous installation ID, and the sequence of actions leading up to the crash. Used solely for stability improvements. — [Crashlytics data collection](https://firebase.google.com/support/privacy)
- **Google AdMob** — Rewarded and banner advertisements. AdMob may use the Android Advertising ID and device identifiers to serve personalized ads. — [Google Privacy Policy](https://policies.google.com/privacy) / [Ad personalization](https://support.google.com/ads/answer/2662922)
- **Google Play Billing** — In-app purchase processing — [Google Payments Privacy Notice](https://payments.google.com/payments/apis-secure/get_legal_document?ldo=0&ldt=privacynotice)
- **Android YouTube Player** — In-app YouTube video playback — [YouTube Terms of Service](https://www.youtube.com/t/terms)

### Advertising

This App displays ads served by Google AdMob, including rewarded video ads. AdMob may use device identifiers to serve personalized ads. You can opt out via your device's ad settings (Settings → Google → Ads → Reset / Delete advertising ID).

### In-App Purchases

Points and subscription plans can be purchased through Google Play Billing. Payment processing is handled entirely by Google — we do **not** store credit card or payment information. To prevent duplicate or fraudulent point grants, our Cloud Functions store the Google Play purchase token and SKU ID as a reconciliation record (in the `purchaseClaims` collection). These records do not contain payment instrument data.

### Data Retention

- **Active account data**: Retained in Firestore as long as your account exists.
- **Account deletion (in-app)**: Open the App → My / Settings → Delete Account (⚠ 刪除帳號). Your Firestore documents are removed immediately by a Cloud Function; backup snapshots may persist for up to 30 days before being permanently purged.
- **Account deletion (web — no install required)**: If you have already uninstalled the App, email `moooo.works@gmail.com` from the Google account associated with the App, with the subject "ViewBoost account deletion". We will confirm and process the deletion within 30 days.
- **Crashlytics diagnostics**: Retained for up to 90 days per Google's standard policy.
- **Purchase reconciliation records**: Retained for the lifetime of the account for billing dispute resolution.

### Your Rights (GDPR / CCPA)

If you reside in the EU/UK/EEA (GDPR) or California (CCPA), you have the right to access, correct, delete, port, or restrict the processing of your personal data. We do not sell personal information. To exercise any of these rights, email `moooo.works@gmail.com`.

### Children's Privacy

This App is not directed at children under 13 and does not knowingly collect data from children. If you believe a child has provided us with data, please contact us and we will delete it.

### Changes to This Policy

We may update this policy. Continued use of the App after changes constitutes acceptance. The "Last updated" date at the top of this page reflects the most recent revision.

### Contact

For questions or data requests, contact: **moooo.works@gmail.com**

---

## 繁體中文

### 概述

ViewBoost（以下簡稱「本應用程式」）由 moooo_works 開發。本政策說明我們收集哪些資訊、如何使用,以及您對這些資訊的相關權利。

### 我們收集的資料

| 資料 | 用途 |
|---|---|
| 電子信箱 | 透過 Google 登入進行帳號識別 |
| 點數餘額 | 核心獎勵機制 — 追蹤已賺取與已使用的點數 |
| 觀看紀錄 | 記錄已完成的影片觀看,防止重複領取獎勵 |
| 訂閱狀態 | 判斷 VIP 方案的相關福利 |
| 廣告獎勵時間戳記 | 執行廣告獎勵之間的冷卻期限制 |
| 影片推廣任務資料 | 儲存您建立的推廣任務 |
| 邀請碼與邀請關係 | 追蹤邀請人/被邀請人關係,以發放雙方獎勵 |
| Play 購買 token 與 SKU | 在 Cloud Functions（`purchaseClaims` 集合）儲存購買兌換紀錄,防止重複發點 |
| Play Integrity / App Check token | 反濫用驗證裝置完整性;token 為匿名,不含個人資訊 |

所有資料儲存於 Google Firebase（Firestore）,並與您的 Google 帳號 UID 關聯。

### 我們不收集的資料

- 我們不收集您的姓名、電話號碼或實體地址。
- 我們不收集精確的 GPS 位置資料。
- 我們不存取您的相機或麥克風。
- 除下方說明的 Google 廣告服務外,我們不會將您的資料分享給其他第三方廣告商或資料仲介。

### 使用的權限

| 權限 | 用途 |
|---|---|
| `INTERNET` | 核心功能 — Firebase、AdMob、YouTube |
| `ACCESS_NETWORK_STATE` | 偵測網路連線狀態變化,以妥善處理離線情境 |
| `WAKE_LOCK` | 觀看任務進行中保持 CPU 喚醒,確保計時準確 |
| `com.android.vending.BILLING` | 透過 Google Play 處理應用程式內購 |
| `SYSTEM_ALERT_WINDOW` | 在觀看任務進行時,於 YouTube App 上方顯示倒數計時懸浮視窗。該視窗僅在任務進行中顯示,任務結束或取消時自動關閉。 |
| `BIND_NOTIFICATION_LISTENER_SERVICE` | 參見下方「YouTube 通知監聽」 |

### YouTube 通知監聽（重要揭露）

為判斷您於觀看任務期間是否實際在收看 YouTube 影片,本應用程式註冊了 `NotificationListenerService`。揭露範圍如下：

- **監聽對象**：僅監聽 YouTube 系列官方套件與常見 mod 客戶端 —
  `com.google.android.youtube`、`com.google.android.apps.youtube.music`、`com.google.android.apps.youtube.kids`、`com.google.android.youtube.tv`、`com.google.android.apps.youtube.lite`、`com.google.android.apps.youtube.googletv`、`com.vanced.android.youtube`、`app.rvx.android.youtube`、`app.revanced.android.youtube`。其他應用程式的通知一律忽略。
- **讀取內容**：僅讀取「發出通知的套件名稱」與「Android `MediaSession` 回報的播放/暫停狀態」。**不讀取通知標題、內文、聯絡人、訊息或任何其他通知內容。**
- **資料流向**：上述資訊**僅在您的裝置上本地使用**,用於判斷是否啟動或停止倒數視窗。**任何通知內容都不會上傳至我們的伺服器,也不會分享給任何第三方。**

您可隨時於「設定 → 通知 → 特殊應用程式存取 → 通知存取權」撤銷此權限。撤銷後觀看任務功能將停用,但其他功能仍可正常使用。

### 第三方服務

本應用程式使用以下第三方服務,這些服務可能依其各自政策收集資料：

- **Firebase（Google）** — 身份驗證、Firestore 資料庫、Cloud Functions、Cloud Messaging（FCM）、App Check / Play Integrity — [Google 隱私權政策](https://policies.google.com/privacy?hl=zh-TW)
- **Firebase Crashlytics** — 當應用程式發生 crash 時自動收集診斷資料,包含裝置型號、作業系統版本、App 版本、語系、匿名安裝 ID、以及 crash 前的操作序列。僅用於穩定性改進。 — [Crashlytics 資料收集說明](https://firebase.google.com/support/privacy?hl=zh-tw)
- **Google AdMob** — 獎勵影片廣告及橫幅廣告。AdMob 可能使用 Android 廣告 ID 及裝置識別碼提供個人化廣告。 — [Google 隱私權政策](https://policies.google.com/privacy?hl=zh-TW) / [廣告個人化設定](https://support.google.com/ads/answer/2662922?hl=zh-TW)
- **Google Play Billing** — 應用程式內購處理 — [Google 付款隱私權聲明](https://payments.google.com/payments/apis-secure/get_legal_document?ldo=0&ldt=privacynotice)
- **Android YouTube Player** — 應用程式內 YouTube 影片播放 — [YouTube 服務條款](https://www.youtube.com/t/terms?hl=zh-TW)

### 廣告

本應用程式顯示由 Google AdMob 提供的廣告,包含獎勵影片廣告。AdMob 可能使用裝置識別碼提供個人化廣告。您可透過裝置廣告設定選擇退出（設定 → Google → 廣告 → 重設/刪除廣告 ID）。

### 應用程式內購

點數與訂閱方案可透過 Google Play Billing 購買。付款處理完全由 Google 負責,我們**不**儲存信用卡或付款資訊。為防止重複或詐騙性的點數發放,我們的 Cloud Functions 會將 Google Play 提供的購買 token 與商品 SKU 儲存為兌換紀錄（於 `purchaseClaims` 集合）。此紀錄不含任何付款工具資料。

### 資料保留

- **使用中帳號**：資料於 Firestore 保留至您刪除帳號為止。
- **App 內刪除帳號**：開啟 App → 我的 / 設定 → 刪除帳號（⚠ 刪除帳號）。您的 Firestore 文件會由 Cloud Function 立即移除;備份快照可能最長保留 30 天後才會完全清除。
- **網頁/Email 刪除帳號（無需安裝 App）**：若您已解除安裝 App,請以您註冊時使用的 Google 帳號信箱寄信至 `moooo.works@gmail.com`,主旨「ViewBoost account deletion」,我們將於 30 天內確認並完成刪除。
- **Crashlytics 診斷資料**：依 Google 標準政策最多保留 90 天。
- **購買兌換紀錄**：為處理計費爭議,保留至帳號生命週期結束。

### 您的權利（GDPR / CCPA）

若您居住於歐盟/英國/EEA（GDPR）或加州（CCPA）,您有權存取、更正、刪除、攜出或限制處理您的個人資料。我們不出售個人資訊。如需行使上述權利,請寄信至 `moooo.works@gmail.com`。

### 兒童隱私

本應用程式不針對 13 歲以下兒童,且不會故意收集兒童資料。如您認為有兒童向我們提供資料,請聯絡我們,我們將立即刪除。

### 政策變更

我們可能更新本政策。更新後繼續使用本應用程式即表示您接受新政策。本頁面頂端的「最後更新」日期反映最近一次修訂時間。

### 聯絡方式

如有疑問或資料相關請求,請聯絡:**moooo.works@gmail.com**
