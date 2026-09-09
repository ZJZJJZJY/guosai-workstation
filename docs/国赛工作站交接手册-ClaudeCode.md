# 鍥借禌宸ヤ綔绔欎氦鎺ユ墜鍐岋紙缁?Claude Code锛?
> 鏈墜鍐屾槸褰撳墠"鍥藉鍐插埡宸ヤ綔绔?鐨勫畬鏁翠氦鎺ヨ鏄庛€傝 Claude Code 閫氳鏈枃浠?+ `INVENTORY.md` + `CONNECT.md` 鍚庢帴绠″崗浣溿€傛潈濞佹柟妗堬細`~.cache\鍥借禌鍗忎綔鏂规涓嶥eepSeek浠诲姟娓呭崟.md`銆?
## 1. 宸ヤ綔绔欐槸浠€涔?鍥寸粫 CUMCM 鍥借禌鍥戒竴/鍥戒簩鏍囧噯鐨勪笁鏂瑰崗浣滈棴鐜細
- **Claude Code**锛堜綘锛? 缂栨帓 + 鍐欎綔 + 璁烘枃/鎽樿/鎺掔増 + 鐘舵€佺淮鎶?- **DeepSeek**锛圖SH/VSCode 鎻掍欢 + `dsh.cmd`锛? 鏁版嵁涓庤绠楋紙娓呮礂/EDA/鎷熷悎/姹傝В/棰勬祴/浼樺寲/鐏垫晱搴?澶嶇畻锛?- **GPT / Codex锛圴SCode 鎻掍欢锛?* = 棣栧腑椤鹃棶锛堝唴瀹瑰憟鐜帮級+ 涓ヨ皑椤鹃棶锛堟暟瀛﹀疄鐜帮級锛屾柟鍚戠粺涓€銆佷竴娆″悎骞躲€佷笉鍞卞弽璋?
鎵€鏈夐樁娈靛叡鐢?*鍚屼竴涓」鐩洰褰?* + 鍞竴鐘舵€佹枃浠?`state/decision_log.json`锛岄伩鍏嶅垎鍙夈€?
## 2. 鍏抽敭璺緞
| 浣滅敤 | 璺緞 |
|---|---|
| 鎬绘寚鎸ュ叆鍙?| `~.agents\skills\national-award-captain\SKILL.md`锛? `~.claude\skills\national-award-captain\SKILL.md`锛孞unction 鍚屼竴濂楋級 |
| 鏂囦欢鑱岃矗娓呭崟 | `...\national-award-captain\INVENTORY.md` |
| 涓夋柟鍗忎綔/鎺ュ姏鍗忚 | `...\national-award-captain\CONNECT.md` |
| 鍗侀樁娈靛紩鎿?| `~.claude\skills\mathmodel-skill\`锛坄references\stage_00..09*.md`锛?|
| 鍐呭/绠楁硶搴?| `~.claude\skills\math-modeling\`锛坄assets\01..07`銆乣references\Outstanding Thesis\`銆乣tools\{pdf,xlsx,paper_search}`锛?|
| 涓撳鍥㈤槦缂栨帓 | `~.claude\skills\top-math-group\` |
| 鑾峰鐭ヨ瘑灞?| `~.claude\skills\cumcm-award-playbook\`锛坄references\five_year_problems.md` 绛夛級 |
| 鍘籄I鍛?| `~.claude\skills\anti-defensive-writing\` + `...\captain\ai-flavor\README.md` |
| 澶欰I 璋冪敤 | `...\captain\multi_ai\{config.json,multi_ai.py,personas.md,role_division.md}` |
| 鍥剧焊椋庢牸 | `...\captain\styles\{styles.json,plot_dispatch.md,render_starter.py}` |
| 鐭ヨ瘑妯″潡 | `...\captain\addons\{cumcm-essence-2023-2025.md,losing-lessons.md,topic_index.md,tooling_route.md}` |
| 璇婃柇 | `...\captain\diagnostics\{pre_checklist.md,post_review.md}` |

## 3. 鏂拌鎶€鑳斤紙`.agents\skills\`锛? 涓紝鍧囧凡娉ㄥ唽锛?`xlsx`锛圓nthropic 瀹樻柟锛夈€乣pdf`锛圓nthropic 瀹樻柟锛夈€乣exploratory-data-analysis`銆乣scikit-learn`銆乣sympy`銆乣networkx`銆乣pymoo`锛堝悗 5 涓細K-Dense scientific-agent-skills 1.4-1.6K 瀹夎閲忥級銆?> 娉ㄦ剰锛氬彧瑁呬簡 `SKILL.md` 涓绘枃浠讹紱`pymoo` **Python 搴撻渶鑷**锛坄pip install pymoo`锛夛紱`scikit-learn` 搴撳悕鐩綍涓?`sklearn`銆?
## 4. 涓夌鍗忓悓鍗忚锛堥噸鐐癸級
- **鍏变韩鐘舵€?*锛歚<椤圭洰鐩綍>\state\decision_log.json`锛堟ā鏉?`mathmodel-skill\templates\shared\decision_log.json`锛夈€傛瘡闃舵缁撴潫鐢?Claude 鏇存柊 `current_stage`/鏍稿績鍐崇瓥/缁撴灉璺緞/寰呭鏍搁」銆?- **鐩綍绾﹀畾**锛歚<椤圭洰鐩綍>\{棰樼洰.pdf, data\raw\, data\clean\, state\, code\, results\, reports\, figures\, paper\}`銆?- **DeepSeek 鍙啓** `code/ results/ reports/ figures/`锛屼笉鐩存帴鏀硅鏂囩粨璁猴紱璁烘枃鏁板瓧鍞竴鏉ユ簮 = `results\final_results_manifest.json` 涓櫥璁颁负 `accepted` 鐨勬渶缁堢粨鏋滄枃浠躲€?- 鍐欎綔鍓嶈繍琛?`multi_ai\validate_manifest.py` 鏍￠獙 manifest 涓殑鏂囦欢璺緞銆乤ccepted 鐘舵€佸拰涓夋柟澶嶆牳璁板綍銆?- **DeepSeek 浜ゆ帴鏍煎紡**锛堟瘡浠诲姟蹇呭甫锛夛細浠诲姟缂栧彿 / 杈撳叆鏂囦欢 / 鎵ц鑴氭湰 / 杈撳嚭鏂囦欢 / 鍏抽敭缁撴灉 / 璇樊路鏀舵暃鎸囨爣 / 闅忔満绉嶅瓙 / 澶嶇幇鍛戒护 / 寰?Claude路GPT 澶嶆牳椤广€?- **澶欰I 璋冪敤**锛歚multi_ai.py` + `advise.py` 浣跨敤 VSCode 鎻掍欢鏈湴 CLI锛欴eepSeek 涓?`dsh --profile headless`锛孋laude 涓?`claude --print`锛孏PT 涓?`codex exec`銆侰CSwitch 浠呬綔涓浆閰嶇疆锛屼笉鏄皟鐢ㄥ櫒鍏ュ彛銆傝緭鍑?JSON 涓変欢濂楋細`{"recommendation","enhancements"(鈮?),"risk"(鈮?)}`銆侰LI 鏈櫥褰?澶辫触 鈫?璺宠繃骞堕檷绾э紙鍗曟ā鍨?L1 璇勫锛夛紝涓嶄腑鏂€?
## 5. 宸ヤ綔娴侀樁娈?鈫?鎶€鑳介€熸煡
| 闃舵 | 鐢?|
|---|---|
| 0-1 鏁版嵁 | `pdf` `xlsx` `exploratory-data-analysis` + `math-modeling` |
| 2-3 閫夊瀷 | `scikit-learn` `sympy` `networkx` `pymoo` + 绠楁硶搴?+ `model_catalog.md` |
| 4-5 姹傝В | 鍚屼笂 + `scientific-toolkit-skill` + `code_starter\` |
| 6 鐏垫晱搴?| SALib锛堝簱锛? LHS/Sobol 鎵嬪啓锛堝鍙橀噺鑱斿悎锛岀 OAT锛?|
| 7 鍥捐〃 | `matplotlib` `figura` `nature-figure` + `styles\plot_dispatch.md` + `render_starter.py` |
| 8 璁烘枃 | `research-writing-skill` `nature-writing/polishing/citation` `docx` `office-academic-skill` `anti-slop` `anti-defensive-writing` |
| 9 缁堝 | `verification-before-completion` + 鐭ヨ瘑妯″潡 + `diagnostics\post_review.md` + `multi_ai` |

## 6. 鐜鍓嶆彁
- Python 搴撳凡瑁咃細`networkx` `sympy` `openpyxl`锛堝強 numpy/scipy/pandas/matplotlib/cvxpy/pulp/sklearn/xgboost/lightgbm/SALib 绛夛紝鍏ㄩ噺瑙?`mathmodel-skill\templates\shared\requirements.txt`锛夛紱`pymoo` 寰呰銆?- LaTeX锛氬浗璧?鐢靛伐鏉?`xelatex`锛堟ā鏉?`mathmodel-skill\templates\latex\cumcm\cumcmthesis\`锛夛紝缇庤禌 `pdflatex`锛坄templates\latex\mcm\main.tex`锛夈€?- 澶欰I锛氫笁涓?VSCode 鎻掍欢鍒嗗埆绠＄悊璁よ瘉锛涜皟鐢ㄥ櫒涓嶈姹傝缃?`NEWBI_API_KEY`銆備换涓€ CLI 鏈櫥褰曟垨涓嶅彲鐢ㄦ椂鑷姩闄嶇骇銆?- Junction 宸插缓锛歚.claude\skills\national-award-captain` 鈫?`.agents\skills\...`锛堟敼涓ょ鍚屾锛夈€?
## 7. 缁欎綘鐨勭涓€涓姩浣?1. 璇?`INVENTORY.md` + `CONNECT.md` + 鏈墜鍐岋紙5 鍒嗛挓鍐咃級銆?2. 纭涓€涓?`<椤圭洰鐩綍>`锛堟斁棰樼洰 PDF + 闄勪欢锛夊苟鍒濆鍖?`state\decision_log.json` 鈫?瀹屾垚棰樼洰鎷嗚В锛坰tage 0-2锛夈€?3. Claude 涓?GPT 鑱斿悎褰㈡垚妯″瀷璺嚎鍜屽垱鏂扮偣鍐崇瓥鍗★紝鍏堝悜鐢ㄦ埛纭锛屽啀缁?DeepSeek 涓嬪彂鏁版嵁娓呮礂/EDA/鍩虹嚎瀹為獙浠诲姟锛涙帴鏀剁粨鏋滃悗鍐欏叆 `code\results\reports\figures\` 骞剁櫥璁?manifest銆?4. 鍏抽敭灏忛棶鏁板€煎厛涓庡畼鏂圭瓟妗堝鏍囷紝鍐嶈繘璁烘枃锛泂tage 8 鎴愮鍚庢墽琛?8B `ai-flavor` 鍘籄I鍛筹紱stage 9 鎸夆€淒eepSeek 澶嶇畻 鈫?manifest 鐧昏 鈫?Claude 鏇存柊璁烘枃 鈫?GPT/Claude 缁堝鈥濇墽琛屻€?