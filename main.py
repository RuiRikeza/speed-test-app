
import speedtest
import time
from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

def medir_velocidade_internet():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    
    return download_speed, upload_speed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test_speed():
    download_speed, upload_speed = medir_velocidade_internet()
    return jsonify({
        'download': round(download_speed, 2),
        'upload': round(upload_speed, 2),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
