from cortex.tests import *

class TestDiscoverController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='discover', action='index'))
        # Test response...
