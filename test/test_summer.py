from py_summer import create_server


def test_config():
    """Test create_app without passing test config."""
    assert not create_server().testing
    assert create_server({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
