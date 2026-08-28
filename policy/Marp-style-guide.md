# Marp講義スライド スタイルガイド

## 1. 基本コンセプト

このスタイルは、大学の講義・研究発表において、

- 内容を一目で把握できる
- 教員の口頭説明を主、スライドを補助とする
- 数式・図・コードを視覚的に理解しやすくする
- 「何が重要なのか」を色とサイズで明確にする

ことを目的とする。

デザイン上の基本原則は以下。

> **白いキャンバスの上に、濃紺を基本色として情報を配置し、赤紫を「意味のある強調」に限定して使用する。**

装飾よりも情報構造を優先する。

---

# 2. スライドサイズ

Marpでは必ず **4:3** を使用する。

```yaml
---
marp: true
size: 4:3
theme: lecture
paginate: false
---
```

カスタムサイズを指定する場合：

```css
/* @size 4:3 10in 7.5in */
```

標準的な論理サイズ：

- 横：1024
- 縦：768
- アスペクト比：4:3

---

# 3. 1スライドあたりの情報量

## 3.1 原則

**1スライド = 1メッセージ**

「このスライドを見た学生が、10秒後に何を覚えていればよいか」を1つに絞る。

---

## 3.2 文字数の目安

日本語の場合、タイトルを除いた本文について以下を目安とする。

| スライドタイプ | 推奨文字数 | 上限目安 |
|---|---:|---:|
| メッセージ中心 | 20〜50文字 | 70文字 |
| 図＋説明 | 30〜80文字 | 100文字 |
| 箇条書き | 60〜120文字 | 150文字 |
| 数式＋説明 | 30〜80文字 | 100文字 |
| コード＋説明 | 20〜60文字＋コード | 100文字 |
| 比較・まとめ | 50〜100文字 | 130文字 |

通常スライドでは、

> **本文60〜100文字程度**

を標準とする。

**150文字を超えたら、原則として2枚以上に分割する。**

---

## 3.3 行数の目安

本文：

- 3〜6行程度
- 最大8行

箇条書き：

- 2〜4項目
- 最大5項目

1項目：

- 原則1行
- 長くても2行

---

## 3.4 「少なすぎる」ことを恐れない

例えば、

```text
次数中心性

多くのノードと接続しているノードは？
```

だけでも1枚として成立する。

情報を1枚にまとめるより、

```text
概念
↓
直感
↓
定義
↓
式
↓
具体例
↓
コード
```

のように複数スライドへ分解することを優先する。

---

# 4. カラースキーマ

## 4.1 基本色

```css
:root {
  --navy: #08285A;
  --text: #293348;
  --accent: #C2174F;
  --blue: #0783C6;

  --pink-light: #F3DDE5;
  --blue-light: #DDECF6;

  --gray: #C7C7C7;
  --gray-light: #EEEEEE;
  --code-bg: #E8EBF2;

  --white: #FFFFFF;
}
```

---

## 4.2 色の役割

### Navy

```text
#08285A
```

使用対象：

- タイトルバー
- 図の輪郭線
- エッジ
- 基本文字の一部
- コード枠線

---

### Dark Text

```text
#293348
```

使用対象：

- 本文
- 大見出し
- 数式
- 通常ラベル

完全な黒 `#000000` は原則使わない。

---

### Accent Red

```text
#C2174F
```

最重要色。

使用対象：

- キーワード
- 注目ノード
- 注目エッジ
- 矢印
- 注意
- 結論
- 問い
- 下部メッセージバー

**意味のある強調だけに使う。**

---

### Accent Blue

```text
#0783C6
```

用途：

- 比較対象
- 第2の注目対象
- 対照条件
- 別カテゴリ

赤と青を同時使用する場合：

```text
赤 = A側
青 = B側
```

のように意味を固定する。

---

# 5. コントラストの文法

基本：

```text
背景             白
通常情報         濃紺／濃いグレー
重要情報         赤紫
補助比較         青
非注目情報       薄グレー
```

視線誘導には**色を増やすのではなく、コントラストを落とす**。

例：

```html
<div class="inactive">
固有ベクトル中心性
</div>

<div>
次数中心性
</div>
```

```css
.inactive {
  color: #C7C7C7;
}
```

現在説明している要素だけを濃くする。

---

# 6. フォント

## 6.1 日本語

