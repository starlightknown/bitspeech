from flask import Blueprint

post_blueprint = Blueprint("post", __name__)

from bitspeech.post import routes
