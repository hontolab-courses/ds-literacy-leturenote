# 名古屋市立大学「データサイエンス・リテラシー」講義ノート作成のための参考資料リスト（授業回別）

## TL;DR
- 全8回について，ACM・IEEE・AAAI系の著名論文誌／国際会議を優先しつつ，Nature・Science・JASA・The American Statistician・Journal of Statistical Software等の古典的重要論文とオープンアクセス資料を組み合わせた，網羅的すぎない実用リストを作成した．
- 大半の資料はオープンアクセスPDFが実際にダウンロード可能であることを確認した（Cleveland，Donoho，Codd，Wickham，Stevens，Anscombe，FAIR原則，Stochastic Parrots，Attention Is All You Need，Mehrabiほか）．一部（Science，Nature，IEEE，一部ACM）は著者版のみ無料またはpaywallのため，DOI提示と配布時のライセンス確認が必要である．
- 学部1年生向け概論科目という性格上，最先端論文よりサーベイ・チュートリアル・マガジン記事・古典を優先し，各回に事例ベースの資料（1936年Literary Digestの世論調査失敗，Netflix再識別，だますグラフの実例など）を含めることで，導入と小テスト（事例判断型設問）の作成に直接使えるようにした．

## Key Findings
- **各回に「原典（古典）＋サーベイ／解説＋事例」の三層構造**を意識して選定した．たとえば第3回はCoddの原典（1970）＋NoSQLとの対比を論じるCACM記事（2011）＋FAIR原則（2016）で「保存の理論・多様化・実務」を，第6回はCHI/IEEE TVCGの実証研究＋EuroVisの分類学で「だますグラフ」を体系的に扱える．
- **オープンアクセスの確実性は資料ごとに大きく異なる**．整然データ（Journal of Statistical Software），FAIR原則（Scientific Data，CC BY），Stochastic Parrots（ACM，オープン），Transformer（arXiv），Mehrabiの公平性サーベイ（arXiv版）は確実にダウンロード可能である一方，Bakshyら（Science）とvan Disら（Nature）は著者版のみ無料である点に注意が必要である．
- **事例ベース資料の質が高い**．1936年Literary Digest事例は，単純な「悪い標本」の教訓を超えて，重み付け補正による教材化を論じたLohr & Brick（2017）やChanceら（2024）が利用でき，小テスト設計に有用である．Netflix再識別（Narayanan & Shmatikov）は匿名加工の限界を示す決定的事例である．

## Details

### 第1回：データサイエンスとは何か——ビッグデータとThick・Thinデータ

