# main.py
from webhook import app


# Definir ruta raíz
@app.route('/')
def home():
    return 'Wow Flask está funcionando Botme listo!'


if __name__ == "__main__":
    app.run(port=8001, debug=True)
