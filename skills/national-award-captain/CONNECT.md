# CONNECT / 鍗忎綔 鈥?Claude 缂栨帓鍐欎綔 脳 DeepSeek 璁＄畻 脳 GPT 椤鹃棶锛堜笁鏂癸紝鍚屼竴椤圭洰鐩綍锛?
> 渚濇嵁銆婂浗璧涘崗浣滄柟妗堜笌 DeepSeek 浠诲姟娓呭崟銆嬪畾绋跨殑涓夋柟鍒嗗伐锛涙湰鎶€鑳芥槸涓夋柟鍏辩敤鐨勭煡璇?鍏ュ彛搴曞骇銆?
## 涓€銆佷笁鏂瑰垎宸?| 瑙掕壊 | 璋?| 鍏ュ彛 | 骞蹭粈涔?|
|---|---|---|---|
| 缂栨帓+鍐欎綔 | **Claude Code** | `.claude/skills`锛坖unction 鎸囧悜鏈妧鑳斤級+ `claude.cmd` | stage 0-9 娴佺▼缂栨帓銆佽鏂囨鏂?鎽樿/鍥捐〃璇存槑/鎺掔増銆佺淮鎶?`state/decision_log.json`銆佹妸 DeepSeek 楠岃瘉杩囩殑鏁板瓧鍐欏洖璁烘枃 |
| 鏁版嵁+璁＄畻 | **DeepSeek锛堟垜锛?* | DSH 鎻掍欢 `vithrive.deepseek-harness-vscode-0.8.43` / `dsh.cmd` | 鏁版嵁娓呮礂銆丒DA銆佹嫙鍚堛€佹暟鍊兼眰瑙ｃ€侀娴嬨€佷紭鍖栥€佽挋鐗瑰崱娲涖€佽仈鍚堢伒鏁忓害銆佹渶缁堝绠楋紱**鍙啓** `code/ results/ reports/ figures/`锛涗笉鐩存帴鏀硅鏂囩粨璁?|
| 棣栧腑椤鹃棶 | **GPT**锛坓pt5.6sol锛?| `multi_ai/config.json` + personas | 妯″瀷璺嚎銆佸垱鏂扮偣/澶嶅悎鍛藉悕銆佸熀绾垮姣斻€佹憳瑕佷簲娈靛紡銆佲墺3 瀹氶噺缁撴灉銆佸浘琛ㄥ憟鐜扮粓瀹★紱涓?Claude 鑱斿悎姝ｇ‘鎬ф鏌ワ紙棰樻剰/鍋囪/鍏紡/浠ｇ爜/缁撴灉/鍥捐〃/缁撹閫愰」瀵瑰簲锛?|

> GPT/Codex 鐨?`rigor` persona 璐熻矗鏁板涓庡疄鐜颁弗璋ㄦ€у鏍革紙鏁板€煎鏍?鍋囪/鐏垫晱搴?闄勫綍瀹屾暣鎬э級銆?
## 浜屻€佸叡浜姸鎬佷笌鐩綍绾﹀畾锛堜笉鍙橀噺锛?- 椤圭洰鐩綍锛歚<椤圭洰鐩綍>/` 鍚?`棰樼洰.pdf`銆乣data/raw/`銆乣data/clean/`銆乣state/decision_log.json`銆乣code/`銆乣results/`銆乣reports/`銆乣figures/`銆乣paper/`銆?- **state 鍞竴**锛歚<椤圭洰鐩綍>/state/decision_log.json`锛堣捣鐐规ā鏉?`<mm>/templates/shared/decision_log.json`锛夈€傛瘡闃舵缁撴潫鐢?Claude 鏇存柊 `current_stage` + 鏍稿績鍐崇瓥 + 缁撴灉鏂囦欢璺緞 + 寰呭鏍搁」锛涘幓AI鍛充綔涓?stage 8 瀛愭楠?8B锛屼笉鍗曠嫭鍗犵敤 stage 缂栧彿銆?- 璁烘枃涓殑鏁板瓧**鍞竴鏉ユ簮** = `results/` 涓嬬櫥璁板湪 `final_results_manifest.json` 涓旂姸鎬佷负 `accepted` 鐨勬渶缁堢粨鏋滄枃浠躲€?- 鍐欎綔鍓嶈繍琛?`python ~.agents\skills\national-award-captain\multi_ai\validate_manifest.py <椤圭洰鐩綍>\results\final_results_manifest.json --project-root <椤圭洰鐩綍>`锛岄獙璇佷笁鏂瑰鏍稿拰鏂囦欢瀛樺湪鎬с€?
## 涓夈€丏eepSeek锛堟垜锛夌殑浜ゆ帴鏍煎紡锛堟瘡椤逛换鍔″繀甯︼級
```text
浠诲姟缂栧彿锛?杈撳叆鏂囦欢锛?鎵ц鑴氭湰锛?杈撳嚭鏂囦欢锛?鍏抽敭缁撴灉锛?璇樊/鏀舵暃鎸囨爣锛?闅忔満绉嶅瓙锛?澶嶇幇鍛戒护锛?寰?Claude/GPT 澶嶆牳椤癸細
```

