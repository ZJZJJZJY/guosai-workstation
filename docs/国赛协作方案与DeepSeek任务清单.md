# 鏁板寤烘ā鍥借禌鍗忎綔鏂规涓?DeepSeek 浠诲姟娓呭崟

## 1. 鍗忎綔鐩爣

鐩爣鏄洿缁?CUMCM 鍥借禌鍥戒竴/鍥戒簩鏍囧噯锛屽舰鎴愨€淐laude 缂栨帓涓庡啓浣?+ DeepSeek 鏁版嵁璁＄畻 + GPT 棣栧腑椤鹃棶妫€鏌モ€濈殑闂幆銆傛墍鏈夐樁娈靛叡鐢ㄥ悓涓€涓」鐩洰褰曞拰 `state/decision_log.json`锛岄伩鍏嶆ā鍨嬨€佷唬鐮佸拰璁烘枃鐗堟湰鍒嗗弶銆?
鏈満鎬绘寚鎸ユ妧鑳藉叆鍙ｏ細

`~.agents\skills\national-award-captain\SKILL.md`

鎺ュ姏鍗忚锛?
`~.agents\skills\national-award-captain\CONNECT.md`

## 2. 涓夋柟鍒嗗伐

### GPT锛堥甯【闂級

- 鎶婃ā鍨嬭矾绾胯娓呮锛岀‘淇濆悇灏忛棶涔嬮棿閫昏緫缁熶竴銆?- 妫€鏌ュ垱鏂扮偣銆佸鍚堟ā鍨嬪懡鍚嶃€佸熀绾垮姣斿拰瀹氶噺缁撴灉瀵嗗害銆?- 妫€鏌ユ憳瑕佹槸鍚﹂噰鐢ㄤ簲娈靛紡锛氳儗鏅笌鐩爣銆佹柟娉曘€佸叧閿粨鏋溿€佺粨璁恒€佹帹骞?灞€闄愩€?- 妫€鏌ュ浘琛ㄦ槸鍚﹁冻澶熴€佸瓧鍙锋槸鍚︿笉灏忎簬 9 pt銆侀厤鑹叉槸鍚﹂€傚悎璁烘枃銆?- 涓?Claude 鑱斿悎鍋氭渶缁堟纭€ф鏌ワ細棰樻剰銆佸亣璁俱€佸叕寮忋€佷唬鐮併€佺粨鏋溿€佸浘琛ㄥ拰缁撹閫愰」瀵瑰簲銆?
### Claude

- 璐熻矗 stage 0鈥? 鐨勬祦绋嬬紪鎺掑拰椤圭洰鐘舵€佺淮鎶ゃ€?- 璐熻矗璁烘枃姝ｆ枃銆佹憳瑕併€佸浘琛ㄨ鏄庛€佹ā鍨嬭В閲婂拰鏈€缁堟帓鐗堛€?- 璐熻矗鎶?DeepSeek 鐨勮绠楃粨鏋滃啓鍥炵粺涓€椤圭洰鐩綍锛屽苟纭繚璁烘枃鍙娇鐢ㄥ凡楠岃瘉鏁板瓧銆?
### DeepSeek锛圴SCode DeepSeek Harness 鎻掍欢锛?
- 璐熻矗鏁版嵁娓呮礂銆佹帰绱㈡€х粺璁°€佸弬鏁版嫙鍚堛€佹暟鍊兼眰瑙ｃ€侀娴嬨€佷紭鍖栧疄楠屽拰鏁忔劅鎬у垎鏋愩€?- 姣忛」浠诲姟蹇呴』杈撳嚭鍙鐜颁唬鐮併€佽緭鍏ユ枃浠惰鏄庛€佽緭鍑烘枃浠躲€佸叧閿腑闂寸粨鏋滃拰璇樊/鏀舵暃鎸囨爣銆?- 涓嶇洿鎺ユ敼璁烘枃缁撹锛涙墍鏈夊叧閿暟瀛楃敱 Claude 鍜?GPT 澶嶆牳鍚庢墠鑳借繘鍏ユ鏂囥€?
## 3. 鎺ㄨ崘宸ヤ綔娴?
### Stage 0鈥?锛氶鐩笌鏁版嵁鍑嗗

