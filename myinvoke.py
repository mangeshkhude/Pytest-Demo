
import pytest

class MyPlugin(object):

    def pytest_sessionfinish(self):
        print("*** test run reporting finish")

pytest.main(["-qq"], plugins=[MyPlugin()])