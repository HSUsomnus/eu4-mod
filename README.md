# EU4 Mods

Europa Universalis IV 的自製工具型 Mod 與修改。

Utility mods and modifications for Europa Universalis IV.

**支援版本 / Supported version:** 1.37.5.*

---

## 內容 / Contents

### 1. [Boost Toggle](boost_toggle/) — 獨立 Mod / Standalone mod

透過「決策」面板切換全球殖民移民與陸軍士氣加成。僅影響玩家，不影響 AI。

Toggle global colonial growth and army morale bonuses via the Decisions panel. Player-only.

安裝：把 `boost_toggle/` 與 `boost_toggle.mod` 放進 EU4 mod 目錄，在啟動器啟用。
詳見 [`boost_toggle/README.md`](boost_toggle/README.md)。

---

### 2. [全局移民增長](mmtat_settler_growth/) — 附加功能，非獨立 Mod / Add-on, not standalone

⚠️ **這是基於第三方創意工坊修改器 Mod 的修改，不能單獨使用。**

⚠️ **This is a modification built on top of a third-party Workshop trainer mod. It does not work standalone.**

在**安本纳尔修改器 (Anbennar Trainer)** 的主選單裡加一個「全局移民增長」面板，用 +100 / -100 / 歸零三個按鈕調整 `global_settler_increase`，範圍 0～5000。

Adds a "Global Settler Growth" panel to the **Anbennar Trainer**'s main menu.

| 依賴 / Dependency | 來源 / Source |
|---|---|
| 安本纳尔修改器 (Anbennar Trainer) | Steam Workshop `3756037459`（作者 Memento） |
| Anbennar: A Fantasy Total Conversion | Steam Workshop `1385440355` |
| EU4dll（中文顯示必需） | [matanki-saito/EU4dll](https://github.com/matanki-saito/EU4dll) |

**本 repo 不包含也不再散布上述任何 Mod 的檔案**，只收錄本專案自行撰寫的部分。
上述 Mod 請自行從 Steam 訂閱或依其原始來源取得，各自權利歸原作者所有。

**This repo does not include or redistribute any files from those mods** — only files written for this project. Obtain them from Steam; all rights remain with their respective authors.

安裝：`cd mmtat_settler_growth && python install.py`
詳見 [`mmtat_settler_growth/README.md`](mmtat_settler_growth/README.md)，內含 Anbennar `replace_path` 衝突的說明與排查方式。

---

## 授權 / Licence

本 repo 內由本專案撰寫的檔案採 MIT。第三方 Mod 不在此授權範圍內。

Files authored by this project are MIT-licensed. Third-party mods are not covered.