Claude 璇诲彇棰樼洰鍜岄檮浠讹紝寤虹珛椤圭洰鐩綍锛?
`<椤圭洰鐩綍>\棰樼洰.pdf`

`<椤圭洰鐩綍>\data\raw\`

`<椤圭洰鐩綍>\state\decision_log.json`

DeepSeek 浠诲姟锛?
- 璇诲彇骞剁洏鐐规墍鏈夐檮浠舵牸寮忋€佸瓧娈点€佺己澶卞€煎拰寮傚父鍊笺€?- 灏嗗師濮嬫暟鎹浆鎹负 UTF-8 CSV 鎴?XLSX锛屽啓鍏?`<椤圭洰鐩綍>\data\clean\`銆?- 杈撳嚭 `<椤圭洰鐩綍>\data\data_dictionary.xlsx`锛岃鏄庡瓧娈靛惈涔夈€佸崟浣嶃€佺己澶卞鐞嗗拰鏁版嵁鏉ユ簮銆?- 杈撳嚭 `<椤圭洰鐩綍>\reports\eda_report.md`锛屽寘鍚垎甯冦€佺浉鍏虫€с€佸紓甯稿€煎拰鍙敤鏍锋湰閲忋€?
寤鸿 DeepSeek 浠ｇ爜鐩綍锛?
`<椤圭洰鐩綍>\code\01_data_cleaning.py`

`<椤圭洰鐩綍>\code\02_eda.py`

### Stage 2鈥?锛氶棶棰樻媶瑙ｄ笌妯″瀷閫夊瀷

Claude 鎻愮偧姣忎釜灏忛棶鐨勭洰鏍囥€佸彉閲忋€佺害鏉熷拰璇勪环鎸囨爣锛屾彁鍑鸿嚦灏戜笁涓粨鏋勫樊寮傛槑鏄剧殑鍊欓€夋ā鍨嬨€?
GPT 妫€鏌ワ細

- 鏄惁鏈夋竻鏅扮殑涓荤嚎妯″瀷鍜屽熀绾挎ā鍨嬨€?- 鏄惁瀛樺湪鏈虹悊妯″瀷涓庢暟鎹ā鍨嬬殑鍚堢悊缁勫悎銆?- 鍒涙柊鐐规槸鍚﹁惤瀹炲埌鍙橀噺銆佺害鏉熴€佺洰鏍囧嚱鏁版垨绠楁硶姝ラ涓€?
DeepSeek 浠诲姟锛?
- 瀵瑰€欓€夋ā鍨嬭繘琛屽揩閫熷熀绾垮疄楠屻€?- 杈撳嚭鍚勬ā鍨嬬殑璇樊銆佽繍琛屾椂闂淬€佺ǔ瀹氭€у拰閫傜敤鏉′欢瀵规瘮銆?
杈撳嚭浣嶇疆锛?
`<椤圭洰鐩綍>\results\model_baseline_comparison.csv`

`<椤圭洰鐩綍>\reports\model_selection_experiment.md`

### Stage 4鈥?锛氭ā鍨嬫眰瑙ｄ笌鍏抽敭灏忛棶瀵规爣

DeepSeek 璐熻矗鎵ц姝ｅ紡璁＄畻锛?
- 鍙傛暟浼拌銆佸洖褰掓垨鏃堕棿搴忓垪棰勬祴銆?- 绾挎€?鏁存暟/闈炵嚎鎬т紭鍖栧拰鍚彂寮忕畻娉曘€?- 钂欑壒鍗℃礇鎴栫鏁ｄ簨浠朵豢鐪熴€?- 鍏抽敭灏忛棶鐨勬暟鍊肩粨鏋溿€佺疆淇″尯闂淬€佽宸寚鏍囧拰鏀舵暃鏇茬嚎銆?- 涓庨鐩粰瀹氱瓟妗堛€佺幇瀹為噺绾ф垨瀹樻柟璧勬枡杩涜瀵规爣銆?
姣忎釜灏忛棶鍗曠嫭淇濆瓨锛?
`<椤圭洰鐩綍>\code\q1_solution.py`

`<椤圭洰鐩綍>\code\q2_solution.py`

`<椤圭洰鐩綍>\code\q3_solution.py`

`<椤圭洰鐩綍>\results\q1_results.csv`

`<椤圭洰鐩綍>\results\q2_results.csv`

`<椤圭洰鐩綍>\results\q3_results.csv`

`<椤圭洰鐩綍>\reports\numerical_validation.md`

姣忎釜缁撴灉鎶ュ憡蹇呴』鍐欐槑锛氳緭鍏ユ暟鎹増鏈€侀殢鏈虹瀛愩€佸弬鏁般€佺洰鏍囧嚱鏁板€笺€佺害鏉熸弧瓒虫儏鍐点€佽宸寚鏍囧拰杩愯鍛戒护銆?
### Stage 6锛氳仈鍚堢伒鏁忓害涓庣ǔ鍋ユ€?
DeepSeek 鎵ц澶氬彉閲忚仈鍚堟壈鍔紝绂佹鍙仛涓€娆℃敼鍙樹竴涓弬鏁帮紙OAT锛夈€?
- 鑷冲皯閫夋嫨 3 涓叧閿弬鏁般€?- 浣跨敤 LHS 鎴?Sobol 閲囨牱鐢熸垚鑱斿悎鎵板姩缁勫悎銆?- 璁板綍杈撳嚭鍒嗗竷銆佹晱鎰熷害鎸囨暟銆佹渶鍧忔儏褰㈠拰鎺ㄨ崘鍙傛暟鍖洪棿銆?
杈撳嚭浣嶇疆锛?
`<椤圭洰鐩綍>\code\sensitivity_lhs.py`

`<椤圭洰鐩綍>\results\sensitivity_samples.csv`

`<椤圭洰鐩綍>\results\sensitivity_summary.csv`

`<椤圭洰鐩綍>\figures\sensitivity_tornado_or_heatmap.pdf`

`<椤圭洰鐩綍>\reports\sensitivity_analysis.md`

### Stage 7锛氱粨鏋滄眹鎬讳笌鍥捐〃

DeepSeek 鐢熸垚鍘熷缁撴灉琛ㄥ拰鍥撅紝Claude 璐熻矗璁烘枃鍙欎簨锛孏PT 璐熻矗鍛堢幇缁堝銆?
鑷冲皯鍑嗗锛?
- 鐮旂┒娴佺▼鎴栨ā鍨嬫鏋跺浘銆?- 鍘熷鏁版嵁鍒嗗竷/瓒嬪娍鍥俱€?- 鍩虹嚎涓庢渶缁堟ā鍨嬪姣斿浘銆?- 鍙傛暟鎴栧彉閲忓叧绯诲浘銆?- 浼樺寲鍓嶅悗瀵规瘮鍥俱€?- 棰勬祴璇樊鎴栨畫宸浘銆?- 鑱斿悎鐏垫晱搴︾儹鍥?鍒嗗竷鍥俱€?- 鍏抽敭鏂规鐨勫彲琛屽煙鎴?Pareto 鍥撅紙閫傜敤鏃讹級銆?
鍥捐〃鐩綍锛?
`<椤圭洰鐩綍>\figures\`

寤鸿浣跨敤鐨勭粯鍥捐剼鏈ā鏉匡細

`~.agents\skills\national-award-captain\styles\render_starter.py`

### Stage 8锛氳鏂囧啓浣?
Claude 鏍规嵁宸查獙璇佺粨鏋滃畬鎴愶細

- 鎽樿銆侀棶棰橀噸杩般€佹ā鍨嬪亣璁俱€佺鍙疯鏄庛€?- 鍚勫皬闂ā鍨嬪缓绔嬨€佹眰瑙ｃ€佺粨鏋滃垎鏋愬拰鐜板疄瑙ｉ噴銆?- 妯″瀷浼樼偣銆佸叿浣撳眬闄愬拰鎺ㄥ箍鏂瑰悜銆?- 鍙傝€冩枃鐚€侀檮褰曚唬鐮佽鏄庡拰澶嶇幇瀹為獙璇存槑銆?
GPT 妫€鏌ワ細

- 鎽樿鏄惁鍖呭惈鑷冲皯 3 涓畾閲忕粨鏋溿€?- 缁撹鏄惁鑳藉湪琛ㄦ牸鎴栧浘涓壘鍒板搴旇瘉鎹€?- 姣忎釜灏忛棶鏄惁鏈夊熀绾裤€佹牳蹇冪粨鏋滃拰瑙ｉ噴銆?- 璇█鏄惁瀛︽湳銆佺洿鎺ワ紝鏄惁鍒犻櫎绌烘硾濂楄瘽銆?
璁烘枃鏂囦欢寤鸿锛?
`<椤圭洰鐩綍>\paper\鏁板寤烘ā璁烘枃.docx`

`<椤圭洰鐩綍>\paper\鏁板寤烘ā璁烘枃.pdf`

### Stage 9锛氱粓瀹?
GPT 涓?Claude 鑱斿悎妫€鏌ワ細

- 棰樼洰瑕佹眰鏄惁閫愭潯鍥炵瓟銆?- 鍏抽敭鏁板瓧鑳藉惁鐢变唬鐮佸鐜般€?- 鍏紡銆佺鍙枫€佷唬鐮佸彉閲忓拰鍥捐〃鏍囩鏄惁涓€鑷淬€?- 妯″瀷鏄惁鏈夊熀绾垮姣斻€佽宸獙璇佸拰鑱斿悎鐏垫晱搴︺€?- 鎽樿銆佸垱鏂扮偣銆佺己鐐瑰弽鎬濆拰鍙傝€冩枃鐚槸鍚﹁揪鍒板浗濂栧憟鐜版爣鍑嗐€?
DeepSeek 鍙墽琛屾渶缁堝绠楋細

`<椤圭洰鐩綍>\code\run_all.py`

杈撳嚭锛?
`<椤圭洰鐩綍>\reports\reproducibility_check.md`

`<椤圭洰鐩綍>\results\final_recomputed_results.csv`

## 4. VSCode 鎻掍欢涓?CCSwitch 涓浆鍏崇郴

CCSwitch 鍙墽琛岀▼搴忥紙浠呰礋璐ｄ腑杞?鍒囨崲锛夛細

`D:\CCSWITCH\cc-switch.exe`

CCSwitch 鏁版嵁搴擄紙浠呬繚瀛樻彁渚涘晢閰嶇疆锛夛細

`~.cc-switch\cc-switch.db`

VSCode DeepSeek Harness 鎻掍欢鐩綍锛?
`~.vscode\extensions\vithrive.deepseek-harness-vscode-0.8.43`

Claude Code 鎻掍欢鐩綍锛?
`~.vscode\extensions\anthropic.claude-code-2.1.263-win32-x64`

Claude Code 鏈湴鍛戒护锛?
`~AppData\Roaming\npm\claude.cmd`

OpenAI Codex VSCode 鎻掍欢鐩綍锛?
`~.vscode\extensions\openai.chatgpt-26.5903.61454-win32-x64`

Codex 鏈湴鍙墽琛屾枃浠讹細

`~.vscode\extensions\openai.chatgpt-26.5903.61454-win32-x64\bin\windows-x86_64\codex.exe`

DeepSeek Harness 鐨勬湰鍦板懡浠わ細

`~AppData\Roaming\npm\dsh.cmd`

DeepSeek Harness 鎻掍欢閫氳繃 VSCode 鑱婂ぉ妯″瀷 `vendor=dsh` 娉ㄥ唽妯″瀷锛屽苟鏀寔 headless 璋冪敤锛?
`dsh --profile headless "浠诲姟鏂囨湰"`

鏁版嵁搴撲腑鐨勬彁渚涘晢鍚嶇О锛圕CSwitch 涓浆璁板綍锛夛細`DeepSeek`

绔偣锛歚https://api.deepseek.com/anthropic`

