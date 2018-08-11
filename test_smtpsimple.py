

import pytest

@pytest.fixture
def smtp_connection():
    import smtplib
    return smtplib.SMTP("smt.gmail.com", 587, timeout=5)

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.elho()
    assert response == 250
    assert response == 0