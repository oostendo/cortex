import logging
import redis

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from cortex.lib.base import BaseController, render

log = logging.getLogger(__name__)
rd = redis.Redis(host='localhost', port=6379, db=0)

class DiscoverController(BaseController):

    def index(self):
        # Return a rendered template

        c.stylesheets = ["/css/ui-lightness/jquery-ui-1.8.10.custom.css",
          "/css/style.css"]

        c.jsincludes = ["/js/processing.js",
          "/js/sparklines.min.js",
          "/js/jquery-1.4.4.min.js",
          "/js/jquery-ui-1.8.10.custom.min.js",
          "/js/cortex/cortex.js",
          "/js/cortex/histogram.js"] 

        c.widgets = [ { "id": "histogram", "constructor": "new Histogram('histogram', '/GET/histogram.txt')" } ]

        return render('/discover.mako')
        # or, return a string
        #return 'Hello World'
