# Boost Toggle — EU4 Mod

A simple cheat/utility mod for Europa Universalis IV that lets you toggle powerful stat boosts on and off via in-game decisions. Player-only; AI is never affected.

**Supported version:** 1.37.5.*

---

## Features

### Group A — Global Colonial Growth
Toggle a permanent migration bonus via the Decisions panel:

| Decision | Effect |
|---|---|
| [Boost] Migration +200 | `global_colonial_growth = +200` |
| [Boost] Migration +500 | `global_colonial_growth = +500` |
| [Boost] Migration +1000 | `global_colonial_growth = +1000` |
| [Boost] Migration — OFF | Remove active migration bonus |

### Group B — Army Morale
Toggle a permanent land morale bonus via the Decisions panel:

| Decision | Effect |
|---|---|
| [Boost] Army Morale +200% | `land_morale = +200%` |
| [Boost] Army Morale +500% | `land_morale = +500%` |
| [Boost] Army Morale +1000% | `land_morale = +1000%` |
| [Boost] Army Morale — OFF | Remove active morale bonus |

Only one level can be active at a time per category. Selecting a new level automatically removes the previous one.

---

## Installation

1. Copy the `boost_toggle` folder and `boost_toggle.mod` file into your EU4 mod directory:
   ```
   Documents/Paradox Interactive/Europa Universalis IV/mod/
   ```
2. Enable **Boost Toggle** in the EU4 launcher.
3. Start or load a game and open the **Decisions** panel to find the boost options.

---

## Notes

- All boosts are permanent (`duration = -1`) until manually turned off.
- Only affects the human player (`ai = no`).
- Compatible with most other mods as it only adds new modifiers and decisions.
