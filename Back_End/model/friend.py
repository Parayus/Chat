from db import db


class FriendModel(db.Model):
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    friend = db.Column(db.Integer)
    status = db.Column(db.String(100))
    # id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # users = db.relationship('UserModel')

    def __init__(self, freind1, freind2):
        self.user = freind1
        self.friend = freind2
        self.status = 'pending'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_by_id(cls, id1, id2):
        return cls.query.filter_by(user=id1, freind=id2).first()

    @classmethod
    def friends(cls, user):

        return cls.query.filter_by(user=user, status='friend').all()

    @classmethod
    def friends_pending(cls, user):

        return cls.query.filter_by(friend=user, status='pending').all()

