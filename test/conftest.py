import pytest
from py_summer import app as testapp, db, engine, Base
import os
import tempfile


@pytest.fixture
def app():
    @testapp.route('/hello')
    def get_user():
        return 'py_summer'

    db_fd, db_path = tempfile.mkstemp()
    yield testapp, db_path
    os.close(db_fd)
    os.unlink(db_path)


@pytest.yield_fixture()
def db():
    Base.metadata.create_all(engine)
    # yield db
    # Base.metadata.drop_all(engine)


@pytest.yield_fixture
def client(app):
    with app[0].test_client() as client:
        yield client
