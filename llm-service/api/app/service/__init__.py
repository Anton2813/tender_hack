import torch
from ..manager.analyzer import LLMManager
from .common import *
from .chat import *
from semantic_equality import semantic_cosine, symbolic_levenshtein

def create_app():
    app = Flask(__name__)
    init_routers(app)
    return app
