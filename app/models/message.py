from app import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(120), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return 'id=%r, title=%r,content=%r' % (self.id, self.title,self.content)