# EU4 Mods

歐陸風雲 4（EU4）自製小 Mod：在 Anbennar 修改器裡調整全局移民成長。

A small utility add-on for Europa Universalis IV that adjusts global settler growth inside the Anbennar Trainer.

支援版本 / Supported version: EU4 `1.37.5.*`

---

## 這是什麼 / What this is

- 在 **安本纳尔修改器 (Anbennar Trainer)** 的主選單加上「全局移民成長」面板。
- **這不是獨立 Mod**，必須搭配下方兩個創意工坊 Mod 才能運作。
- Adds a "Global Settler Growth" panel to the **Anbennar Trainer** main menu.
- **Not standalone** — requires the two Workshop mods below to work.

---

## 需要先裝什麼 / Requirements

| 依賴 / Dependency | 來源 / Source |
|---|---|
| 安本纳尔修改器 (Anbennar Trainer) | [Steam Workshop `3756037459`](https://steamcommunity.com/sharedfiles/filedetails/?id=3756037459)（作者 Memento） |
| Anbennar: A Fantasy Total Conversion | [Steam Workshop `1385440355`](https://steamcommunity.com/sharedfiles/filedetails/?id=1385440355) |
| EU4dll（中文顯示必需 / required for Chinese text） | [matanki-saito/EU4dll](https://github.com/matanki-saito/EU4dll) |

本 repo 不包含也不散佈上述任何第三方 Mod 的檔案，只收錄本專案自行撰寫的部分；請自行從 Steam 或原始來源取得。

This repo does not include or redistribute any files from those mods — only files written for this project. Obtain them from Steam or their original sources; all rights remain with their respective authors.

---

## 怎麼安裝 / Installation

```bash
cd mmtat_settler_growth
python install.py
```

安裝腳本會把檔案複製進 Anbennar 的 Workshop 資料夾並插入選單項目；詳細步驟、參數、Anbennar `replace_path` 衝突說明與 Steam 更新後的重裝方式，請見 [`mmtat_settler_growth/README.md`](mmtat_settler_growth/README.md)。

The script copies the files into Anbennar's Workshop folder and adds the menu entry. See [`mmtat_settler_growth/README.md`](mmtat_settler_growth/README.md) for installation details, options, `replace_path` background, and re-running after Anbennar updates.

---

## 效果 / What it does

- 進遊戲後，從修改器主選單打開「全局移民成長」。
- 提供 `+100`、`-100`、`歸零` 三個按鈕，調整 `global_colonial_growth`（範圍 `0`～`5000`），只套用在玩家國家。
- Open "Global Settler Growth" from the trainer menu in-game to adjust `global_colonial_growth` from `0` to `5000` in `±100` steps (player-only).

---

## 已移除 / Removed

- **Boost Toggle**（2026-08-05 移除 / removed）：原本透過決議切換 `global_colonial_growth` 與 `land_morale` 的獨立 Mod。因 Anbennar 宣告 `replace_path="decisions"` 導致決議無法顯示，且移民加成與 `mmtat_settler_growth` 重複而移除；若日後需要陸軍士氣面板，可改為仿照 `mmtat_settler_growth` 加進修改器主選單。
- A standalone decision-based mod toggling `global_colonial_growth` and `land_morale`, removed because Anbennar's `replace_path="decisions"` blocks its entry point and its settler bonus duplicated `mmtat_settler_growth`.

---

## 授權 / Licence

本 repo 內由本專案撰寫的檔案採 MIT 授權；第三方 Mod 不在此授權範圍內。

Files authored by this project are MIT-licensed. Third-party mods remain under their authors' terms.
