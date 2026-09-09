# 国赛工作站 setup.ps1 —— 一键落位技能 + 装 Python 依赖 + 生成配置文件
# 用法：powershell -ExecutionPolicy Bypass -File .\setup.ps1
$ErrorActionPreference = "Continue"
$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillsRoot = "$env:USERPROFILE\.agents\skills"
$claudeRoot = "$env:USERPROFILE\.claude\skills"
New-Item -ItemType Directory -Force -Path $skillsRoot,$claudeRoot | Out-Null

Write-Host "== 1. 落位 skills（软链优先，失败自动复制）==" -ForegroundColor Cyan
$nSkills = 0
Get-ChildItem "$repo\skills" -Directory | ForEach-Object {
  $name = $_.Name
  foreach ($root in @($skillsRoot,$claudeRoot)) {
    $dest = Join-Path $root $name
    if (Test-Path $dest) { continue }
    try {
      New-Item -ItemType Junction -Path $dest -Target $_.FullName -ErrorAction Stop | Out-Null
      Write-Host ("  [junction] {0} -> {1}" -f $name,$dest)
      $nSkills++
    } catch {
      New-Item -ItemType Directory -Force -Path $dest | Out-Null
      Copy-Item (Join-Path $_.FullName '*') $dest -Recurse -Force
      Write-Host ("  [copy]     {0} -> {1}" -f $name,$dest)
      $nSkills++
    }
  }
}
Write-Host ("  已落位 {0} 个技能（x2 目录）" -f $nSkills) -ForegroundColor Green

Write-Host "== 2. 安装 Python 依赖 ==" -ForegroundColor Cyan
$req = "$repo\skills\mathmodel-skill\templates\shared\requirements.txt"
if (Test-Path $req) {
  Write-Host "  安装 requirements.txt ..."
  python -m pip install -r $req
} else {
  Write-Host "  未找到 requirements.txt（跳过）"
}
Write-Host "  安装计算补充库 networkx sympy pymoo openpyxl ..."
python -m pip install networkx sympy pymoo openpyxl

Write-Host "== 3. 生成 multi_ai/config.json（无则从示例拷贝）==" -ForegroundColor Cyan
$srcCfg = "$repo\skills\national-award-captain\multi_ai\config.example.json"
$dstCfg = "$skillsRoot\national-award-captain\multi_ai\config.json"
if (-not (Test-Path $dstCfg) -and (Test-Path $srcCfg)) {
  Copy-Item $srcCfg $dstCfg -Force
  Write-Host "  已生成 config.json（本地 CLI 三模型，无需 key）" -ForegroundColor Green
} else {
  Write-Host "  config.json 已存在或示例缺失（跳过）"
}

Write-Host "== 4. 完成 ==" -ForegroundColor Green
Write-Host ""
Write-Host "下一步：" -ForegroundColor Yellow
Write-Host "  · 新开 DeepSeek 会话，说『冲刺国奖 / 开始建模』即用。"
Write-Host "  · 若用 Claude Code，skills 也已落 ~/.claude/skills，同样触发词即可。"
Write-Host "  · 多AI 默认本地 CLI（dsh/claude/codex），无需 API key；未登录会自动降级。"
Write-Host "  · 详细来源/放置/命令见 docs\安装与下载指南.md"
