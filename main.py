from pinescriptgen_core.flask_app import app

# Punto de entrada principal para la app.
# No se debe iniciar la app desde ningun otro archivo que no sea este


if __name__ == '__main__':
    app.run(debug=True, port=251)