- **William S. Cleveland, "Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics," International Statistical Review, 69(1), 21–26, 2001.** DOI: 10.1111/j.1751-5823.2001.tb00477.x． 「データサイエンス」という語を統計学の拡張分野として提唱した古典．学際性（統計学×情報学×ドメイン）の歴史的起点として導入に最適．複数大学サイトでオープンPDF入手可．
- **David Donoho, "50 Years of Data Science," Journal of Computational and Graphical Statistics, 26(4), 745–766, 2017（初出2015）.** DOI: 10.1080/10618600.2017.1384734． データサイエンスの定義論争・歴史を批判的に概観．オープンPDF（course.ccs.neu.edu にプレプリント版）．データサイエンスと統計学の関係を論じる導入講義の骨格に使える．
- **Vasant Dhar, "Data Science and Prediction," Communications of the ACM, 56(12), 64–73, 2013.** DOI: 10.1145/2500499． CACMによるデータサイエンスの定義的マガジン記事．「なぜ統計学に加えて新語が必要か」を論じ，データ駆動型社会の説明に有用．
- **Longbing Cao, "Data Science: A Comprehensive Overview," ACM Computing Surveys, 50(3), Article 43, 2017.** DOI: 10.1145/3076253． データサイエンスの学際性を「statistics ∩ informatics ∩ computing ∩ communication ∩ sociology ∩ management」と定式化．学際性の図解の出典に．
- **Tricia Wang, "Why Big Data Needs Thick Data"（Ethnography Matters, 2013）** および **Tobias Bornakke & Brian L. Due, "Big–Thick Blending: A Method for Mixing Analytical Insights from Big and Thick Data Sources," Big Data & Society, 5(1), 2018.** DOI: 10.1177/2053951718765026（完全オープンアクセス）． Thick/Thinデータの対比と補完的利用の中心資料．量的で文脈の薄いデータ（Thin）と質的・文脈的データ（Thick）の説明に．Wangの記事はGeertzの「厚い記述」に由来する概念の一次的解説として，学生に親しみやすい．
- **ビッグデータの3V（事例的解説）: Marco Brambilla et al. および各種サーベイ**——3V（Volume・Velocity・Variety）はDoug Laney（Gartner, 2001）が起点．学術的整理としては **"What Is (Not) Big Data Based on Its 7Vs Challenges: A Survey," MDPI Big Data and Cognitive Computing, 6(4), 158, 2022**（DOI: 10.3390/bdcc6040158，オープン）が3V→5V→7Vの拡張を体系的に扱い，講義ノートの背景に使える．
- **医用画像AI事例: Geert Litjens et al., "A Survey on Deep Learning in Medical Image Analysis," Medical Image Analysis, 42, 60–88, 2017.** DOI: 10.1016/j.media.2017.07.005，arXiv:1702.05747（オープン）． 画像診断支援の事例（300超の研究を概観）．社会におけるAI活用事例の導入に．
- **推薦システム事例: Shoujin Wang et al., "A Survey on Session-based Recommender Systems," ACM Computing Surveys, 54(7), Article 154, 2021.** DOI: 10.1145/3465401． マーケティングの推薦システム事例に．他にGNN・会話型など多数のACM CSURサーベイが利用可能．

### 第2回：データの収集

- **Peverill Squire, "Why the 1936 Literary Digest Poll Failed," Public Opinion Quarterly, 52(1), 125–133, 1988.** DOI: 10.1086/269085． 選択バイアス・非回答バイアスの古典的分析．**具体的数値**：Literary Digest誌は約1,000万枚の模擬投票用紙を郵送し，約240万枚が返送された．同誌はLandonが57%で勝利すると予測したが，実際にはRooseveltが約60.8%の得票で大勝し，Landonはメイン・バーモントの2州のみ獲得，選挙人団では523対8の地滑り的勝利であった（Squire 1988）．
- **Sharon L. Lohr & J. Michael Brick, "Roosevelt Predicted to Win: Revisiting the 1936 Literary Digest Poll," Statistics, Politics and Policy, 8(1), 65–84, 2017.** DOI: 10.1515/spp-2016-0006． オープンPDF（gwern.net）． 単純な「悪い標本」の教訓を超え，重み付け補正で予測を改善できたことを示す教材的分析．授業の深掘りに．
- **Beth Chance, Andrew Kerr & Jett Palmer, "Taking the Next Step in Exploring the Literary Digest 1936 Poll," Journal of Statistics and Data Science Education, 32(4), 2024.** DOI: 10.1080/26939169.2024.2395505（オープンアクセス，NSF PARにもPDF）． データ取得・クレンジング・可視化・標本補正まで扱える授業活動の設計例．小テスト（事例判断型設問）作成に直接利用可能．
- **世論調査・ビッグデータのバイアス概説: "Impact of Biases in Big Data," arXiv:1803.00897, 2018.** 1936年および1948年（Dewey defeats Truman）事例を含む選択バイアスの概説．オープン．標本の偏り・選択バイアスの導入に．
- 一次／二次データ，構造化／非構造化データ，標本と母集団の基礎説明は上記の事例資料を軸に，社会調査法・実験計画法への橋渡しに用いる．

### 第3回：データの保存と検索

