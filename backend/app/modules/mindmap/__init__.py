from flask import Blueprint

mindmap_bp = Blueprint('mindmap', __name__)

from . import routes 