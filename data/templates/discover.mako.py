# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1300159547.623498
_template_filename='/home/home/oostendo/dev/cortex/cortex/cortex/templates/discover.mako'
_template_uri='/discover.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html \n     PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n    <head>\n        <title>Cortex</title>\n')
        # SOURCE LINE 8
        for js in c.jsincludes:
            # SOURCE LINE 9
            __M_writer(u'          <script type="text/javascript" src="')
            __M_writer(escape(js))
            __M_writer(u'"></script> \n')
            pass
        # SOURCE LINE 11
        for css in c.stylesheets:
            # SOURCE LINE 12
            __M_writer(u'          <style type="text/css" rel="stylesheet" href="')
            __M_writer(escape(css))
            __M_writer(u'"></style>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'        <style type="text/css">\n\nbody { font-family:verdana, arial, sans-serif; font-size:12px; background-image: url(/frame/index); background-repeat:no-repeat; background-position:center top; background-attachment:fixed; /*-o-background-size: 100% 100%, auto; -moz-background-size: 100% 100%, auto; -webkit-background-size: 100% 100%, auto;*/ background-size: 100% , auto; }\n\n#histogram { position:absolute; bottom: 0; width: 500; height: 50}\n        </style>\n    </head>\n    <body>\n')
        # SOURCE LINE 22
        for w in c.widgets:
            # SOURCE LINE 23
            __M_writer(u'         <canvas id="')
            __M_writer(escape(w["id"]))
            __M_writer(u'"></canvas>\n')
            pass
        # SOURCE LINE 25
        __M_writer(u'       <script type="text/javascript">\n')
        # SOURCE LINE 26
        for w in c.widgets:
            # SOURCE LINE 27
            __M_writer(u"           cortex.registerWidget('")
            __M_writer(escape(w["id"]))
            __M_writer(u"', ")
            __M_writer(w["constructor"] )
            __M_writer(u');\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'\n         cortex.refresh();\n       </script>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