- **E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM, 13(6), 377–387, 1970.** DOI: 10.1145/362384.362685． リレーショナルデータベースの原典．表・キー・関連づけ・正規化の概念の起点．オープンPDF複数（upenn.edu, umag.cl）．データベース設計の重要性の説明に．
- **Erik Meijer & Gavin Bierman, "A Co-Relational Model of Data for Large Shared Data Banks," Communications of the ACM, 54(4), 49–58, 2011.** DOI: 10.1145/1924421.1924436． SQLとNoSQL（key/value）の数学的双対性を論じるCACM記事．保存の多様化（NoSQL等）の解説に，Coddの延長線上で読ませられる．
- **Mark D. Wilkinson et al., "The FAIR Guiding Principles for Scientific Data Management and Stewardship," Scientific Data, 3, 160018, 2016.** DOI: 10.1038/sdata.2016.18． 研究データ管理（Findable, Accessible, Interoperable, Reusable）の国際的標準．CC BY 4.0で完全オープン．研究データ管理・長期保存・データ品質の中心資料．
- データ品質管理・データセキュリティ（情報漏えい・アクセス管理）・バックアップの導入は，上記FAIR原則を軸に，第7回のNetflix再識別事例（Narayanan & Shmatikov）と関連づけると効果的．

### 第4回：データの前処理

- **Hadley Wickham, "Tidy Data," Journal of Statistical Software, 59(10), 1–23, 2014.** DOI: 10.18637/jss.v059.i10． 整然データ（各変数＝列，各観測＝行，各観測単位＝表）の原典．完全オープン（jstatsoft.org）．前処理・データ整形の中核概念に．
- **Karl W. Broman & Kara H. Woo, "Data Organization in Spreadsheets," The American Statistician, 72(1), 2–10, 2018.** DOI: 10.1080/00031305.2017.1375989． PeerJ Preprints版（DOI: 10.7287/peerj.preprints.3183v2）でオープン入手可．セル結合された表・表記ゆれ・空セル・日付書式などバッドデータの具体例と実務的推奨（一貫性，YYYY-MM-DD，1セル1項目，データ辞書作成など）．事例・小テスト作成に最適．
- **S. S. Stevens, "On the Theory of Scales of Measurement," Science, 103(2684), 677–680, 1946.** DOI: 10.1126/science.103.2684.677． 名義・順序・間隔・比率の4尺度水準の原典．オープンPDF複数（ucmerced.edu, ucla.edu）． 変数の型・尺度水準の説明の出典に．
- **「分析の8割は前処理」の典拠: Steve Lohr, "For Big-Data Scientists, 'Janitor Work' Is Key Hurdle to Insights," The New York Times, 2014年8月17日.** 該当箇所：「Data scientists ... spend from 50 percent to 80 percent of their time mired in this more mundane labor of collecting and preparing unruly digital data, before it can be explored for useful nuggets.」 講義でよく引かれる「8割は前処理」の初出的典拠として引用推奨．なお同種の産業調査（CrowdFlower 2016 Data Science Report）では「データサイエンティストの時間の約60%がデータの整理・清掃に費やされる」と報告されており，数値には幅がある点を補足するとよい．
- 機械可読性（machine-readable）・データクレンジング・前処理の恣意性の議論は，Wickham と Broman & Woo を中心に構成する．

### 第5回：データの分析

