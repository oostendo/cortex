from cortex.tests import *

class TestRedisController(TestController):

    def test_ping(self):
        response = self.app.get(url(controller='testredis', action='index'))
        # Test response...
        if (response == "pong"):
          return 1
        else:
          return 0

