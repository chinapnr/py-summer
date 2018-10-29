import pytest
from application import db
from application.model.test import Test


@pytest.mark.usefixtures('db')
class TestTable:
    def test_get_by_id(self):
        user = Test(name='test_name', score=100)
        db.add(user)
        db.commit()

        retrieved = Test.get_info_by_id(user.uid)
        assert retrieved == user
