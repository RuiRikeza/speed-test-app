#!/bin/bash
# Script para testar localmente com Gunicorn

echo "🚀 Testando aplicação com Gunicorn..."
echo ""

# Verificar se Python está instalado
if ! command -v python &> /dev/null; then
    echo "❌ Python não encontrado. Por favor, instale Python 3.11+"
    exit 1
fi

echo "✅ Python encontrado: $(python --version)"
echo ""

# Criar venv se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python -m venv venv
fi

# Ativar venv
echo "📦 Ativando ambiente virtual..."
source venv/bin/activate 2>/dev/null || venv\Scripts\activate 2>/dev/null

# Instalar dependências
echo "📥 Instalando dependências..."
pip install -r requirements.txt --quiet

echo "✅ Dependências instaladas"
echo ""

# Executar com Gunicorn
echo "🚀 Iniciando Gunicorn..."
echo "📍 Acesse: http://localhost:8000"
echo "⏸️  Pressione CTRL+C para parar"
echo ""

gunicorn --workers 2 --timeout 600 --bind 0.0.0.0:8000 --reload main:app
