from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv() #To load variables of .env file


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "https://simulacion-laboral.vercel.app"])

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
migrate = Migrate(app, db) #To user the flask db migrate command
#api routes
import routes

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run (debug=True)