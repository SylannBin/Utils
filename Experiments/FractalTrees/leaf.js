
"use strict";

/**
 * 
 * 
 */
function Leaf(){
  this.pos = createVector(random(width), random(height - 100));
  this.reached = false;

  this.show = function() {
    fill(120,180,140);
    noStroke();
    ellipse(this.pos.x, this.pos.y, 12, 4);
  }
}