from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    salt = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, name, email, password, salt):
        self.name = name
        self.email = email
        self.password = password
        self.salt= salt
    
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }