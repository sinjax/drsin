from drsin.tests import *

class TestAndroidtestController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='androidTest', action='index'))
        # Test response...
