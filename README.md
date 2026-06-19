# Boost Toggle — EU4 Mod

一個讓你在遊戲內透過「決策」面板自由切換強力數值加成的工具型 Mod，僅影響玩家本人，不影響 AI。

A simple cheat/utility mod for EU4 that lets you toggle powerful stat boosts on and off via the Decisions panel. Player-only; AI is never affected.

**支援版本 / Supported version:** 1.37.5.*

---

## 功能介紹 / Features

### A 組：全球殖民移民 / Group A — Global Colonial Growth

透過決策面板切換永久性移民加成：

Toggle a permanent migration bonus via the Decisions panel:

| 決策 / Decision | 效果 / Effect |
|---|---|
| [Boost] 移民 +200 / Migration +200 | `global_colonial_growth = +200` |
| [Boost] 移民 +500 / Migration +500 | `global_colonial_growth = +500` |
| [Boost] 移民 +1000 / Migration +1000 | `global_colonial_growth = +1000` |
| [Boost] 移民 — 關閉 / Migration — OFF | 移除當前移民加成 / Remove active bonus |

### B 組：陸軍士氣 / Group B — Army Morale

透過決策面板切換永久性士氣加成：

Toggle a permanent land morale bonus via the Decisions panel:

| 決策 / Decision | 效果 / Effect |
|---|---|
| [Boost] 士氣 +200% / Army Morale +200% | `land_morale = +200%` |
| [Boost] 士氣 +500% / Army Morale +500% | `land_morale = +500%` |
| [Boost] 士氣 +1000% / Army Morale +1000% | `land_morale = +1000%` |
| [Boost] 士氣 — 關閉 / Army Morale — OFF | 移除當前士氣加成 / Remove active bonus |

每個類別同一時間只能啟用一個等級，選擇新等級時會自動移除舊的。

Only one level can be active at a time per category. Selecting a new level automatically removes the previous one.

---

## 安裝方式 / Installation

1. 將 `boost_toggle` 資料夾與 `boost_toggle.mod` 複製到 EU4 Mod 目錄：

   Copy the `boost_toggle` folder and `boost_toggle.mod` file into your EU4 mod directory:
   ```
   Documents/Paradox Interactive/Europa Universalis IV/mod/
   ```

2. 在 EU4 啟動器中啟用 **Boost Toggle**。

   Enable **Boost Toggle** in the EU4 launcher.

3. 進入遊戲後打開「決策」面板即可使用。

   Start or load a game and open the **Decisions** panel to find the boost options.

---

## 備註 / Notes

- 所有加成皆為永久生效（`duration = -1`），需手動關閉。All boosts are permanent (`duration = -1`) until manually turned off.
- 僅影響玩家（`ai = no`），不影響 AI 國家。Only affects the human player; AI countries are unaffected.
- 僅新增 Modifier 與 Decision，與大多數 Mod 相容。Compatible with most other mods as it only adds new modifiers and decisions.
