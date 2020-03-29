from flask import Flask

APP = Flask(__name__)
APP.config.from_mapping({'DEBUG': True})