優先順位：

```css
font-family:
  "Noto Sans JP",
  "Hiragino Sans",
  "Yu Gothic",
  sans-serif;
```

Mac中心で生成する場合：

```css
font-family:
  "Hiragino Sans",
  "Noto Sans JP",
  sans-serif;
```

推奨：

- Noto Sans JP
- ヒラギノ角ゴ
- 游ゴシック

---

# 7. 文字サイズ

4:3を前提とする。

```css
section {
  font-size: 30px;
}
```

目安：

| 要素 | サイズ |
|---|---:|
| 上部タイトル | 25〜29px |
| 主メッセージ | 44〜52px |
| 大見出し | 40〜48px |
| 本文 | 29〜34px |
| 箇条書き | 29〜34px |
| 注釈 | 22〜27px |
| コード | 24〜28px |
| 数式 | 36〜48px |

---

# 8. 太さの文法

重要なのは「サイズ＋太さ」の階層。

```text
タイトルバー       Regular / Medium
本文               Regular
見出し             Bold
メインメッセージ   Bold / ExtraBold
強調語             Bold
```

例：

```html
<div class="hero">
注目ノードが
<span class="accent">いくつのノードと接しているか</span>
を示す指標
</div>
```

---

# 9. 基本レイアウト

全スライドに上部タイトルバーを配置する。

```text
┌──────────────────────────┐
│ Title                    │
├──────────────────────────┤
│                          │
│       CONTENT            │
│                          │
│                          │
└──────────────────────────┘
```

---

# 10. タイトルバー

高さ：

```text
スライド高さの約6〜7%
```

Marp：

```css
section::before {
  content: attr(data-title);
}
```

ただしMarpでは疑似要素によるタイトル管理より、

```markdown
<div class="slide-title">
次数中心性 (degree centrality) (1/4)
</div>
```

を標準とする方が安定する。

CSS：

```css
.slide-title {
  position: absolute;
  top: 14px;
  left: 14px;
  right: 14px;

  height: 52px;

  background: var(--navy);
  color: white;

  box-sizing: border-box;

  display: flex;
  align-items: center;

  padding-left: 60px;

  font-size: 27px;
  font-weight: 400;
}
```

---

# 11. コンテンツ領域

```css
section {
  padding:
    95px
    70px
    45px
    70px;
}
```

目安：

```text
上：90〜100px
左右：60〜75px
下：40〜50px
```

タイトルバーと本文の間に十分な余白を取る。

---

# 12. メインメッセージ

スライド上部には「そのスライドの結論」を置く。

例：

```markdown
<div class="hero">

注目ノードとグラフ中の他のノードとの  
<span class="accent">距離が平均的にどの程度近いか</span>を示す指標

</div>
```

```css
.hero {
  font-size: 47px;
  font-weight: 800;
  line-height: 1.25;
  color: var(--text);
}

.accent {
  color: var(--accent);
}
```

---

# 13. 強調の文法

文章全体を赤にしない。

NG：

```text
注目ノードがいくつのノードと接しているかを示す指標
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 全部赤
```

OK：

```text
注目ノードが
「いくつのノードと接しているか」
を示す指標
```

赤は1スライド中：

- 1〜3箇所
- 合計10〜30文字程度

を目安とする。

---

# 14. 図と文章の比率

標準：

```text
文章 : 図 = 30 : 70
```

または

```text
文章 : 図 = 40 : 60
```

図を説明するスライドでは、図を可能な限り大きくする。

---

# 15. 代表レイアウト

## Pattern A：メッセージ＋図

```text
┌────────────────────────┐
│ Title                  │
├────────────────────────┤
│ BIG MESSAGE            │
│                        │
│       DIAGRAM          │
│                        │
└────────────────────────┘
```

最も基本的な形式。

---

## Pattern B：左右分割

```text
┌────────────────────────┐
│ Title                  │
├────────────────────────┤
│ MESSAGE                │
│                        │
│ Diagram      Formula   │
│                        │
└────────────────────────┘
```

Marp：

```html
<div class="columns">
  <div>
    図
  </div>

  <div>
    数式
  </div>
</div>
```

```css
.columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 50px;
  align-items: center;
}
```

---

## Pattern C：比較

```text
      A                B

    [図]             [図]

   結果A             結果B
```

