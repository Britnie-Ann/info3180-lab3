from flask import Flask
from flask_mail import Mail
from app import config

app = Flask(__name__)
from app import views
app.config.from_object(config)
mail = Mail(app)