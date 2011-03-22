/*
  Histogram Widget for CortexUI

  
*/
function Histogram(div, dataurl, data) {
  this.inheiritFrom = WidgetCanvas;
  this.inheiritFrom(div, dataurl, data);
  
  this.render = function() {
    new Sparkline(this.canvas, this.data, {
      "top_padding": 5,
      "bottom_padding":5  
      }).draw();
  }
}
