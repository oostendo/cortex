from cortex.tests import *

class TestFrameController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='frame', action='index'))
        # Test response...