- **F. J. Anscombe, "Graphs in Statistical Analysis," The American Statistician, 27(1), 17–21, 1973.** DOI: 10.1080/00031305.1973.10478966． アンスコムの四重奏の原典．平均・分散・相関係数・回帰直線が同一でも分布が全く異なる4データセットにより，記述統計の限界と可視化の重要性を示す．オープンPDF（sjsu.edu）．記述統計と代表値・ばらつきの限界の説明に．
- **Judea Pearl, "The Seven Tools of Causal Inference, with Reflections on Machine Learning," Communications of the ACM, 62(3), 54–60, 2019.** DOI: 10.1145/3241036． 相関と因果の区別（本回の中心テーマ），交絡，因果のはしご（association / intervention / counterfactual）の解説．UCLA著者版（技術報告R-481）でオープン入手可能．ACM版はpaywall．
- **疑似相関の事例: Tyler Vigen, "Spurious Correlations"（tylervigen.com，書籍版 Hachette, 2015）.** 学術論文ではないが，疑似相関の直感的な導入教材・小テストの題材として有効．交絡・見かけの相関の説明に．
- 推測統計の入口・機械学習の入口への橋渡しは，Anscombe（可視化と統計量）とPearl（因果）を軸に構成する．

### 第6回：データの可視化とコミュニケーション

- **Anshul Vikram Pandey, Katharina Rall, Margaret L. Satterthwaite, Oded Nov & Enrico Bertini, "How Deceptive are Deceptive Visualizations?: An Empirical Analysis of Common Distortion Techniques," ACM CHI 2015.** DOI: 10.1145/2702123.2702608． 軸の切り取り（truncated axis）・面積による量の表現・アスペクト比・軸の反転という4つの歪曲技法の実証実験．だますグラフの中心資料．参加者は歪曲グラフで対照条件より58.5%〜129.5%大きく差を知覚したと報告．
- **A. V. Pandey, A. Manivannan, O. Nov, M. Satterthwaite & E. Bertini, "The Persuasive Power of Data Visualization," IEEE Transactions on Visualization and Computer Graphics, 20(12), 2211–2220, 2014.** DOI: 10.1109/TVCG.2014.2346419． 可視化の説得力に関するIEEE VIS/TVCG論文．コミュニケーション手段としての可視化の意義に．
- **Leo Yu-Ho Lo, Ayush Gupta, Kento Shigyo, Aoyu Wu, Enrico Bertini & Huamin Qu, "Misinformed by Visualization: What Do We Learn From Misinformative Visualizations?," Computer Graphics Forum (EuroVis) 41(3), 515–525, 2022.** DOI: 10.1111/cgf.14559． 誤誘導と報告された1,000超の実世界の可視化をオープンコーディングし，74種類の問題からなる分類学を構築（原文：「we open-coded over one thousand real-world visualizations that have been reported as misleading. From these examples, we discovered 74 types of issues and formed a taxonomy of misleading elements in visualizations.」）．軸切り取り（1位），3D（2位），二重軸（4位），面積エンコーディング等の頻度も示す．事例・小テスト作成に有用．オープンPDF．
- **Claire Lauer & Shaun O'Brien, "The Deceptive Potential of Common Design Tactics Used in Data Visualizations," ACM SIGDOC 2020.** DOI: 10.1145/3380851.3416762． だますグラフの類型と実験，説明テキストとの組合せの効果を扱う．
- 基本グラフ（棒・折れ線・散布図・ヒストグラム）とデータ型の対応の説明は，上記実証研究群を背景資料とし，ヒートマップ・地図可視化・ダッシュボード等は各種IEEE VIS論文で補う．

### 第7回：データと法——情報法の基礎

