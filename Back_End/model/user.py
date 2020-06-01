from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80), nullable=True)
    full_name = db.Column(db.String(80))
    email_id = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80),nullable=False)

    # friends = db.relationship('FriendModel')
    def __init__(self,username,first_name,last_name,full_name,email_id,password):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email_id = email_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls,email):
        return cls.query.filter_by(email_id=email).first()
    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
        'first_name': self.first_name,
        'last_name' : self.last_name,
        'full_name': self.full_name,
        'email_id': self.email_id
        }



