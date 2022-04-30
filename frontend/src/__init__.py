from flask import Flask
from src.database.Database import Database

app = Flask(__name__)

db = Database()

import src.views.index_views
import src.views.auth_view