左右対称を徹底する。

---

## Pattern D：段階説明

同一レイアウトを数枚連続使用する。

```text
Slide 1    全体
Slide 2    分子を強調
Slide 3    分母を強調
Slide 4    計算例
Slide 5    コード
```

**情報を追加するたびにレイアウトを変更しない。**

学生が「変わった部分」にだけ注意できるようにする。

---

# 16. 非注目要素のグレーアウト

Marpではアニメーションが基本的に使えないため、

**同じスライドを複製して状態を変更する。**

例：

Slide 1：

```text
近接中心性
次数中心性
固有ベクトル中心性
媒介中心性
```

Slide 2：

```text
近接中心性 ← 濃紺
次数中心性 ← グレー
固有ベクトル中心性 ← グレー
媒介中心性 ← グレー
```

Marpでは：

```html
<div class="active">
近接中心性
</div>

<div class="inactive">
次数中心性
</div>
```

---

# 17. 下部メッセージバー

重要な結論・注意・問いは下端に赤いバーを置く。

例：

```markdown
<div class="takeaway">
グラフの何に注目したいかによって用いる中心性は変わる
</div>
```

```css
.takeaway {
  position: absolute;

  left: 100px;
  right: 15px;
  bottom: 16px;

  background: var(--accent);
  color: white;

  padding: 10px 28px;

  border-radius: 30px 0 0 30px;

  font-size: 27px;
  text-align: center;
}
```

用途：

- 結論
- 注意
- 問い
- 次への導入

頻繁に使いすぎない。

---

# 18. 数式

数式はできるだけ単独で大きく表示する。

```markdown
$$
C_D(v_i)=\frac{\deg(v_i)}{|V|-1}
$$
```

数式の周囲には十分な余白を入れる。

数式の一部を説明するときは、

```text
数式
↑
赤い矢印
説明
```

とする。

文章で数式全体を説明しない。

---

# 19. コード

コードは10行以内を基本とする。

推奨：

- 3〜8行
- 最大12行

長いコードは複数スライドに分ける。

```markdown
<div class="codebox">

```python
# 次数中心性
nx.degree_centrality(G)

# 正規化なし
G.degree
```

</div>
```

CSS：

```css
.codebox {
  background: var(--code-bg);
  border-left: 6px solid var(--navy);
  padding: 20px;
}
```

---

# 20. コードの色

基本：

```text
コード          濃紺
コメント        緑
背景            薄い青グレー
```

派手なIDEテーマは使わない。

---

# 21. 箇条書き

最大4項目程度。

```markdown
- グラフにおける各ノードの重要度を示す指数
- 重要ノードの発見や順序づけに利用
- グラフ構造に基づいて計算
```

箇条書きだけでスライドを完成させない。

可能なら下半分には：

- 図
- 具体例
- 問い

のいずれかを配置する。

---

# 22. 図形

図形は以下に限定する。

- 円
- 角丸長方形
- 線
- 矢印
- 点線矢印

3D、影、グラデーションは使用しない。

---

# 23. ノード図

```css
.node {
  background: white;
  border: 5px solid var(--navy);
  border-radius: 50%;
}

.node.focus-red {
  background: var(--pink-light);
}

.node.focus-blue {
  background: var(--blue-light);
}
```

---

# 24. 線

標準：

```css
stroke: var(--navy);
stroke-width: 5;
```

注目：

```css
stroke: var(--accent);
```

補助：

```css
stroke: var(--blue);
```

---

# 25. 画像生成時のルール

画像をAI等で生成する場合も、

- 白背景
- フラットデザイン
- 線画中心
- 影なし
- グラデーションなし
- 使用色は基本4色以内

とする。

---

# 26. Marpで避けること

## NG 1：Markdownだけで複雑なレイアウトを作る

複雑なスライドではHTMLを使用する。

```html
<div class="columns">
...
</div>
```

---

## NG 2：1枚に内容を詰め込む

Marpではページ追加コストが低い。

したがって、

```text
1枚にまとめる
```

より

```text
3枚に分解する
```

を優先する。

---

## NG 3：毎回違うレイアウト

レイアウトパターンを5〜6種類に限定する。

---

# 27. 推奨Marpテーマ

`lecture.css`

