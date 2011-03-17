<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html 
     PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <title>Cortex</title>
        % for js in c.jsincludes:
          <script type="text/javascript" src="${js}"></script> 
        % endfor
        % for css in c.stylesheets:
          <style type="text/css" rel="stylesheet" href="${css}"></style>
        % endfor
        <style type="text/css">

body { font-family:verdana, arial, sans-serif; font-size:12px; background-image: url(/frame/index); background-repeat:no-repeat; background-position:center top; background-attachment:fixed; /*-o-background-size: 100% 100%, auto; -moz-background-size: 100% 100%, auto; -webkit-background-size: 100% 100%, auto;*/ background-size: 100% , auto; }

#histogram { position:absolute; bottom: 0; width: 500; height: 50}
        </style>
    </head>
    <body>
       % for w in c.widgets:
         <canvas id="${w["id"]}"></canvas>
       % endfor
       <script type="text/javascript">
         % for w in c.widgets:
           cortex.registerWidget('${w["id"]}', ${w["constructor"] | n});
         % endfor

         cortex.refresh();
       </script>
    </body>
</html>
