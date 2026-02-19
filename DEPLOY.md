# Guia de Deploy no Render com Gunicorn

## O que foi preparado

A aplicação está pronta para ser deployada no Render com Gunicorn como WSGI server.

## Arquivos de Configuração

- **Procfile** - Define o comando de start para o Render
- **render.yaml** - Configuração alternativa (mais detalhada) do Render
- **gunicorn_config.py** - Configuração avançada do Gunicorn (opcional)
- **requirements.txt** - Todas as dependências necessárias

## Passo a Passo

### 1. Preparar o Repositório Git Localmente

```powershell
# Inicializar Git (se ainda não for um repo)
git init

# Adicionar todos os arquivos
git add .

# Commit inicial
git commit -m "Aplicação Speedtest com Gunicorn - Pronto para Render"

# Conectar ao repositório remoto (GitHub, GitLab, Gitea)
git remote add origin https://github.com/seu-usuario/seu-repo.git

# Push para o repositório
git branch -M main
git push -u origin main
```

### 2. Conectar ao Render

1. Acesse [render.com](https://render.com)
2. Crie ou faça login na sua conta
3. Clique em "Dashboard"
4. Clique em "New +" menu

### 3. Opção A: Web Service Manual

1. Clique em "Web Service"
2. Selecione "GitHub" ou sua plataforma Git
3. Procure por `speed-test-app` (ou seu repo)
4. Autorize o Render a acessar seu GitHub
5. Selecione o repositório
6. Configure:
   - **Name:** `speed-test-app`
   - **Environment:** `Python 3`
   - **Region:** Escolher mais próximo de você
   - **Branch:** `main`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn --workers 2 --timeout 600 --bind 0.0.0.0:$PORT main:app`
   - **Instance Type:** Free ou Starter
7. Clique em "Create Web Service"
8. Aguarde o deploy (2-3 minutos)

### 4. Opção B: Deploy Automático com render.yaml

1. O repositório já tem `render.yaml`
2. Apenas faça push para GitHub
3. Connect o repositório no Render
4. Render lerá `render.yaml` automaticamente
5. Deploy acontece a cada push para `main`

### 5. Variáveis de Ambiente (Opcional)

No Dashboard do Render:
1. Vá até seu Web Service
2. Clique em "Environment"
3. Adicione (se quiser customizar):
   - `FLASK_ENV` = `production`
   - `FLASK_DEBUG` = `False`

## Detalhes da Configuração

### Gunicorn
- **Workers:** 2 (suficiente para app de teste)
- **Timeout:** 600 segundos (10 minutos para o teste completo)
- **Bind:** Escuta em `0.0.0.0:$PORT` (qualquer interface)

### Memory & CPU
- **Free Plan:** 0.5GB RAM
- **Starter Plan:** 0.5GB RAM com melhor uptime
- **Pro Plan:** 2GB RAM com melhor performance

**Recomendação:** Use Free para testar, Starter para produção.

## Testar o Deploy

Após o deploy estar pronto:

1. Render fornecerá uma URL como: `https://speed-test-app.onrender.com`
2. Abra em seu navegador
3. Clique em "Verificar Conexão"
4. Se OK, clique em "Iniciar Teste"

## Monitoramento

No Render Dashboard:
- Logs aparecem em tempo real
- Veja métricas de CPU/Memória
- Reinicie a aplicação se necessário

## Auto-Redeploy

O Render fará redeploy automático a cada push para `main`:

```powershell
# Fazer uma mudança no código
Edit main.py

# Commit e push
git add main.py
git commit -m "Fix: melhoria na aplicação"
git push origin main

# Render detecta automaticamente e faz redeploy
```

## Dicas Importantes

### Hibernação no Free Plan
- Aplicação hiberna após 15 minutos de inatividade
- Primeira requisição depois de hibernação demora 10-30 segundos
- Solução: usar Free Plan com um "pinger" ou upgrade para Starter

### Teste de Velocidade Lento
- No Free Plan com 0.5GB RAM, o teste pode levar mais tempo
- Considere upgrade para Starter ou Pro
- Ou reduza para 1 worker em alta latência

### Limpar Logs
- Logs no Render limpam automaticamente
- Para análise, use suas ferramentas de logging (Datadog, etc)

## Troubleshooting

### Deploy falha no build
```
Error: pip install failed
```
**Solução:** Verifique `requirements.txt` - todos os pacotes estão escritos corretamente?

### Aplicação inicia mas não funciona
```
Error: Module not found
```
**Solução:** Verify imports em `main.py`. Todos os imports têm pacotes em requirements.txt?

### Teste de velocidade timeout
```
Error: Timeout
```
**Solução:** Aumentar timeout em `Procfile` ou considerar upgrade de plano.

### "Hibernated" - aplicação suspensa
**Solução:** Faça uma chamada para o endpoint `/health` a cada 14 minutos, ou upgrade para Starter.

## Próximos Passos

1. ✅ Git configurado
2. ✅ Requirements.txt completo
3. ✅ Procfile pronto
4. ✅ render.yaml pronto
5. → Conectar Render ao GitHub
6. → Fazer primeiro push
7. → Acompanhar deploy no Render

## Suporte Render

- Documentação: https://render.com/docs
- Status: https://status.render.com
- Email: support@render.com
