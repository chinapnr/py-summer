import pytest


@pytest.mark.usefixtures('client')
class TestSummer:
    def test_get(self, client):
        response = client.get('/api/test')
        assert response.status_code == 200
