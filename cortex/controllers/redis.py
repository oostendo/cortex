import logging

from pylons import app_globals, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from cortex.lib.base import BaseController, render

log = logging.getLogger(__name__)
rd = app_globals.rd 

class RedisController(BaseController):

    def ping(self):
        # Return a rendered template
        #return render('/testredis.mako')
        # or, return a string

        if (rd.ping()):
          return "pong" 
        else:
          return ""