褰撳墠妯″瀷鏄犲皠锛?
- `ANTHROPIC_MODEL` 鈫?`deepseek-v4-pro`
- `ANTHROPIC_DEFAULT_OPUS_MODEL` 鈫?`deepseek-v4-pro[1M]`
- `ANTHROPIC_DEFAULT_SONNET_MODEL` 鈫?`deepseek-v4-pro`
- `ANTHROPIC_DEFAULT_HAIKU_MODEL` 鈫?`deepseek-v4-flash`

璁よ瘉浠ょ墝鐘舵€侊細宸查厤缃紱鏈枃浠朵笉璁板綍浠ょ墝鍐呭銆?
娉ㄦ剰锛欳CSwitch 鐨?`is_current` 鍙〃绀哄綋鍓嶄腑杞厤缃紝涓嶅喅瀹氭湰鍦版彃浠惰皟鐢ㄥ櫒浣跨敤鍝釜妯″瀷銆傛寮忎换鍔＄敱 VSCode 鎻掍欢瀵瑰簲鐨?CLI 鎵ц锛汥eepSeek 瀹屾垚鏁版嵁浠诲姟鍚庯紝Claude Code 璇诲彇缁撴灉缁х画鍐欎綔銆?
## 5. 缁熶竴浜ゆ帴瑙勫垯

