import logging.config
from flask import Flask
from coderakki import main_app
from coderakki.paths import logconf



app = main_app()
logger = logging.getLogger('coder')


def init_log():
    logging.config.fileConfig(logconf)
    logging._srcfile = None
    logging.logThreads = 0
    logging.logProcesses = 0

if __name__ == "__main__":
    init_log()
    app.run(debug=True)

