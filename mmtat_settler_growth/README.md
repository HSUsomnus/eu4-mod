# 全局移民增長 — 安本纳尔修改器 附加功能

Global Settler Growth — an add-on for the Anbennar Trainer

在**安本纳尔修改器**的主選單裡加一個「全局移民增長」面板，用 +100 / -100 / 歸零三個按鈕調整 `global_colonial_growth`（遊戲內顯示為「全局移民增加」），範圍 0～5000。

Adds a "Global Settler Growth" panel to the Anbennar Trainer's main menu, adjusting `global_colonial_growth` in ±100 steps between 0 and 5000.

**支援版本 / Supported version:** EU4 1.37.5.*

---

## ⚠️ 這不是獨立 Mod / This is not a standalone mod

本目錄是**掛在別人的創意工坊 Mod 上的修改**，不能單獨使用。

This is a **modification layered on top of a third-party Workshop mod**. It cannot run on its own.

| 依賴 / Dependency | Workshop ID | 作者 / Author |
|---|---|---|
| 安本纳尔修改器 (Anbennar Trainer) | `3756037459` | Memento |
| Anbennar: A Fantasy Total Conversion | `1385440355` | Anbennar Team |
| [EU4dll](https://github.com/matanki-saito/EU4dll) | — | matanki-saito |

本目錄**只包含本專案自行撰寫的檔案**。上述 Mod 的任何檔案都沒有收錄在此 repo——創意工坊作品沒有再散布授權，請自行從 Steam 訂閱取得。

This directory contains **only files written for this project**. No files from the mods above are redistributed here; subscribe to them on Steam.

命名沿用原修改器的 `mmtat_` 前綴，以便與其既有功能並存而不衝突。

---

## 為什麼要這樣裝 / Why the install is unusual

Anbennar 的 `descriptor.mod` 宣告了：

```
replace_path="events"
replace_path="decisions"
```

這會讓遊戲**忽略其他 Mod 在這兩個資料夾下的所有檔案**，而修改器的內容剛好全在這兩個資料夾。這不是載入順序問題，把修改器排在 Anbennar 後面也沒用。

Anbennar declares `replace_path` for `events` and `decisions`, which makes the game ignore those folders from every other mod. Load order does not help.

因此唯一可行的做法是把檔案放進 **Anbennar 自己的資料夾**——檔案在替換方自己的目錄裡就不會被排除掉。

The workaround is to place the files inside **Anbennar's own folder**, where `replace_path` cannot exclude them.

### 診斷指紋 / Diagnostic fingerprint

功能沒出現時，先看 `logs\error.log`：

```
[eventmanager.cpp:389]: unknown namespace 'mmtat_...' defined in event files
[onaction.cpp:189]: On action event mmtat_... does not exist!
```

出現這類訊息代表 `events/` 被 `replace_path` 擋掉了，不是語法錯誤。

---

## 安裝 / Installation

執行 `install.py`（需要 Python 3）：

```bash
python install.py
```

它會做兩件事：

1. 把本目錄的 4 個檔案複製進 Anbennar 的 mod 資料夾
2. 在 Anbennar 那份 `events/mmtat_menu.txt` 複製檔裡插入一個選單項目

插入採**位元組層級**，不重新編碼整個檔案——原修改器的註解是已經損壞的雙重編碼位元組，整檔重寫會把它們毀掉。腳本會先建立 `.orig` 備份，且重複執行不會重覆插入。

The menu insertion is done at **byte level** with no re-encoding, because the original trainer's comments are already double-encoded byte sequences that a full rewrite would destroy. The script backs up to `.orig` and is idempotent.

### ⚠️ Anbennar 更新後會失效 / Breaks on every Anbennar update

Steam 更新 Anbennar 時會還原整個 workshop 資料夾，把所有外來檔案清掉，本功能與修改器本身都會一起消失。**每次 Anbennar 更新後都要重跑一次 `install.py`**，並重新複製修改器自己那 10 個檔。

Steam restores the workshop folder on every Anbennar update, wiping all foreign files. Re-run `install.py` after each update.

---

## 實作 / Implementation

| 檔案 | 內容 |
|---|---|
| `events/mmtat_settler.txt` | 面板事件 `mmtat_settler.1`，四個選項 |
| `common/event_modifiers/mmtat_settler_modifiers.txt` | 50 個級距 `mmtat_settler_100` … `mmtat_settler_5000` |
| `common/scripted_effects/mmtat_settler_effects.txt` | `mmtat_settler_clear` / `mmtat_settler_refresh` |
| `localisation/mmtat_settler_l_english.yml` | 介面字串與 50 個修正名稱 |

### ⚠️ 欄位名稱：`global_colonial_growth`

EU4 **沒有** `global_settler_increase` 這個修正欄位。初版誤用了它，遊戲會靜默忽略整個
修正（面板、變數、修正切換全都正常運作，但數值不會進到「全局移民增加」）。

診斷方式 — `logs\error.log`：

```
[modifier.cpp]: Unknown modifier. Type: "global_settler_increase", File: "..."
```

正確欄位是 `global_colonial_growth`，原版 23 個檔、Anbennar 74 個檔都用它；
原版的「开疆扩土」(`expand_colonial_territory`) 就是這個欄位的來源之一。

### 為什麼是 50 個修正而不是一個動態值

`global_colonial_growth` 是 modifier 欄位，不能直接綁國家變數。所以改用：

```
國家變數 mmtat_settler_bonus 保存目前級距
→ 按鈕修改變數 ±100
→ mmtat_settler_refresh 移除全部 50 個舊級距
→ 依變數套用唯一一個對應 modifier
```

`remove_country_modifier` 對不存在的修正是 no-op，所以全部移除再套用是安全的，也保證任何時間最多只有一個 `mmtat_settler_*` 生效。腳本只處理自己建立的 `mmtat_settler_*`，不動修改器其他功能、Anbennar 或原版的殖民加成。

### 邊界處理

到達 0 或 5000 時，對應按鈕直接**不顯示**（透過 option `trigger`）。事件選項沒有「變灰」這個狀態，只有顯示或不顯示。

### 目前數值怎麼看

透過**國家修正清單**——修正名稱本身就是「全局移民增長 +300」。

沒有採用 `[Root.<variable>.GetValue]` 這類本地化變數語法，因為該語法在本專案的 EU4 版本尚未驗證，寫錯會讓整個事件描述無法顯示。

### 本地化編碼

`mmtat_settler_l_english.yml` 是**預先以 EU4dll 跳脫編碼寫入**的，不是一般 UTF-8 中文。EU4 引擎的 bitmapfont 只接受字元 ID ≤ 255，中文必須編成 3 位元組跳脫格式，由 EU4dll 在執行期還原。編碼器移植自 EU4dll 的 `Plugin64/escape_tool.cpp`。

**沒有 EU4dll 時這個檔會顯示成亂碼。**

---

## 驗收 / Acceptance checklist

部分已於 2026-08-04 實機確認，其餘待驗。

Partially verified in-game on 2026-08-04; the rest is pending.

- [x] 面板出現、中文顯示正常、變數改動與修正切換正常（2026-08-04 實機確認）
- [ ] 第一次 `+100` 是否取得 `global_colonial_growth = 100`（欄位修正後待重驗）
- [ ] 連按 `+100` 是否正確累加，且任何時間只有一個 `mmtat_settler_*` 修正
- [ ] `-100` 與歸零行為
- [ ] 0 與 5000 邊界時按鈕是否正確隱藏
- [ ] 存檔／讀檔後變數與修正是否一致
- [ ] AI 國家不受影響
- [ ] `error.log` 無 `mmtat_settler` 相關報錯

---

## 授權 / Licence

本目錄內由本專案撰寫的檔案採 MIT。所依賴的第三方 Mod 各自保留其原作者權利，本 repo 未包含也未再散布其任何檔案。

Files authored by this project are MIT. The third-party mods remain under their authors' terms; none of their files are included or redistributed here.
