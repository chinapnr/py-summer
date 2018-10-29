from application import Base, db
from sqlalchemy import Column, Integer, String


class Test(Base):
    # 建立用户信息表
    __tablename__ = 'test_table'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False, index=True)
    score = Column(Integer)

    @staticmethod
    def get_info_by_id(uid):
        return db.query(Test).filter_by(uid=uid).first()