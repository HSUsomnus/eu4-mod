# EU4 Mods

Europa Universalis IV 的自製工具型 Mod 與修改。

Utility mods and modifications for Europa Universalis IV.

**支援版本 / Supported version:** 1.37.5.*

---

## 內容 / Contents

### [全局移民增長](mmtat_settler_growth/) — 附加功能，非獨立 Mod / Add-on, not standalone

⚠️ **這是基於第三方創意工坊修改器 Mod 的修改，不能單獨使用。**

⚠️ **This is a modification built on top of a third-party Workshop trainer mod. It does not work standalone.**

在**安本纳尔修改器 (Anbennar Trainer)** 的主選單裡加一個「全局移民增長」面板，用 +100 / -100 / 歸零三個按鈕調整 `global_colonial_growth`，範圍 0～5000。

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

## 已移除 / Removed

### Boost Toggle（2026-08-05 移除 / removed）

透過決議面板切換 `global_colonial_growth` 與 `land_morale` 的獨立作弊 Mod。已放棄，原因：

A standalone player-only cheat mod toggling `global_colonial_growth` and `land_morale` via decisions. Abandoned because:

- **入口是決議，在 Anbennar 底下必定失效。** Anbennar 宣告 `replace_path="decisions"`，其他 Mod 的 `decisions/` 一律被忽略，怎麼裝都不會出現。
  Its entry point is a decision, and Anbennar's `replace_path="decisions"` makes it unreachable no matter how it is installed.
- **移民加成與 `mmtat_settler_growth` 重複**，後者對同一個 `global_colonial_growth` 欄位提供 0～5000、±100 的細調。
  Its colonial-growth half duplicates `mmtat_settler_growth`, which controls the same field with finer steps.

唯一不重複的是陸軍士氣。若日後需要，正確做法是仿照 `mmtat_settler_growth` 在修改器主選單新增面板，沿用既有注入點，而非再維護一個獨立 Mod。

Only the land-morale half was unique. If wanted later, add it as another Anbennar Trainer panel following the `mmtat_settler_growth` pattern rather than as a separate mod.

---

## 授權 / Licence

本 repo 內由本專案撰寫的檔案採 MIT。第三方 Mod 不在此授權範圍內。

Files authored by this project are MIT-licensed. Third-party mods are not covered.
