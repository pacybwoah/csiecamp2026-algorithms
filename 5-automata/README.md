# 關卡五

## 關卡資訊
請先看 slides/ 內的關卡簡報 (`introduction.pdf`) 跟題解（`editorial.pdf`），如果有任何不清楚的細節請跟我講

關主流程：

0. 如 `introduction.pdf` 所說會分兩個教室，兩個關主在第一間，一個關主在第二間
1. 第一間關主請把撲克牌分成（黑桃、愛心）跟（紅磚、梅花）兩種，然後把除了 1-9 的拿掉
2. 兩個關主分別負責一個小隊，每一回合之前：
    - 給他們兩分鐘想，這時候把牌處理好
        - 如果是第一關，直接抽十張牌就好
        - 如果是第二關，請用 `generate.py` 生成謎底
    - 照說明簡報所說，叫小隊員一個一個出來，要用某個東西把白板擋起來讓其他人看不到
    - 一個隊員做完事就可以趕他去第二間教室然後叫下一個
3. 最重要的是要把 1. 那十張牌 跟 2. 每個隊員做的操作記在 https://docs.google.com/spreadsheets/d/1E6H7rAKHYmUjqgZ2lOTnRrL53KMOc67oTGatTlMwHaA/edit?gid=0#gid=0，然後第二間關主用投影布幕直播這個
4. 1-9 玩完之後，第二間關主叫他們猜對方回答的答案

然後要講介紹跟題解，應該就大概照念就好，要確定他們知道第二關規則（紅黑紅黑紅會算兩次）

## 重新編譯簡報

```sh
cd slides
xelatex introduction.tex
xelatex editorial.tex
```

需要 XeLaTeX、`beamer`、`xeCJK`、`tcolorbox`，以及中文字型 `Heiti TC`、英文字型 `JetBrainsMono Nerd Font`
（沒有的話可改 `coconut-theme.tex` 裡的 `\setCJKmainfont`）。