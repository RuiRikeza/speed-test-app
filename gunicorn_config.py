import os
import multiprocessing

# Configuração do Gunicorn

# Número de workers
workers = int(os.getenv('GUNICORN_WORKERS', 2))

# Tipo de worker
worker_class = 'sync'

# Timeout para requisições (600 segundos = 10 minutos)
timeout = 600

# Port
bind = f"0.0.0.0:{os.getenv('PORT', 5000)}"

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Performance
keepalive = 5
max_requests = 1000
max_requests_jitter = 100

# Threads por worker (útil para I/O-bound operations como speedtest)
threads = 1
