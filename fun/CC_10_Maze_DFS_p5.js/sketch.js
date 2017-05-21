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

// Configuration
const CANVAS_WIDTH      = 600
    , CANVAS_HEIGHT     = 600
    , CELL_WIDTH        = 30
    , CELL_HEIGHT       = CELL_WIDTH
    , OBSTACLE_ODDS     = 10
    , IPS               = 120
    , UPDATES_PER_FRAME = 1;

// Globals
var MazeCanvas
  , Grid
  , Turns  = 0
  , State  = 0
  , Paused = false;


/**
 * P5 setup function:
 * (Initializes once at page load)
 * Creates and fills canvas with a grid.
 */
function setup() {
  frameRate(IPS);
  MazeCanvas = createCanvas(CANVAS_WIDTH, CANVAS_HEIGHT);
  MazeCanvas.parent('canvas-container');
  setContainerSize();
  Grid = new Grid();
  Grid.Init();
}


/**
 * P5 draw function:
 * (Executes as long as loop is enabled)
 * Draws the grid and updates it if needed/possible.
 */
function draw() {
  background(55,55,55);
  Grid.Draw();

  for (var u = 0; u < UPDATES_PER_FRAME; u++) {
    Turns++;
    State = Grid.Update();

    if (State == 2){
      addGameOverMessage();
      noLoop();
      break;
    }
  }
}


/**
 * P5 mousePressed function:
 * (Mouse click event)
 * Pause or unpause the game.
 */
function mousePressed() {
  if(State !== 2){
    Paused = !Paused;
    if (Paused)
      noLoop();
    else
      loop();
  }
}


/**
 * 
 */
function setContainerSize(){
  var container = document.getElementById('main-container');
  container.style.width = CANVAS_WIDTH+'px';
  container.style.height = CANVAS_HEIGHT+'px';
}


/**
 * 
 */
function addGameOverMessage(){
  var msgContainer = document.getElementById('msg-container');
  var title = document.createElement('h3');
  var msg = document.createElement('p');
  title.append("GameOver");
  msg.append("Number of turns: " + Turns)
  msgContainer.appendChild(title);
  msgContainer.appendChild(msg);
  console.log("GameOver! Number of turns: " + Turns);
}