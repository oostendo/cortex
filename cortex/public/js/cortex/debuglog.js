/*
  Histogram Widget for CortexUI

  
*/
function DebugLog(div, dataurl, data) {
  this.inheiritFrom = Widget;
  this.inheiritFrom(div, dataurl, data);

  this.render = function() {
    objDiv = $("#"+this.div);
    objDiv.html("<pre>" + this.data + "</pre>");
    objDiv.scrollTop(objDiv[0].scrollHeight);
  }

}
