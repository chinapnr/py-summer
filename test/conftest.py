import pytest
from summer import create_server


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""

    app = create_server({
        'TESTING': True,
    })

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
