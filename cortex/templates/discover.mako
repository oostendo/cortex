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
          <link rel="stylesheet" type="text/css" rel="stylesheet" href="${css}" />
        % endfor
    </head>
    <body>
      <div class="widgetbox-wrapper">
      <div class="widgetbox">
       % for w in c.widgets:
         <h3><a href="#">${w["id"]}</a></h3>
         <div class="widget" id="${w["id"]}"></div>
       % endfor
      </div>
      </div>
       <script type="text/javascript">
         % for w in c.widgets:
           cortex.registerWidget('${w["id"]}', ${w["constructor"] | n});
         % endfor

$(function(){

  $('.widgetbox-wrapper').dialog({
    autoOpen: true,
    maxWidth: 425,
    maxHeight: 300,
    height: 425,
    position: ['left', 'bottom' ]
 
  });

  $('.widgetbox').accordion();

  cortex.refresh();
});


       </script>
    </body>
</html>
