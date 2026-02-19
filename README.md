# Teste de Velocidade de Internet

Aplicação Flask para testar a velocidade de internet.

## Requisitos Locais

- Docker
- Docker Compose
- OU Python 3.11+

## Como executar localmente

### Opção 1: Com Docker Compose (Recomendado)

```bash
docker-compose up --build
```

A aplicação estará disponível em: `http://localhost:5000`

### Opção 2: Com Docker direto

```bash
docker build -t speed-test .
docker run -p 5000:5000 speed-test
```

### Opção 3: Sem Docker (Python local)

1. Criar ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instalar dependências:
```bash
pip install -r requirements.txt
```

3. Executar:
```bash
python main.py
```

## Deploy no Render

### Pré-requisitos
- Conta no [Render.com](https://render.com)
- Repositório Git (GitHub, GitLab ou Gitea)

### Passos para Deploy

1. **Commit e push para seu repositório Git:**
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

2. **No Render Dashboard:**
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub
   - Configure:
     - **Name:** `speed-test-app`
     - **Runtime:** Python 3.11
     - **Build command:** `pip install -r requirements.txt`
     - **Start command:** `gunicorn --workers 2 --timeout 600 --bind 0.0.0.0:$PORT main:app`
     - **Plan:** Free (ou pago conforme necessário)

3. **Variáveis de Ambiente (opcional):**
   - `FLASK_ENV` = `production`
   - `FLASK_DEBUG` = `False`

4. **Deploy:**
   - Clique em "Create Web Service"
   - Aguarde o deploy (2-3 minutos)
   - Acesse sua URL pública fornecida pelo Render

### Alternativa: Usar render.yaml

Se tiver um arquivo `render.yaml` no repositório, o Render lerá as configurações automaticamente.

```bash
git push origin main
```

Render detectará `render.yaml` e fará o deploy automaticamente.

## Como usar

1. Acesse a aplicação (local ou Render)
2. Clique em "Verificar Conexão" para testar a conectividade
3. Clique em "Iniciar Teste" para medir a velocidade
4. Aguarde alguns minutos pelo resultado

## Parar a aplicação localmente

Com Docker Compose:
```bash
docker-compose down
```

Com Docker direto:
```bash
docker stop <container_id>
```

## Estrutura da Aplicação

```
.
├── main.py                 # Aplicação Flask principal
├── requirements.txt        # Dependências Python
├── Procfile               # Para deploy no Render/Heroku
├── render.yaml            # Configuração do Render (alternativa)
├── Dockerfile             # Para executar com Docker
├── docker-compose.yml     # Orquestração Docker
├── .env                   # Variáveis de ambiente (local)
├── .gitignore            # Arquivos ignorados no Git
├── .dockerignore         # Arquivos ignorados no Docker
├── README.md             # Este arquivo
└── templates/
    └── index.html        # Interface web
```

## Notas Importantes

- O teste de velocidade pode levar 3-5 minutos
- Requer conexão ativa com a internet
- No Render (plano free), a aplicação pode hibernar após 15 min de inatividade
- Para evitar hibernação, use um plano pago ou um "pinger" externo

## Troubleshooting

### "Erro ao realizar o teste de velocidade"
1. Clique em "Verificar Conexão"
2. Se estiver OK, aguarde e tente novamente
3. Verifique os logs: `docker-compose logs -f web`

### "Sem conexão com internet"
- Verifique sua conexão de internet
- Se estiver no Docker, verifique DNS: `docker-compose exec web nslookup google.com`

### Aplicação lenta no Render
- Plano free tem limitações de recursos
- Considere upgrade para plano pago
- O teste de velocidade é computacionalmente intensivo

## API Endpoints

- `GET /` - Página principal
- `GET /health` - Verificar status e conexão com internet
- `GET /test` - Executar teste de velocidade

Exemplo de resposta `/test`:
```json
{
  "download": 45.23,
  "upload": 12.45,
  "timestamp": "2024-02-19 14:30:00"
}
```
