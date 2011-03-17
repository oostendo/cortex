/*
  Class Cortex 

  cortex is the master class which controls all widgets, and lets the widgets
  talk to each other.  It also holds the keys to the webdis data access point

*/

cortex = new function Cortex() {  //Javascript Singleton
  this.widgets = {};//where we store our widgets that we have to keep track of
  this.datasource = ""; //location of our webdis server
  this.lastupdate = ""; //when the last refresh occurred

  this.registerWidget = function(name, widget) {
    this.widgets[name] = widget;
  }

  this.releaseWidget = function(name) {
    this.widgets[name].shutdown();
    delete this.widgets[name];
  }

  this.refresh = function(names) {
    if (!names || names.length == 0) {
      names = [];
      for (var i in this.widgets) { 
        names.push(i); // default to refreshing all widgets
      }
    }
    for (var k in names) {
      this.widgets[names[k]].refresh();  //refresh any widgets
    }
  }

}
  
/* 
  Class Widget

  this is an abstract class for all the widgets in cortex, it provides
  the basic constructor, and default methods. 

  Constructor Parameters:
  canvas - ID of canvas element where widget is rendered
  dataurl - ID of where JSON data feed will be published
  data - initial data for widget
*/

function Widget(canvas, dataurl, data) { 
  this.canvas = canvas;
  this.datafeed = cortex.datasource + dataurl;
  if (data && typeof(data) == "object") {
      this.data = data 
  }

  this.render = function() { alert("hi"); }  //abstract -- implemented by instances

  this._dataCallback = function(data) {
    this.data = jQuery.parseJSON(data);
    this.render();
  }
  this.refresh = function() {
    jQuery.ajax({
      url: this.datafeed, 
      context: this,
      success: this._dataCallback});
  }
  this.shutdown = function() {
    $("#"+this.canvas).hide();
  }
}