- **Arvind Narayanan & Vitaly Shmatikov, "Robust De-anonymization of Large Sparse Datasets," IEEE Symposium on Security and Privacy (S&P) 2008, pp. 111–125.** DOI: 10.1109/SP.2008.33． 約50万人分のNetflix Prize匿名映画評価データの再識別．**代表的結果**：「加入者の64%については，わずか2件の評価とその日付を知るだけで完全に再識別でき，89%については2件の評価と日付でほぼ50万件から8件以下に絞り込める」．匿名加工情報の限界を示す決定的事例．IEEE S&P 2019で本論文にInaugural "Test of Time" Awardが授与された．オープンPDF（cs.cornell.edu, arXiv:cs/0610105）．匿名加工・仮名加工情報とプライバシーの議論に．
- **Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena, Kristina Lerman & Aram Galstyan, "A Survey on Bias and Fairness in Machine Learning," ACM Computing Surveys, 54(6), Article 115, 1–35, 2021.** DOI: 10.1145/3457607，arXiv:1908.09635（オープンPDF）． バイアスの源泉と公平性の定義の体系的整理．アルゴリズムによる差別・公平性の基礎資料．（注：arXiv初出は2019年，CSUR掲載は2021年．）
- **Frederik J. Zuiderveen Borgesius, Damian Trilling, Judith Möller, Balázs Bodó, Claes H. de Vreese & Natali Helberger, "Should We Worry About Filter Bubbles?," Internet Policy Review, 5(1), 2016.** DOI: 10.14763/2016.1.401． 完全オープンアクセス（CC BY 3.0 DE）． フィルターバブルの実証的根拠を批判的に検討したレビュー．「懸念すべき明確な証拠は乏しい」とする均衡の取れた視座．
- **Eytan Bakshy, Solomon Messing & Lada A. Adamic, "Exposure to Ideologically Diverse News and Opinion on Facebook," Science, 348(6239), 1130–1132, 2015.** DOI: 10.1126/science.aaa1160． 約1,010万人の米国ユーザーを対象に，アルゴリズムより個人の選択が横断的接触をより制限すると示した大規模実証研究．フィルターバブルの実証面に．正式にはオープンアクセスでなく著者版のみ無料（配布時ライセンス確認要）．
- 日本法に関する部分（個人情報保護法，個人情報・仮名加工情報・匿名加工情報の区分，AI学習と著作権）は，**個人情報保護委員会（ppc.go.jp）** および **文化庁「AIと著作権に関する考え方について」等の公式資料**を補助的に用いる（政府公式資料で可）．

### 第8回：生成AIの基礎と知的活動への利用

- **Ashish Vaswani et al., "Attention Is All You Need," Advances in Neural Information Processing Systems (NeurIPS) 30, 2017.** arXiv:1706.03762（オープン）． Transformerの原典．大規模言語モデル（LLM）の仕組み（自己注意機構）の背景に．学部1年生には仕組みの直感的理解（次の語の予測）を補う位置づけで紹介．
- **Emily M. Bender, Timnit Gebru, Angelina McMillan-Major & Shmargaret Shmitchell, "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?," ACM FAccT 2021, pp. 610–623.** DOI: 10.1145/3442188.3445922（オープンPDF）． 学習データ・バイアス・環境コスト・「意味を理解せず統計的に模倣する」という批判的視座．LLMのバイアス・限界の議論に．
- **Lei Huang et al., "A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions," ACM Transactions on Information Systems, 43(2), Article 42, 2025.** DOI: 10.1145/3703155，arXiv:2311.05232（オープン）． ハルシネーションの体系的整理．知識の鮮度・事実性の議論に．
- **Ziwei Ji et al., "Survey of Hallucination in Natural Language Generation," ACM Computing Surveys, 55(12), Article 248, 2023.** DOI: 10.1145/3571730． ハルシネーションの分類のもう一つの標準的サーベイ．
- **Enkelejda Kasneci et al., "ChatGPT for Good? On Opportunities and Challenges of Large Language Models for Education," Learning and Individual Differences, 103, 102274, 2023.** DOI: 10.1016/j.lindif.2023.102274（オープンアクセス）． 大学教育での適切な利用（学習支援・個別化）と剽窃・学術的誠実性のリスクを扱う，教育に焦点を当てた査読論文．レポート作成支援・文献調査・学術的誠実性の議論に最適．
- **Eva A. M. van Dis, Johan Bollen, Willem Zuidema, Robert van Rooij & Claudi L. Bockting, "ChatGPT: Five Priorities for Research," Nature, 614(7947), 224–226, 2023.** DOI: 10.1038/d41586-023-00288-7． 研究・教育における責任ある生成AI利用に関するNatureのコメント記事．著者版PDF入手可（正式にはオープンアクセスでない）．学術的誠実性・情報アクセスの変容の議論に．

