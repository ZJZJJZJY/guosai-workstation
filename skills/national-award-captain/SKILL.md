---
name: national-award-captain
description: 鍥藉鍐插埡鎬绘寚鎸ャ€傛暟瀛﹀缓妯＄珵璧涚鍒扮缁熶竴鍏ュ彛锛氫富鏀?CUMCM 鍥借禌锛堝吋瀹?MCM/ICM銆佺數宸ユ澂锛夛紝鏁村悎 mathmodel-skill锛?0闃舵寮曟搸锛? math-modeling锛堝唴瀹?绠楁硶搴擄級+ top-math-group锛堜笓瀹跺洟闃燂級+ cumcm-award-playbook锛堣幏濂栨敾鐣ワ級+ anti-defensive-writing锛堝幓AI鍛筹級锛屽苟鏂板 VSCode 鏈湴澶欰I鍗忎綔锛圖eepSeek 鏁版嵁銆丆laude 缂栨帓銆丟PT 鍛堢幇涓庣粓瀹★級銆佹枃鐚绱€侀珮绾х粯鍥鹃鏍煎簱銆佽禌鍓嶈禌鍚庤瘖鏂€佽繎涓夊勾鍥戒竴绮惧崕涓庤惤閫夋暀璁€傝Е鍙戯細鏁板寤烘ā銆佹暟妯°€佸浗璧涖€丆UMCM銆佺編璧涖€丮CM銆両CM銆佺數宸ユ澂銆佸啿鍒哄浗濂栥€佸缓妯″垎鏋愩€佸缓妯℃眰瑙ｃ€佹暟妯¤鏂囥€佹壘璁烘枃銆佸幓AI鍛炽€侀珮绾х敾鍥俱€佺瓟杈㏄PT銆佽瘖鏂鐩樸€?---

# national-award-captain 鈥?鍥藉鍐插埡鎬绘寚鎸?
鍙紪鎺掞紝涓嶅鍒躲€傚簳灞傝兘鍔涚敱寮曠敤寮曟搸鎻愪緵锛涙湰鎶€鑳芥彁渚涘叆鍙ｃ€佽皟搴︿笌鏂板缁勪欢銆?
## 鐩綍绾﹀畾
- `<captain>` = 鏈妧鑳界洰褰?- `<mm>` = `~.claude\skills\mathmodel-skill`锛?0 闃舵杩囩▼寮曟搸锛?- `<mmd>` = `~.claude\skills\math-modeling`锛堝唴瀹?绠楁硶/璁烘枃璧勬簮锛?- `<tmg>` = `~.claude\skills\top-math-group`锛堜笓瀹跺洟闃熺紪鎺掞級
- `<playbook>` = `~.claude\skills\cumcm-award-playbook`锛堣幏濂栫煡璇嗗眰锛?- `<adw>` = `~.claude\skills\anti-defensive-writing`
- `<cwd>` = 鐢ㄦ埛宸ヤ綔鐩綍锛沗<comp>` = cumcm | mcm | diangong

## 妯″紡
| 妯″紡 | token 棰勭畻 | 鍙嶉 | 閫傜敤 |
|---|---|---|---|
| sprint锛堥粯璁わ級 | 鈮?50k | L1 + 鍏抽敭鑺傜偣 L2锛涘AI 鎸夐渶 | 璺濇瘮璧?2-6 鍛?|
| full | 鈮?00k | L1+L2+L3+L4+red-team | 鏃堕棿鍏呰 / 鎻愪氦鍓嶇粓瀹?|

妯″紡鑷姩鎺ㄨ崘锛氬墿浣?>60h 鈫?full锛?-24h 鈫?sprint + champion 缁堝锛?6h 鈫?鐩存帴杩?stage 9銆?
## 鎰忓浘璺敱锛堝厛鍒嗘祦锛屽啀璧版祦绋嬶級
| 鐢ㄦ埛瑕佷粈涔?| 璧板摢 |
|---|---|
| 瀹屾暣寤烘ā/鍐插埡鍥藉 | `<tmg>` 缁熶竴娴佹按绾匡紙stage 0-9锛夛紝鎸変笅鏂?姣忛樁娈垫敞鍏? |
| 鍙眰妯″瀷/绠楁硶鎺ㄨ崘 | `<mm>/references/model_catalog.md` + `<mmd>/assets/README.md` |
| 鍙啓璁烘枃/娑﹁壊/寮曠敤 | 璺?stage 8锛歚<mm>/references/stage_08_writing.md` + nature-writing/polishing/citation |
| 鎵剧浉鍏宠鏂?| `search/README.md` |
| 鍘籄I鍛?| `ai-flavor/README.md` |
| 楂樼骇鐢诲浘 | `styles/plot_dispatch.md`锛堝彲涓嶈窇鍏ㄦ祦绋嬶級 |
| 绛旇京 PPT | nature-paper2ppt |
| 璇婃柇/澶嶇洏 | `diagnostics/pre_checklist.md`锛堣禌鍓嶏級鎴?`post_review.md`锛堣禌鍚庯級 |

