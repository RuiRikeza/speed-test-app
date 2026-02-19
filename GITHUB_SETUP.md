#!/bin/bash
# Guia rápido: Push para GitHub

# 1. Configurar Git (primeira vez)
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"

# 2. Inicializar repositório (se não tiver feito)
git init

# 3. Adicionar todos os arquivos
git add .

# 4. Fazer commit
git commit -m "Initial commit: Aplicação Speedtest com Gunicorn pronta para Render"

# 5. Renomear branch para main
git branch -M main

# 6. Adicionar repositório remoto
# Substitua SEU-USUARIO e SEU-REPO pela URL do seu repositório
git remote add origin https://github.com/SEU-USUARIO/SEU-REPO.git

# 7. Fazer push
git push -u origin main

# Pronto! Seu código está no GitHub! 🎉