## Recommendations
1. **まず古典を骨格に据える（各回の導入）**：Cleveland（第1回），Codd（第3回），Wickham・Stevens（第4回），Anscombe（第5回）を各回の「核」に置き，学部1年生が概念の起源を体感できるようにする．これらはすべてオープンPDFが確実で，Jupyter Bookに直接リンクできる．
2. **事例ベース資料を小テスト（事例判断型設問）に活用する**：1936年Literary Digest（第2回），Netflix再識別（第7回），だますグラフの74分類（第6回）は，「この事例で何が問題か」を問う設問に直結する．特にChanceら（2024）とLoら（2022）は教材化を明示的に意図しており優先度が高い．
3. **オープンアクセスの確実性で配布方法を切り替える**：完全オープン（Wickham，FAIR原則，Stochastic Parrots，Mehrabi arXiv版，Kasneci，Borgesius）はPDFを埋め込み，paywall／著者版のみ（Bakshy=Science，van Dis=Nature，Pandey=IEEE，一部ACM）はDOIリンク提示に留める．
4. **段階的拡張の指標**：受講生の反応（小テスト正答率・アンケート）を見て，理解が浅い回にはサーベイ（Cao，各種CSUR）を追加し，逆に負荷が高すぎる場合は原典を要約スライド化して原典リンクは「発展」に格下げする．具体的な閾値としては，事例判断型設問の正答率が70%を下回る回は事例資料を1本追加，90%を超える回は発展資料へ振り分ける運用が目安．
5. **日本法パートは政府公式資料を主軸に**：第7回の日本法（個人情報保護法，仮名加工・匿名加工情報，AI学習と著作権）は，学術論文より個人情報保護委員会・文化庁の最新公式資料を一次資料とし，海外の学術論文（Narayanan & Shmatikov，Mehrabi）は「なぜ規制が必要か」の理論的背景として位置づける．

## Caveats
- **掲載年の表記ゆれ**：Mehrabiらの公平性サーベイはarXiv初出2019年だがACM Computing Surveys掲載は2021年（54(6), Article 115）である．引用時は掲載版年に統一するとよい．同様にDonohoは2015年プレプリント／2017年正式掲載である．
- **オープンアクセスでない資料**：Bakshyら（Science 2015），van Disら（Nature 2023）は正式にはオープンアクセスでなく，著者版・機関リポジトリ版のみ無料である．Pandeyら（IEEE TVCG 2014）およびPearl（CACM 2019のACM版）もpaywallで，Pearlは UCLA 著者版で代替可能．講義ノートで全文PDFを配布する際は各出版社のライセンスを必ず確認すること．
- **一次典拠の性質の違い**：Tricia Wangの「Thick Data」やTyler Vigenの「Spurious Correlations」，Steve Lohrの New York Times 記事は査読学術論文ではない（それぞれブログ／ウェブサイト／新聞記事）．概念の直感的導入や事例としては極めて有用だが，学術的典拠としては本文中で明示的に「一次的解説／報道」と位置づけ，可能なら査読論文（Bornakke & Due，Anscombe等）と併記することを推奨する．
- **3Vの起点**：ビッグデータの3V（Volume・Velocity・Variety）は学術論文ではなくDoug Laney（Gartner, 2001）の業界メモが起点であり，査読サーベイ（MDPI 7Vサーベイ等）は後付けの整理である点に留意．
- **「8割は前処理」の数値の幅**：この経験則は厳密な学術的推計ではなく，New York Times記事（2014）やCrowdFlower産業調査（2016）由来で「50〜80%」「約60%」など出典により幅がある．講義では「おおむね5〜8割」と幅を持たせて提示するのが誠実である．