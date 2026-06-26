# 關卡四

## 關卡資訊
請先看 slides/ 內的關卡簡報 (`introduction.pdf`) 跟題解（`editorial.pdf`），如果有任何不清楚的細節請跟我講

關主流程：

0. 先把 `print.pdf` 印 20 張，讓小隊有打草稿的地方
1. 到 http://ws7.csie.org:10061/gm 建立關卡，密碼為 `67`
    1. 第一回合請選 Level 2，第二回合請選 Level 3，不要管 Level 1
2. 叫兩隊派人猜拳，贏的選他們要先進攻還是先防守
3. 把關卡連結分別傳給兩小隊
4. 兩位關主分別管一個小隊，確保小隊知道網站怎麼操控（應該很簡單），如果小隊某一步花太久請勸導
5. 引導小隊的方向：
    1. 防守隊：
        - 你給這個提示，對方可以得到多少資訊？
            - 他可以把多少點刪掉？
    2. 進攻隊：
        - 現在還有哪些點可能是答案？
        - 我猜了這個點，對方最好的回答是什麼？
            - 如果對方的回答是 x，那我的局面會變成怎麼樣？
        - 我想要最小化可能是答案的點數，我要怎麼猜才能達成目標？

## 重新編譯簡報

```sh
cd slides
xelatex introduction.tex
xelatex editorial.tex
```

需要 XeLaTeX、`beamer`、`xeCJK`、`tcolorbox`，以及中文字型 `Heiti TC`、英文字型 `JetBrainsMono Nerd Font`
（沒有的話可改 `coconut-theme.tex` 裡的 `\setCJKmainfont`）。