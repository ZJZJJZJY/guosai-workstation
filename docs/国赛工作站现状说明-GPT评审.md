# 鍥借禌宸ヤ綔绔欑幇鐘惰鏄庯紙缁?GPT 璇勫锛?
> 浣狅紙GPT锛夊皢浣滀负鏈伐浣滅珯鐨?鍐呭涓庡憟鐜伴【闂?+ 涓ヨ皑澶嶆牳"瑙掕壊銆傝閫氳鏈鏄庯紝浜嗚В绯荤粺鐜扮姸锛岀劧鍚庢寜鏈熬绗?7 鑺傜粰鎴戯紙DeepSeek锛夋垨 Claude 鐨勮礋璐ｄ汉鍥炲纭涓庢剰瑙併€傛湰鏂囦欢鏄?2026-09-07 鏅氱殑蹇収锛圕laude Code 鍒氬畬鎴愪竴杞敼閫狅級銆?
## 1. 绯荤粺鏄粈涔?CUMCM 鍥借禌锛堝浗涓€/鍥戒簩鐩爣锛変笁鏂瑰崗浣滈棴鐜細
- **Claude Code** = 鎬绘寚鎸ワ細stage 0-9 缂栨帓銆佽鏂囧啓浣滀笌鎺掔増銆佺姸鎬佺淮鎶ゃ€?*鍚堝苟鍚勬柟鎰忚骞舵媿鏉?*
- **DeepSeek锛堟垜锛?* = 鏁版嵁涓庢暟鍊奸【闂細鏁版嵁娓呮礂/EDA/鎷熷悎/姹傝В/棰勬祴/浼樺寲/鑱斿悎鐏垫晱搴?鍏ㄩ噺澶嶇畻
- **GPT锛堜綘锛?* = 鍐呭涓庡憟鐜伴【闂?+ 涓ヨ皑澶嶆牳锛堢孩闃燂級

鎵€鏈夐樁娈靛叡鐢?*鍚屼竴椤圭洰鐩綍** + 鍞竴鐘舵€佹枃浠?`state/decision_log.json`锛岄伩鍏嶅垎鍙夈€?
## 2. 浣狅紙GPT锛夌殑瑙掕壊瀹氫箟锛坧ersona锛岃皟鐢ㄦ椂浣滀负 system prompt锛?- **鍐呭涓庡憟鐜伴【闂?*锛坰tage 2/7/8锛夛細妯″瀷璺嚎璁叉竻妤氥€佸垱鏂扮偣/澶嶅悎妯″瀷鍛藉悕銆佸熀绾垮姣斻€佹憳瑕佷簲娈靛紡锛堚墺3 瀹氶噺缁撴灉锛夈€佸浘琛ㄥ瘑搴︿笌瀛楀彿锛堚墺9pt锛夈€佽鏂囧鏈寲锛堝幓 AI 鍛筹級銆?- **涓ヨ皑澶嶆牳/绾㈤槦**锛坰tage 3/5/9锛夛細鍏抽敭灏忛棶鏁板€间笌**瀹樻柟绛旀瀵规爣**銆佸亣璁惧悎鐞嗘€э紙3-7 鏉′笖甯︿緷鎹級銆佺伒鏁忓害鏄惁 **鈮? 鍙傛暟鑱斿悎鎵板姩锛圠HS/Sobol锛岀 OAT锛?*銆佹ā鍨嬩笌瀹炵幇涓€鑷存€с€侀檮褰曚唬鐮佸畬鏁村彲杩愯锛堢己澶?鍙栨秷璇勫璧勬牸锛夈€?
> 涓轰粈涔?涓ヨ皑澶嶆牳"涔熸槸浣犺€岄潪鐙珛鐨?opus5锛欳laude Code 鏈韩鍗?Opus 5锛屽啀璋冨悓鍨嬪彿鍋?鐙珛澶嶆牳"鎷夸笉鍒扮嫭绔嬭瑙掞紙鍚屾ā鍨嬭嚜璇勶級锛涜瘎瀹￠渶瑕?*寮傛瀯妯″瀷**锛屾晠鍚堝苟缁欎綘銆傝繖鏄?Claude 鐨勬槑纭喅绛栵紙`role_division.md` 鏈夎褰曪級銆?
## 3. 鏈€杩戜竴娆￠噸澶ф敼鍔紙Claude Code锛?6:43-17:34锛?澶欰I 灞備粠"**API 缃戝叧锛坅pi.new.bi + gpt5.6sol/opus5 + NEWBI_API_KEY锛?*"鏀逛负"**鏈湴 CLI 涓夋ā鍨?*"锛堥浂 API key锛岀敤 VSCode 鎻掍欢鑷甫璁よ瘉锛夛細
| 閰嶇疆 | 鍊?|
|---|---|
| `deepseek` | 鏈湴 CLI `dsh --profile headless`锛圖eepSeek Harness锛?|
| `claude` | 鏈湴 CLI `claude --print --model opus`锛圕laude Code锛?|
| `gpt` | 鏈湴 CLI `codex exec --ephemeral --sandbox read-only`锛宮odel=`gpt-5.6-sol`锛宖allback=[`gpt-5.6`, `gpt-5.6-codex`] |

