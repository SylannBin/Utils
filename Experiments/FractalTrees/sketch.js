
"use strict";

var tree;

/**
 * P5 setup function:
 * (Initializes once at page load)
 * Creates and fills canvas with a grid.
 */
function setup()
{
  createCanvas(400,400);
  background(55);
  //tree = new FractalTree();
  tree = new Tree(400, 10, 60, 100000);
  tree.sead();
  // console.log(tree);
}


/**
 * P5 draw function:
 * (Executes as long as loop is enabled)
 * Draws the grid and updates it if needed/possible.
 */
function draw() {
  //tree.live();
  tree.show();
  tree.grow();
}


function mousePressed()
{
  noLoop();
}