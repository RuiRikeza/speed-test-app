
import speedtest
import time
import os
import logging
import socket
from flask import Flask, render_template, jsonify
from datetime import datetime
from threading import Timer

app = Flask(__name__)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_internet():
    """Verifica se há conexão com a internet"""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        logger.info("Conexão com internet verificada")
        return True
    except OSError:
        logger.error("Sem conexão com a internet")
        return False

def medir_velocidade_internet():
    """Realiza o teste de velocidade da internet com tratamento de erros"""
    try:
        # Verificar conexão
        if not check_internet():
            raise Exception("Sem conexão com a internet. Verifique sua conexão.")
        
        logger.info("Iniciando teste de velocidade...")
        
        # Criar instância do Speedtest
        st = speedtest.Speedtest(secure=True)
        logger.info("Instância Speedtest criada com sucesso")
        
        logger.info("Buscando melhor servidor...")
        st.get_best_server()
        logger.info(f"Servidor selecionado: {st.best['sponsor']}")
        
        logger.info("Testando velocidade de download...")
        download_speed = st.download(threads=4) / 1_000_000  # Convert to Mbps
        logger.info(f"Download: {download_speed:.2f} Mbps")
        
        logger.info("Testando velocidade de upload...")
        upload_speed = st.upload(threads=4) / 1_000_000      # Convert to Mbps
        logger.info(f"Upload: {upload_speed:.2f} Mbps")
        
        logger.info(f"Teste concluído - Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")
        return round(download_speed, 2), round(upload_speed, 2)
    
    except speedtest.ConfigRetrievalError as e:
        logger.error(f"Erro ao obter configuração: {str(e)}")
        raise Exception("Erro ao conectar com os servidores de teste. Por favor, tente novamente em alguns momentos.")
    except speedtest.SpeedtestException as e:
        logger.error(f"Erro no teste de velocidade: {str(e)}")
        raise Exception(f"Erro durante o teste: {str(e)}")
    except socket.timeout:
        logger.error("Timeout ao conectar")
        raise Exception("Timeout na conexão. Por favor, tente novamente.")
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}", exc_info=True)
        raise Exception(f"Erro inesperado: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test_speed():
    try:
        logger.info("=== INICIANDO TESTE DE VELOCIDADE ===")
        download_speed, upload_speed = medir_velocidade_internet()
        logger.info("=== TESTE CONCLUÍDO COM SUCESSO ===")
        return jsonify({
            'download': download_speed,
            'upload': upload_speed,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }), 200
    except Exception as e:
        logger.error(f"Erro na rota /test: {str(e)}", exc_info=True)
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/health')
def health():
    """Endpoint para verificar se a aplicação está rodando"""
    internet = check_internet()
    return jsonify({
        'status': 'ok',
        'internet': internet,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }), 200

if __name__ == "__main__":
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False') == 'True'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port, use_reloader=False)