```css
/* @theme lecture */
/* @size 4:3 10in 7.5in */

:root {
  --navy: #08285A;
  --text: #293348;
  --accent: #C2174F;
  --blue: #0783C6;

  --pink-light: #F3DDE5;
  --blue-light: #DDECF6;

  --gray: #C7C7C7;
  --gray-light: #EEEEEE;
  --code-bg: #E8EBF2;
}

section {
  width: 10in;
  height: 7.5in;

  padding: 95px 70px 45px;

  background: white;
  color: var(--text);

  font-family:
    "Noto Sans JP",
    "Hiragino Sans",
    "Yu Gothic",
    sans-serif;

  font-size: 31px;
  line-height: 1.35;
}

.slide-title {
  position: absolute;

  top: 14px;
  left: 14px;
  right: 14px;

  height: 52px;

  padding-left: 60px;

  box-sizing: border-box;

  display: flex;
  align-items: center;

  background: var(--navy);
  color: white;

  font-size: 27px;
  font-weight: 400;
}

.hero {
  font-size: 47px;
  font-weight: 800;
  line-height: 1.25;
}

.accent {
  color: var(--accent);
}

.blue {
  color: var(--blue);
}

.inactive {
  color: var(--gray);
}

.columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 50px;
  align-items: center;
}

.takeaway {
  position: absolute;

  left: 100px;
  right: 15px;
  bottom: 16px;

  box-sizing: border-box;

  padding: 9px 28px;

  background: var(--accent);
  color: white;

  border-radius: 32px 0 0 32px;

  text-align: center;
  font-size: 27px;
}

pre {
  background: var(--code-bg);
  border-left: 6px solid var(--navy);

  padding: 18px 22px;

  font-size: 25px;
}

strong {
  color: var(--accent);
}
```

---

# 28. Marp Markdownテンプレート

```markdown
---
marp: true
theme: lecture
size: 4:3
paginate: false
math: mathjax
---

<div class="slide-title">
次数中心性 (degree centrality) (1/4)
</div>

<div class="hero">

注目ノードが  
<span class="accent">いくつのノードと接しているか</span>  
を示す指標

</div>

<div class="columns">

<div>

[図]

</div>

<div>

$$
C_D(v_i)=\deg(v_i)
$$

</div>

</div>

---

<div class="slide-title">
次数中心性 (degree centrality) (2/4)
</div>

<div class="hero">

注目ノードが  
<span class="accent">いくつのノードと接しているか</span>  
を示す指標

</div>

<div class="columns">

<div>

[同じ図]

</div>

<div>

$$
C_D(v_i)
=
\frac{\deg(v_i)}{|V|-1}
$$

</div>

</div>

<div class="takeaway">
グラフに属するノードの数で正規化することもある
</div>
```

---

# 29. 自動生成AI向けレイアウト判断ルール

スライド生成時には、内容を以下の順番で分類する。

### STEP 1

まず1枚の「中心メッセージ」を決める。

### STEP 2

文字数を確認する。

```text
〜100文字   → 原則1枚
100〜150文字 → 図がなければ1枚も可
150文字〜   → 分割
```

### STEP 3

内容タイプを判定する。

```text
概念説明 → Hero + Diagram

比較
→ 2 columns

数式説明
→ Diagram + Formula

コード
→ Diagram + Code

複数概念
→ List

結論
→ Hero / Takeaway
```

### STEP 4

強調語を1〜3個抽出する。

### STEP 5

強調語だけを赤紫にする。

### STEP 6

説明可能なら文章を図へ変換する。

---

# 30. AI生成時の最重要ルール

以下を優先順位順に守る。

1. **1スライド1メッセージ**
2. **本文60〜100文字程度**
3. **150文字を超えたら分割**
4. **図を大きくする**
5. **重要語だけ赤紫**
6. **濃紺＋赤紫＋白を基本色とする**
7. **同一テーマの説明ではレイアウトを維持する**
8. **段階説明はスライドを複製して差分だけ変える**
9. **小さい文字を使わない**
10. **情報量が少ないことを恐れない**

---

# 31. デザインを一言で表現すると

> **「教科書を縮小して貼る」のではなく、「板書の要点を1場面ずつ切り出す」スライド。**

大量の情報を一覧表示するのではなく、

**問い → 直感 → 定義 → 数式 → 具体例 → 実装**

を時間方向に分割して見せる。