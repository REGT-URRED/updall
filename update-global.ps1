<#
.SYNOPSIS
  Actualizador global de ContextBase para agentes de codigo.

.DESCRIPTION
  Punto unico de entrada (single entrypoint) para actualizar la integracion de
  ContextBase (memoria tecnica autonoma de agentes) en cualquier instalacion.

  Ejecuta el ciclo completo de mantenimiento:
    1. contextbase doctor --fix   -> Diagnostico + reparacion automatica.
    2. contextbase install-skill  -> Skills + registro MCP en homes globales detectados.
    3. contextbase sync           -> Reinyecta reglas de agentes y bloque tecnico.
    4. contextbase guard          -> Integridad de archivos base (+ reparacion).
    5. contextbase status --check -> Chequeo final de estado / drift.

  Cada subcomando de ContextBase solo actua sobre los agentes presentes en la
  maquina (OpenCode, Kilo Code, Claude Code, Antigravity/Gemini, .agents, etc.),
  asi que el actualizador se adapta solo: si el equipo tiene mas o menos
  herramientas instaladas, solo se actualiza lo que detecta.

.PARAMETER RepoRoot
  Carpeta del proyecto contextbase. Por defecto: carpeta donde vive este script.

.PARAMETER ContextBaseBin
  Ruta al CLI de ContextBase (contextbase.js). Por defecto: ruta global de npm.

.PARAMETER DryRun
  Ejecuta la fase de diagnostico mostrando los comandos sin mutar nada.

.EXAMPLE
  .\update-global.ps1

.EXAMPLE
  .\update-global.ps1 -RepoRoot "D:\PROCESO\updall"

.NOTES
  Requiere Node.js (runtime del CLI de ContextBase) y PowerShell 5+ / PowerShell 7+.
  En Windows puede necesitar: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#>
[CmdletBinding()]
param(
  [string]$RepoRoot,
  [string]$ContextBaseBin,
  [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

function Get-ContextBaseScriptPath {
  if ($ContextBaseBin) { return $ContextBaseBin }
  if ($env:CONTEXTBASE_BIN) { return $env:CONTEXTBASE_BIN }
  $candidates = @(
    (Join-Path $env:USERPROFILE 'AppData/Roaming/npm/node_modules/contextbase/bin/contextbase.js'),
    (Join-Path $HOME 'AppData/Roaming/npm/node_modules/contextbase/bin/contextbase.js')
  )
  foreach ($candidate in $candidates) {
    if ($candidate -and (Test-Path $candidate)) { return $candidate }
  }
  return $null
}

function Invoke-ContextBase {
  param([string[]]$Arguments, [switch]$DryRun)
  $scriptPath = Get-ContextBaseScriptPath
  if (-not $scriptPath) {
    throw 'ContextBase CLI no encontrado. Instalalo con: npm install -g contextbase'
  }
  if ($DryRun) { Write-Host "    contextbase $($Arguments -join ' ')"; return 0 }
  $nodeExe = (Get-Command node -ErrorAction SilentlyContinue).Source
  if (-not $nodeExe) { $nodeExe = 'C:\Program Files\nodejs\node.exe' }
  $lines = & $nodeExe $scriptPath @Arguments
  if ($lines) { foreach ($line in @($lines)) { Write-Host $line } }
  return $LASTEXITCODE
}

function Invoke-Step {
  param([string]$Title, [string[]]$Arguments, [switch]$DryRun)
  Write-Host "`n==> $Title"
  Write-Host "    contextbase $($Arguments -join ' ')"
  if ($DryRun) { Write-Host '    [dry-run] sin ejecutar.'; return 0 }
  $code = Invoke-ContextBase -Arguments $Arguments -DryRun:$DryRun
  if ($code -ne 0) { Write-Warning "    contextbase $($Arguments -join ' ') devolvio codigo $code" }
  return $code
}

if (-not $RepoRoot) { $RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path }
if (-not (Test-Path (Join-Path $RepoRoot 'contextbase'))) {
  Write-Warning "No se encontro el contexto base en: $RepoRoot"
}

if ($DryRun) {
  Write-Host 'DRY RUN: no se ejecutara ningun comando de ContextBase.'
  exit 0
}

$failed = $false

$code = Invoke-Step -Title 'ContextBase Doctor (diagnostico y reparacion automatica)' -Arguments @('doctor', '--fix')
if ($code -ne 0) { $failed = $true }

$code = Invoke-Step -Title 'ContextBase Install-Skill (skills y registro MCP)' -Arguments @('install-skill')
if ($code -ne 0) { $failed = $true }

$code = Invoke-Step -Title 'ContextBase Sync (sincronizacion de reglas de agentes)' -Arguments @('sync')
if ($code -ne 0) { $failed = $true }

$code = Invoke-Step -Title 'ContextBase Guard (integridad de archivos base)' -Arguments @('guard')
if ($code -ne 0) { $failed = $true }

$code = Invoke-Step -Title 'ContextBase Status (chequeo final de estado)' -Arguments @('status', '--check')
if ($code -ne 0) { $failed = $true }

Write-Host ''
if ($failed) {
  Write-Host 'RESULTADO: el actualizador detecto problemas durante el ciclo.' -ForegroundColor Yellow
  Write-Host 'Revisa los pasos fallidos arriba y vuelve a ejecutar el actualizador.' -ForegroundColor Yellow
  exit 1
}

Write-Host 'RESULTADO: actualizacion global de ContextBase completada sin errores.' -ForegroundColor Green
exit 0