鍏变韩鐘舵€佹枃浠讹細

`<椤圭洰鐩綍>\state\decision_log.json`

姣忛樁娈电粨鏉熺敱 Claude 鏇存柊 `current_stage`銆佹牳蹇冨喅绛栥€佺粨鏋滄枃浠惰矾寰勫拰寰呭鏍搁」銆侱eepSeek 鍙啓鍏ユ寚瀹氱殑 `code`銆乣results`銆乣reports` 鍜?`figures` 瀛愮洰褰曘€傝鏂囦腑鐨勬暟瀛楀繀椤诲紩鐢ㄧ粨鏋滄枃浠朵腑鐨勬渶缁堢増鏈€?
DeepSeek 杩斿洖缁撴灉鏃堕噰鐢ㄤ互涓嬭褰曟牸寮忥細

```text
浠诲姟缂栧彿锛?杈撳叆鏂囦欢锛?鎵ц鑴氭湰锛?杈撳嚭鏂囦欢锛?鍏抽敭缁撴灉锛?璇樊/鏀舵暃鎸囨爣锛?闅忔満绉嶅瓙锛?澶嶇幇鍛戒护锛?寰?Claude/GPT 澶嶆牳椤癸細
```

## 6. 鍙敤 skills 鐨勪换鍔¤矾鐢?
鎬绘寚鎸ュ叆鍙ｏ細

