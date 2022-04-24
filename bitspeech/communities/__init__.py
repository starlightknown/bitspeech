from flask import Blueprint

communities_blueprint = Blueprint("communities", __name__)

from bitspeech.communities import routes