鏂板浠ｇ爜锛?- `multi_ai/multi_ai.py`锛欳LI 璋冪敤鍣紙鑷姩鎵?node+bin.js / claude.exe / codex.exe锛夈€乣at capacity/rate limit` 鑷姩鎹㈠鐢ㄦā鍨嬮噸璇曘€丟BK 涓枃杈撳嚭瑙ｇ爜銆佸け璐ヤ紭闆呴檷绾э紙杩斿洖 None锛夈€?- `multi_ai/advise.py`锛?*闃舵鎰熺煡骞惰椤鹃棶鍏ュ彛**鈥斺€擿python advise.py --stage <0-9> --text "..."`
  - stage 璺敱锛?/7/8鈫掑唴瀹归【闂?GPT)锛?/5/9鈫掓暟鎹【闂?DeepSeek)+涓ヨ皑澶嶆牳(GPT) 骞惰锛涘叾浣欓樁娈碘啋鏁版嵁椤鹃棶
  - 杈撳嚭鍚堝苟 JSON锛歚{"stage","advisors":[{"provider","persona","recommendation","enhancements(鈮?)","risk(鈮?)"}],"skipped","degraded","all_enhancements","all_risks"}`
  - 鏌愰【闂け璐ヨ嚜鍔ㄨ烦杩囷紙`degraded=true`锛夛紝涓嶄腑鏂€?
## 4. 璋冪敤鍗忚锛堟瘡娆¤瘎瀹★級
- 杈撳叆锛歚[闃舵 stageN]` + 鏂规/璁烘枃鐗囨锛涗綘鐨勮緭鍑?*蹇呴』鏄弗鏍?JSON** 涓変欢濂楋細
  `{"recommendation":"涓€鍙ヨ瘽鏄庣‘鎺ㄨ崘","enhancements":["鈮?鏉?],"risk":"鈮?鏉℃渶鍙兘闄嶆。椋庨櫓"}`
- 鏂瑰悜缁熶竴銆佸彧琛ュ己涓嶆姮鏉犮€?*绂佹**缁欎袱濂楀绔嬫柟妗堛€佷笉鍋氭棤璋撹京璇併€?- 鎰忚鍐茬獊鐢?Claude 涓€娆″悎骞朵负鍞竴鏂规骞惰褰曞埌 `decision_log.json`銆?
## 5. 鍏抽敭璺緞
- 鎬绘寚鎸ワ細`~.agents\skills\national-award-captain\SKILL.md`锛坄.claude\skills\national-award-captain` 涓?Junction 鍚屾簮锛?- 鑱岃矗娓呭崟 `INVENTORY.md` / 鎺ュ姏鍗忚 `CONNECT.md` / 鍒嗗伐 `multi_ai\role_division.md`
- 澶欰I锛歚multi_ai\{config.json, multi_ai.py, advise.py, personas.md}`
- 鍗侀樁娈靛紩鎿?`~.claude\skills\mathmodel-skill\`锛涘唴瀹瑰簱 `...\math-modeling\`锛涜幏濂栫煡璇?`...\cumcm-award-playbook\`锛涘幓AI鍛?`...\anti-defensive-writing\`
- 鐭ヨ瘑妯″潡锛堜笁骞村浗涓€绮惧崕+钀介€夋暀璁級锛歚...\national-award-captain\addons\{cumcm-essence-2023-2025.md, losing-lessons.md}`
- 缁樺浘锛歚...\styles\{styles.json(10椋庢牸), plot_dispatch.md, render_starter.py}`

## 6. 宸茬煡閬楃暀锛堝皻鏈敹灏撅紝璇勫鏃跺彲瑙侊級
1. `CONNECT.md` 搂4 浠嶅啓鏃с€宎pi.new.bi/NEWBI_API_KEY銆嶁啋 涓庢湰鍦?CLI 鏂规鐭涚浘
2. 浜ゆ帴鎵嬪唽 `鍥借禌宸ヤ綔绔欎氦鎺ユ墜鍐?ClaudeCode.md` 搂4/搂6 鍚屾牱娈嬬暀鏃?API 璇存硶
3. `multi_ai.py` 鏈熬 `__main__` 婕旂ず鍧椾粛鎵撳嵃鏃?fable5/gpt-key
4. `config.example.json` 鏈悓姝?`role`/`fallback_models`
5. `__pycache__/` 鏈竻鐞?> 鍧囦负鏂囨。/婕旂ず灞傦紝涓嶅奖鍝嶈繍琛岋紱寤鸿鐢?Claude 鎴?DeepSeek 鏀跺熬銆?
## 7. 璇蜂綘锛圙PT锛夊仛涓変欢浜?1. **纭鍒嗗伐涓?persona**锛氬唴瀹归【闂?/ 涓ヨ皑澶嶆牳涓や釜瑙掕壊鐨勮亴璐ｄ綘璁ゅ彲鍚楋紵鏈夋病鏈夎鍔犵殑鍏抽敭妫€鏌ョ偣锛堟瘮濡傝繎涓夊勾鍥戒竴纭寚鏍囷細鎽樿涓綅 992 瀛椼€佺粨鏋滃浘 p50=8銆佸紩鐢?鈮?0 鏉?GB/T 7714銆佹鏂?鈮?0 椤电瓑锛夛紵
2. **纭璋冪敤鍗忚**锛歚advise.py` 鐨?JSON 涓変欢濂?+ 闃舵璺敱锛?/7/8 鍐呭銆?/5/9 涓ヨ皑锛夋槸鍚﹀悎鐞嗭紵
3. **瀵?閬楃暀闂"缁欎竴鍙ユ剰瑙?*锛氬摢浜涜淇€佷紭鍏堢骇濡備綍銆?
锛堝洖澶嶄綘鍙互姝ｅ父璇磋瘽锛屼笉蹇呭己鍒?JSON鈥斺€斾綘鏄互璇勫鑰呰韩浠藉闃呰繖浠借鏄庝功鏈韩銆傦級
