from flask import Flask, request, render_template
from pinescriptgen_core.pinescriptgenerator import PineScriptGenerator
from pinescriptgen_core.formhandler import FormHandler
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_handler = FormHandler(request.form)
        form_handler.handle_form_input()
        strategy = form_handler.strategy

        pinescript_code = PineScriptGenerator.generate(strategy)

        return render_template('generated.html', pine_code=pinescript_code)

    return render_template('index.html')