## 鍥涖€佽皟鐢ㄤ笌涓浆
- 鎴戠殑鏈湴鍛戒护锛歚~AppData\Roaming\npm\dsh.cmd`锛沨eadless锛歚dsh --profile headless "浠诲姟鏂囨湰"`銆?- Claude Code锛歚~AppData\Roaming\npm\claude.cmd`锛汣odex锛堝彲閫夛級锛歟xtensions\openai.chatgpt-...\bin\windows-x86_64\codex.exe銆?- CCSwitch锛坄D:\CCSWITCH\cc-switch.exe`锛変粎鍋氫腑杞厤缃紝**涓嶅喅瀹?*鎻掍欢璋冪敤鍣ㄧ敤鍝釜妯″瀷锛涙寮忎换鍔＄敱 VSCode 鎻掍欢瀵瑰簲 CLI 鎵ц銆?- 澶欰I 鍏辩敤锛歚multi_ai/config.json`銆侱eepSeek 浣跨敤 `dsh --profile headless`锛孋laude 浣跨敤 `claude --print`锛孏PT 浣跨敤 `codex exec`锛汣CSwitch 浠呭仛涓浆閰嶇疆锛屼笉鏄皟鐢ㄥ櫒鍏ュ彛銆?
## 浜斻€佽 Claude Code 鍔犺浇鍚屼竴濂?captain锛堢洰褰曡仈鎺ワ級
```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\national-award-captain" -Target "~.agents\skills\national-award-captain"
```
- Junction 宸插缓骞跺彲璇伙紙涓ょ鍚屼负 24+ 鏂囦欢锛夛紱鏀逛换涓€绔袱绔悓姝ャ€?
## 鍏€佹敞鎰忎簨椤?- 鏈?DSH 浼氳瘽娌欑**鏃犳硶鎵ц Python** 鈫?鎵归噺"璺戜唬鐮?澶嶇畻"鐢?`dsh --profile headless` 鎴?VSCode DeepSeek Harness 鎵ц锛涗篃鍙敱鎴戜氦浠?*鍙鐜颁唬鐮?+ 鎶ュ憡**锛孋laude Code 渚у鏍歌繍琛屻€?- 鎴戜笉鐩存帴鏀硅鏂囩粨璁猴紱鍏抽敭鏁板瓧涓€寰嬬敱 Claude + GPT 澶嶆牳鍚庤繘姝ｆ枃銆?- state 鍙敤鍚屼竴浠斤紝鍕垮垎鍙夛紱stage 9 蹇呴』鎸夆€淒eepSeek 澶嶇畻 鈫?manifest 鐧昏 鈫?Claude 鏇存柊璁烘枃 鈫?GPT/Claude 缁堝鈥濋『搴忔墽琛屻€傚垏鎹㈠彛璇€锛?*鍚屼竴椤圭洰鐩綍 + 鍚屼竴浠?decision_log.json = 鏃犵紳浜ゆ帴**銆?