## Quick Start锛堢敤鎴疯"寮€濮嬪缓妯?鍐插埡鍥藉"锛?1. 涓€娆℃€?5 闂細绔炶禌锛堥粯璁?cumcm锛? 棰樺彿 / 闃熷憳鍒嗗伐 / 鎴鏃堕棿 / 棰樼洰 PDF 璺緞銆?2. 鍒濆鍖栨垨璇诲彇 `<cwd>/state/decision_log.json`锛堟ā鏉?`<mm>/templates/shared/decision_log.json`锛涘啓鍏?competition锛夈€?3. 鍔犺浇 `<playbook>` 鑾峰鐐归€熸煡涓€娆★紙寤虹珛鍩虹嚎锛夛紝杩涘叆 `<tmg>` stage 0銆備笉閲嶅闂凡闂繃鐨勯棶棰樸€?
## 姣忛樁娈垫敞鍏ワ紙sprint 寮哄寲锛?- stage 1-3锛歚<playbook>` 鑾峰鐐归€熸煡鈥斺€旀憳瑕?5 娈靛紡涓烘渶楂樻潬鏉嗭紱閫夊瀷 鈮? 涓粨鏋勬€т笉鍚屽€欓€夊仛 PK锛涙瘡瀛愰棶 鈮? 鍩虹嚎瀵规瘮銆?- stage 5锛氬叧閿皬闂粨鏋滀笌瀹樻柟绛旀/鐜板疄瀵规爣锛堢渷涓€鎺ㄥ浗鎺夋。澶村彿鍘熷洜锛夈€?- stage 6锛氱伒鏁忓害鍋氬鍙橀噺鑱斿悎鎵板姩锛堚墺3 鍙傛暟锛孡HS/Sobol锛夛紝闈?OAT銆?- stage 8锛氳 `<mm>/competitions/<comp>/{winning_patterns, phrase_bank, abstract_template, paper_skeleton}.md` + `addons/cumcm-essence-2023-2025.md` 瀵圭収锛涙枃鐚粡 `search/README.md` 鑾峰彇銆?- stage 8 瀛愭楠?8B锛歚ai-flavor/README.md` 杞诲害锛堣繍琛?`<adw>`锛氬垹闃插尽寮忓啓浣?hedge/閬撴瓑妗嗘灦锛宑laim 鍓嶇疆锛夛紱鐘舵€佷粛淇濇寔 `current_stage: 8`銆?- stage 9锛氬厛鐢?DeepSeek 鍏ㄩ噺澶嶇畻骞剁櫥璁?`results/final_results_manifest.json`锛屽啀鐢?Claude 鏇存柊璁烘枃锛屾渶鍚庣敤 GPT + Claude 鑱斿悎缁堝銆?
## 澶欰I锛堝彲閫夛紝浼橀泤闄嶇骇锛夆€?缁熶竴涓撳椤鹃棶鍥紝鏂瑰悜涓€鑷?瑙?`multi_ai/README.md` 涓?`multi_ai/role_division.md`銆侱eepSeek Harness = 鏁版嵁涓庢暟鍊奸【闂紝Claude Code = 鎵ц涓庡啓浣滅紪鎺掞紝GPT/Codex = 鍐呭涓庡憟鐜伴【闂紱涓夎€?*鍙ˉ寮轰笉鎶潬**锛屾剰瑙佸啿绐佺敱 Claude 涓€娆℃€у悎骞舵垚**鍞竴**鏂规锛堜笉杈╄锛夈€傛湰鍦?CLI 涓嶅彲鐢ㄦ垨璋冪敤澶辫触 鈫?璺宠繃骞惰褰曡鍛婏紝鍗曟ā鍨?L1 璇勫缁х画锛屼笉涓柇銆?
## 鍔犺浇鍗忚锛堢渷 token锛?- 鍙湪杩涘叆闃舵 N 鏃惰 `<mm>/references/stage_NN_*.md`锛涗弗绂佷竴娆″叏璇汇€?- `addons/` 鎸夐渶璇伙紱`styles/` 浠呯敾鍥炬椂璇伙紱`search/` 浠呮壘璁烘枃鏃惰锛沗multi_ai/` 浠呰瘎瀹℃椂璇汇€?- 姣忛樁娈靛紑澶磋銆佺粨灏惧啓 `<cwd>/state/decision_log.json`锛堟牳蹇冨喅绛?+ 5 缁磋瘎鍒?+ current_stage+1锛夈€?
## 璺緞鏂摼鍏滃簳
- `<mm>` / `<mmd>` / `<tmg>` / `<playbook>` / `<adw>` 浠讳竴涓嶅瓨鍦?鈫?鎻愮ず"璇烽噸鏂板畨瑁呭搴旀妧鑳?锛屼笉浣跨敤娈嬬己娴佺▼銆?- addons/ 鎴?styles/ 鏂囦欢缂哄け 鈫?璺宠繃瀵瑰簲澧炲己骞舵彁绀猴紝涓嶄腑鏂富娴佺▼锛堢煡璇嗘ā鍧楃己澶辨椂 stage 8 鍥為€€鐢?`<playbook>` 鑾峰鐐归€熸煡锛涢鏍煎簱缂哄け鏃跺洖閫€ nature-figure/matplotlib 榛樿锛夈€?- Python 鐜缂哄け 鈫?鎻愮ず `addons/env_setup.md` 瀹夎渚濊禆锛涚粯鍥鹃檷绾?matplotlib 鍩虹鐢绘硶銆?