from app.constants import MODE


def test_mode():
    assert MODE.DEV == "development"
    assert MODE.PROD == "production"
