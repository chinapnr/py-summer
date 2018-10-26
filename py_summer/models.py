from py_summer import db


class Test(db.Model):

    # 建立用户信息表
    __tablename__ = 'test_table'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    score = db.Column(db.SmallInteger)
