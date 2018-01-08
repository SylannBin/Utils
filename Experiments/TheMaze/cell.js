// Daniel Shiffman
// http://codingtra.in
// http://patreon.com/codingtrain

// Videos
// https://youtu.be/HyK_Q5rrcr4
// https://youtu.be/D8UgRyRnvXU
// https://youtu.be/8Ju_uxJ9v44
// https://youtu.be/_p5IH0L63wo

// Depth-first search
// Recursive backtracker
// https://en.wikipedia.org/wiki/Maze_generation_algorithm

"use strict";

function Cell(col, row) {
  this.Col = col;
  this.Row = row;
  this.Walls = {
    Top   : true,
    Right : true,
    Bottom: true,
    Left  : true
  };
  // States
  this.IsStartingCell = false;
  this.IsCurrent = false;
  this.Visited = false;
  this.Revisited = false;
  this.IsObstacle = false;


  /**
   * Draws the cell with the proper fill color
   * and proper walls.
   */
  this.Draw = function()
  {
    // This Cell Origin
    var x = this.Col * CELL_WIDTH;
    var y = this.Row * CELL_HEIGHT;
    // Draw the walls
    this.drawWalls(x, y);
    // Draw the cell itself
    this.highlight(x, y);
  }


  /**
   * Changes the color of the cell in a specific color
   * depending on its state.
   */
  this.highlight = function(x, y)
  {
    // Re Draw cell
    noStroke();
    // check state (order is important)
    if      (this.IsStartingCell) fill(255, 255, 125, 100);
    else if (this.IsObstacle)     fill(125, 125, 125, 100);
    else if (this.Revisited)      fill( 50,   0, 125, 100);
    else if (this.IsCurrent)      fill(  0,   0, 255, 100);
    else if (this.Visited)        fill(255,   0, 255, 100);
    else                          fill(  0,   0,   0,   0);
    rect(x, y, CELL_WIDTH, CELL_HEIGHT);
  }

  /**
   * Draw the needed walls
   */
  this.drawWalls = function(x, y)
  {
    // Getting boundaries
    var top = y;
    var right = x + CELL_WIDTH;
    var bottom = y + CELL_HEIGHT;
    var left = x;
    // Drawing
    stroke(255);
    if (this.Walls.Top)    line(left,  top,    right, top);
    if (this.Walls.Right)  line(right, top,    right, bottom);
    if (this.Walls.Bottom) line(left,  bottom, right, bottom)
    if (this.Walls.Left)   line(left,  top,    left,  bottom);
  }


}