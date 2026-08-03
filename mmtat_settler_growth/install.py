#!/usr/bin/env python3
"""安裝「全局移民增長」到安本纳尔修改器。

Anbennar 宣告 replace_path="events" 與 "decisions"，會讓遊戲忽略其他 mod 在這
兩個資料夾下的檔案。唯一可行的做法是把檔案放進 Anbennar 自己的資料夾。

Steam 每次更新 Anbennar 都會還原資料夾、清掉所有外來檔案，因此本腳本設計成可
重複執行：它會補齊修改器本身被清掉的檔案，再裝上本功能。

用法：
    python install.py [--workshop <236850 資料夾路徑>] [--dry-run]
"""
import argparse
import os
import shutil
import sys

ANBENNAR = "1385440355"
TRAINER = "3756037459"

DEFAULT_WORKSHOP = [
    r"D:\steam\steamapps\workshop\content\236850",
    r"C:\Program Files (x86)\Steam\steamapps\workshop\content\236850",
    os.path.expanduser(r"~\scoop\persist\steam\steamapps\workshop\content\236850"),
]

# 本功能自己的檔案：來源相對於本腳本，目的地相對於 Anbennar 資料夾
OWN_FILES = [
    "events/mmtat_settler.txt",
    "common/event_modifiers/mmtat_settler_modifiers.txt",
    "common/scripted_effects/mmtat_settler_effects.txt",
    "localisation/mmtat_settler_l_english.yml",
]

# 選單插入：錨點與插入內容都是純 ASCII，可安全做位元組層級比對
ANCHOR = (b"\toption = {\r\n"
          b"\t\tname = mmtat_global\r\n"
          b"\t\thidden_effect = {\r\n"
          b"\t\t\tcountry_event = { id = mmtat_global.1 }\r\n"
          b"\t\t}\r\n"
          b"\t}\r\n")

INSERT = (b"\r\n"
          b"\toption = {\r\n"
          b"\t\tname = mmtat_settler\r\n"
          b"\t\thidden_effect = {\r\n"
          b"\t\t\tcountry_event = { id = mmtat_settler.1 }\r\n"
          b"\t\t}\r\n"
          b"\t}\r\n")


def find_workshop(explicit):
    for p in ([explicit] if explicit else DEFAULT_WORKSHOP):
        if p and os.path.isdir(os.path.join(p, ANBENNAR)):
            return p
    sys.exit("找不到 Steam workshop 的 236850 資料夾，請用 --workshop 指定。\n"
             "已嘗試：\n  " + "\n  ".join(x for x in ([explicit] if explicit else DEFAULT_WORKSHOP) if x))


def restore_trainer(ws, dry):
    """補齊修改器被 Steam 還原清掉的 events/ 與 decisions/ 檔案。"""
    src, dst = os.path.join(ws, TRAINER), os.path.join(ws, ANBENNAR)
    if not os.path.isdir(src):
        print("！ 找不到修改器 %s，跳過這一步（只裝本功能）" % TRAINER)
        return 0
    n = 0
    for sub in ("decisions", "events"):
        s = os.path.join(src, sub)
        if not os.path.isdir(s):
            continue
        for fn in sorted(os.listdir(s)):
            if not (fn.startswith("mmtat_") and fn.endswith(".txt")):
                continue
            a, b = os.path.join(s, fn), os.path.join(dst, sub, fn)
            if os.path.exists(b):
                # 已插入選單的 mmtat_menu.txt 大小本來就與來源不同，不算缺檔
                if os.path.getsize(a) == os.path.getsize(b):
                    continue
                if INSERT in open(b, "rb").read():
                    continue
            print("  修改器 %s/%s" % (sub, fn))
            if not dry:
                os.makedirs(os.path.dirname(b), exist_ok=True)
                shutil.copy2(a, b)
            n += 1
    return n


def install_own(here, dst, dry):
    n = 0
    for rel in OWN_FILES:
        a = os.path.join(here, rel.replace("/", os.sep))
        if not os.path.isfile(a):
            sys.exit("缺少來源檔案：%s" % a)
        b = os.path.join(dst, rel.replace("/", os.sep))
        print("  本功能 %s" % rel)
        if not dry:
            os.makedirs(os.path.dirname(b), exist_ok=True)
            shutil.copy2(a, b)
        n += 1
    return n


def patch_menu(dst, dry):
    p = os.path.join(dst, "events", "mmtat_menu.txt")
    if not os.path.isfile(p):
        sys.exit("找不到 %s\n修改器的檔案還沒複製進 Anbennar，無法插入選單。" % p)
    raw = open(p, "rb").read()
    if INSERT in raw:
        print("  選單項目已存在，略過")
        return False
    n = raw.count(ANCHOR)
    if n != 1:
        sys.exit("錨點在 mmtat_menu.txt 出現 %d 次（預期 1 次）。\n"
                 "修改器可能已更新，請重新確認插入位置後再執行。" % n)
    print("  選單插入 mmtat_settler（%d -> %d bytes）" % (len(raw), len(raw) + len(INSERT)))
    if not dry:
        if not os.path.exists(p + ".orig"):
            open(p + ".orig", "wb").write(raw)
        open(p, "wb").write(raw.replace(ANCHOR, ANCHOR + INSERT))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workshop", help="Steam workshop 的 236850 資料夾")
    ap.add_argument("--dry-run", action="store_true", help="只顯示會做什麼，不實際寫入")
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    ws = find_workshop(args.workshop)
    dst = os.path.join(ws, ANBENNAR)
    print("Anbennar：%s\n" % dst)

    print("[1/3] 補齊修改器檔案")
    a = restore_trainer(ws, args.dry_run)
    print("      %s\n" % ("補了 %d 個檔" % a if a else "已是最新，無需補齊"))

    print("[2/3] 安裝本功能檔案")
    b = install_own(here, dst, args.dry_run)
    print("      %d 個檔\n" % b)

    print("[3/3] 插入選單項目")
    patch_menu(dst, args.dry_run)

    print("\n完成。" if not args.dry_run else "\n（dry-run，未寫入任何檔案）")
    print("進遊戲後從修改器主選單找「全局移民增長」。")
    print("若沒出現，檢查 logs\\error.log 有無 mmtat_settler 相關訊息。")


if __name__ == "__main__":
    main()
