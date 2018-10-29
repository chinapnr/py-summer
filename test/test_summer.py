import pytest


@pytest.mark.usefixtures('client')
class TestSummer:
    def test_get(self, client):
        response = client.get('/hello')
        assert response.data == b'py_summer'
