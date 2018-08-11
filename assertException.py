
import pytest

def func():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        func()
