from app import db




class City(db.Model):  # (一)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('User', backref='city')

    def __init__(self, name=None):
        self.name = name

    # 在python中，每個對象都可以用str()與repr()來轉成可顯示的字串，str()'可讀性'較高，是給開發者閱讀對象中的'有用資訊'的字串。
    # 而repr()的英文全名是representation，其產生的字串是給python的直譯器看的，這個字串會顯示'明確且教詳盡的資訊'，通常'可以讓python得知究竟這字串所代表的對象為何

    def __repr__(self):
        return 'id=%r, city_name=%r' % (self.id, self.name)