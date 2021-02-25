from app import db


#定義模型(model)
class User(db.Model):  # (多)
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    name = db.Column(db.String(80), unique=True, nullable=False)
    #  relationship
    message = db.relationship('Message', backref='user')

    def __repr__(self):
        return 'id=%r, User_name=%r' % (self.id, self.name)



