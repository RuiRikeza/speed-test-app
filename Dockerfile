# Usar imagem Python oficial
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    net-tools \
    dnsutils \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar arquivos da aplicação
COPY . .

# Expor porta
EXPOSE 5000

# Variáveis de ambiente para Flask
ENV FLASK_APP=main.py
ENV FLASK_DEBUG=False
ENV PYTHONUNBUFFERED=1

# Comando para executar a aplicação
CMD ["python", "-u", "main.py"]
