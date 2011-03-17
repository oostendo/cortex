from cortex.tests import *

class TestHistogramController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='histogram', action='index'))
        # Test response...
