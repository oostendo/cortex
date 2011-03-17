/*
  Histogram Widget for CortexUI

  
*/
function Histogram(canvas, dataurl, data) {
  this.inheiritFrom = Widget;
  this.inheiritFrom(canvas, dataurl, data);

  this.render = function() {
    new Sparkline(this.canvas, this.data, {
      "top_padding": 5,
      "bottom_padding": 10
      }).draw();
  }
}