`~.agents\skills\national-award-captain\SKILL.md`

寤烘ā涓庣畻娉曪細

- `~.agents\skills\math-modeling\SKILL.md`锛氶鐩垎鏋愩€佹ā鍨嬮€夋嫨銆佺畻娉曞簱鍜岃鏂囨鏋躲€?- `~.agents\skills\scientific-toolkit-skill\SKILL.md`锛氱瀛﹁绠椼€佹暟鎹鐞嗗拰 MATLAB/Python 宸ュ叿閾俱€?- `~.agents\skills\scikit-learn\SKILL.md`锛氬洖褰掋€佸垎绫汇€佽仛绫诲拰棰勬祴銆?- `~.agents\skills\pymoo\SKILL.md`锛氬鐩爣浼樺寲涓?Pareto 瑙ｉ泦銆?- `~.agents\skills\sympy\SKILL.md`锛氱鍙锋帹瀵笺€佸叕寮忓寲绠€鍜屾柟绋嬫眰瑙ｃ€?- `~.agents\skills\networkx\SKILL.md`锛氬浘璁恒€佺綉缁滄祦銆佽矾寰勫拰鍖归厤闂銆?
鏁版嵁涓庢枃浠讹細

- `~.agents\skills\exploratory-data-analysis\SKILL.md`锛氶檮浠舵暟鎹洏鐐瑰拰鎺㈢储鎬у垎鏋愩€?- `~.agents\skills\xlsx\SKILL.md`锛欵xcel 闄勪欢璇诲彇銆佹竻娲楀拰缁撴灉琛ㄨ緭鍑恒€?- `~.agents\skills\pdf\SKILL.md`锛氶鐩?PDF銆佸弬鑰冭鏂囧拰闄勪欢鏂囨湰鎻愬彇銆?- `~.agents\skills\docx\SKILL.md`锛氭渶缁堣鏂?Word 鏂囨。鐢熸垚涓庢鏌ャ€?
璁烘枃銆佸浘琛ㄤ笌鏍￠獙锛?
- `~.agents\skills\research-writing-skill\SKILL.md`锛氫腑鏂囨暟妯¤鏂囩粨鏋勫拰璁鸿瘉銆?- `~.agents\skills\nature-writing\SKILL.md`锛氭憳瑕併€佺粨鏋滃彊浜嬪拰瀛︽湳琛ㄨ揪銆?- `~.agents\skills\matplotlib\SKILL.md`锛氶珮璐ㄩ噺鍥捐〃銆?- `~.agents\skills\figura\SKILL.md`锛氳鏂囧浘琛ㄧ殑娓叉煋銆佹鏌ュ拰杩唬銆?- `~.agents\skills\anti-slop\SKILL.md`锛氬幓闄ゆā鏉垮寲銆佺┖娉涘拰 AI 鍛宠〃杈俱€?- `~.agents\skills\verification-before-completion\SKILL.md`锛氱粓绋垮墠楠岃瘉浠ｇ爜銆佺粨鏋滃拰鏂囦欢銆?
璋冪敤瀹炵幇锛?
`~.agents\skills\national-award-captain\multi_ai\multi_ai.py`

鏈湴妯″瀷閰嶇疆锛?
`~.agents\skills\national-award-captain\multi_ai\config.json`

## 7. 鍚姩椤哄簭

1. 纭畾 `<椤圭洰鐩綍>`锛屾斁鍏ラ鐩?PDF 鍜屽師濮嬮檮浠躲€?2. Claude 鍒濆鍖?`state\decision_log.json` 骞跺畬鎴愰鐩媶瑙ｃ€?3. 鍦?VSCode 涓墦寮€ DeepSeek Harness锛屾垨鐢辨湰鍦伴€傞厤鍣ㄨ皟鐢?`dsh.cmd`锛屾墽琛屾暟鎹竻娲椼€佸熀绾垮疄楠屽拰姝ｅ紡姹傝В銆?4. Claude Code 鎻掍欢璇诲彇 DeepSeek 杈撳嚭锛屽畬鎴愯鏂囦笌鍥捐〃鍙欎簨銆?5. GPT 涓?Claude 鍋氳仈鍚堟纭€ф鏌ャ€?6. DeepSeek 鎵ц `run_all.py` 澶嶇畻锛孋laude 淇鏈€缁堢銆?