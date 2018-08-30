from flask import Flask
from common.database import Database

app = Flask(__name__)
app.config.from_object('config')


@app.before_first_request
def init():
    Database.initialize()


from api.api_handicraft import handicraft_blueprint
app.register_blueprint(handicraft_blueprint, url_prefix="/handicraft")
