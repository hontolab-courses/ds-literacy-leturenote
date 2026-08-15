"""データのライフサイクル図（共通部品）を生成する．

- common/common-lifecycle.svg      : フル版（第1章まとめ用，ハイライトなし）
- common/common-lifecycle-chNN.svg : 第2〜6章の冒頭用（現在地をハイライト）

スタイルは figures/STYLE.md に従う．
"""
import pathlib

FIGDIR = pathlib.Path(__file__).resolve().parent.parent / "common"

FONT = "'Hiragino Sans','Noto Sans JP',sans-serif"
BLUE_FILL, BLUE = "#EAF0F8", "#4C72B0"
ORANGE_FILL, ORANGE = "#FBEEE4", "#DD8452"
GRAY_FILL, GRAY = "#F2F2F2", "#8C8C8C"
TEXT = "#333333"

STAGES = [
    ("収集", "第2回", "ch02"),
    ("保存・検索", "第3回", "ch03"),
    ("前処理", "第4回", "ch04"),
    ("分析", "第5回", "ch05"),
    ("可視化", "第6回", "ch06"),
]

W, H = 1170, 330
BOX_W, BOX_H, GAP = 158, 64, 34
MARGIN = 24
TOP = 60


def stage_box(x, y, label, kaisu, highlight):
    fill = ORANGE_FILL if highlight else BLUE_FILL
    stroke = ORANGE if highlight else BLUE
    sw = 3 if highlight else 2
    parts = [
        f'<rect x="{x}" y="{y}" width="{BOX_W}" height="{BOX_H}" rx="8" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>',
        f'<text x="{x + BOX_W / 2}" y="{y + 28}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="19" font-weight="bold" fill="{TEXT}">{label}</text>',
        f'<text x="{x + BOX_W / 2}" y="{y + 50}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="14" fill="{stroke}">{kaisu}</text>',
    ]
    if highlight:
        parts.append(
            f'<text x="{x + BOX_W / 2}" y="{y - 12}" text-anchor="middle" '
            f'font-family="{FONT}" font-size="15" font-weight="bold" fill="{ORANGE}">▼ 現在地</text>'
        )
    return "\n".join(parts)


def arrow(x1, y, x2):
    return (
        f'<line x1="{x1}" y1="{y}" x2="{x2 - 10}" y2="{y}" '
        f'stroke="{GRAY}" stroke-width="2" marker-end="url(#ah)"/>'
    )


def build(highlight_idx=None):
    body = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'font-family="{FONT}">',
        '<defs><marker id="ah" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
        f'<path d="M0,0 L10,4 L0,8 z" fill="{GRAY}"/></marker></defs>',
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="white"/>',
    ]
    x = MARGIN
    mid = TOP + BOX_H / 2
    for i, (label, kaisu, _) in enumerate(STAGES):
        body.append(stage_box(x, TOP, label, kaisu, highlight_idx == i))
        if i < len(STAGES) - 1:
            body.append(arrow(x + BOX_W, mid, x + BOX_W + GAP))
        x += BOX_W + GAP
    # 末端：価値につながる矢印
    end_x = x
    body.append(arrow(end_x - GAP, mid, end_x))
    body.append(
        f'<rect x="{end_x}" y="{TOP + 6}" width="{W - end_x - MARGIN}" height="{BOX_H - 12}" rx="26" '
        f'fill="white" stroke="{GRAY}" stroke-width="2" stroke-dasharray="6 4"/>'
        f'<text x="{end_x + (W - end_x - MARGIN) / 2}" y="{mid - 4}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="15" fill="{TEXT}">誰かの理解・</text>'
        f'<text x="{end_x + (W - end_x - MARGIN) / 2}" y="{mid + 16}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="15" fill="{TEXT}">意思決定へ</text>'
    )
    # 横断テーマの帯
    band_x1, band_x2 = MARGIN, MARGIN + 5 * BOX_W + 4 * GAP
    for j, (name, kaisu) in enumerate([("データと法", "第7回"), ("生成AI", "第8回")]):
        by = TOP + BOX_H + 40 + j * 46
        body.append(
            f'<rect x="{band_x1}" y="{by}" width="{band_x2 - band_x1}" height="36" rx="8" '
            f'fill="{GRAY_FILL}" stroke="{GRAY}" stroke-width="2"/>'
            f'<text x="{(band_x1 + band_x2) / 2}" y="{by + 24}" text-anchor="middle" '
            f'font-family="{FONT}" font-size="16" fill="{TEXT}">{name}（{kaisu}）——ライフサイクル全体に関わる横断テーマ</text>'
        )
    body.append("</svg>")
    return "\n".join(body)


if __name__ == "__main__":
    (FIGDIR / "common-lifecycle.svg").write_text(build(None), encoding="utf-8")
    print("common-lifecycle.svg")
    for i, (_, _, ch) in enumerate(STAGES):
        path = FIGDIR / f"common-lifecycle-{ch}.svg"
        path.write_text(build(i), encoding="utf-8")
        print(path.name)
