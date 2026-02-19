
# Script para testar localmente com Gunicorn (Windows)

Write-Host "🚀 Testando aplicação com Gunicorn..." -ForegroundColor Cyan
Write-Host ""

# Verificar se Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python não encontrado. Por favor, instale Python 3.11+" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Criar venv se não existir
if (-not (Test-Path "venv")) {
    Write-Host "📦 Criando ambiente virtual..." -ForegroundColor Cyan
    python -m venv venv
}

# Ativar venv
Write-Host "📦 Ativando ambiente virtual..." -ForegroundColor Cyan
& "venv/Scripts/Activate.ps1"

# Instalar dependências
Write-Host "📥 Instalando dependências..." -ForegroundColor Cyan
pip install -r requirements.txt --quiet

Write-Host "✅ Dependências instaladas" -ForegroundColor Green
Write-Host ""

# Executar com Gunicorn
Write-Host "🚀 Iniciando Gunicorn..." -ForegroundColor Cyan
Write-Host "📍 Acesse: http://localhost:8000" -ForegroundColor Yellow
Write-Host "⏸️  Pressione CTRL+C para parar" -ForegroundColor Yellow
Write-Host ""

gunicorn --workers 2 --timeout 600 --bind 0.0.0.0:8000 --reload main:app
