from application import db


class Test(db.Model):
    __tablename__ = 'test_table'
    test_id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    test_score = db.Column(db.SmallInteger)