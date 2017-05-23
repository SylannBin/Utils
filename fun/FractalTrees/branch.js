
"use strict"

/**
 * FIXME: Thickness factor is hitting performance a lot!
 * Need to remove the multiplier from strokeWeight
 * 
 */
function Branch(parent, position, direction)
{
  this.parent = parent;
  this.pos = position;
  this.dir = direction;
  this.baseThickness = 0.025;
  this.origDir = this.dir.copy();
  this.count = 0;
  this.len = 5;

  this.reset = function()
  {
    this.dir = this.origDir.copy();
    this.count = 0;
  }

  this.next = function(thickness)
  {
    var nextDir = p5.Vector.mult(this.dir, this.len);
    var nextPos = p5.Vector.add(this.pos, nextDir);
    return new Branch(this, nextPos, this.dir.copy(), thickness);
  }


  this.show = function()
  {
    if (this.parent != null) {
      stroke(150,90,60);
      strokeWeight(this.baseThickness * this.pos.y);
      line(this.pos.x, this.pos.y, this.parent.pos.x, this.parent.pos.y);
    }
  }
}