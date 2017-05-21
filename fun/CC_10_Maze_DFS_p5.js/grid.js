"use strict";

function Grid(){
  this.nbCols;
  this.nbRows;
  this.cells = [];
  this.stack = [];
  this.currentCell;


  /**
   * Build the Grid and fill it with cells
   */
  this.Init = function()
  {
    this.nbCols = floor(window.width/CELL_WIDTH);
    this.nbRows = floor(window.height/CELL_HEIGHT);

    for (var   row = 0; row < this.nbRows; row++)
      for (var col = 0; col < this.nbCols; col++)
        this.cells.push(new Cell(col, row));

    this.initObstacles(OBSTACLE_ODDS);
    this.initStartingCell();
  }


  /**
   * Draw the Grid
   */
   this.Draw = function()
   {
     this.currentCell.IsCurrent = true;

     for (var index = 0; index < this.cells.length; index++) {
       this.cells[index].Draw();
     }
   }


  /**
   * Update the grid and inform of the state
   * @return {int} state (0: normal, 1: dead end, 2: gameover)
   */
  this.Update = function()
  {
    // Pick nextCell destination from neighbors
    var nextCell = this.pickNeighbor(this.currentCell);
    // Available unvisited neighbor
    if (nextCell) {
      nextCell.Visited = true;
      this.stack.push(this.currentCell);
      this.updateWalls(this.currentCell, nextCell);
      this.currentCell.IsCurrent = false;
      this.currentCell = nextCell;
      return 0;
    }
    // All neighbors visited
    else if (this.stack.length > 0) {
      this.currentCell.Revisited = true;
      this.currentCell = this.stack.pop();
      return 1;
    }
    // No more unvisited cells
    return 2;
  }


  /**
   * Remove proper walls according to relative
   * position of both current and next cells.
   */
  this.updateWalls = function(currCell, nextCell)
  {
    var xOffset = currCell.Col - nextCell.Col;
    var yOffset = currCell.Row - nextCell.Row;
    
    if (xOffset === 1) {
      currCell.Walls.Left  = false;
      nextCell.Walls.Right = false;
    }
    else if (xOffset === -1) {
      currCell.Walls.Right = false;
      nextCell.Walls.Left  = false;
    }
    if (yOffset === 1) {
      currCell.Walls.Top    = false;
      nextCell.Walls.Bottom = false;
    }
    else if (yOffset === -1) {
      currCell.Walls.Bottom = false;
      nextCell.Walls.Top    = false;
    }
  }


  /**
   * Chose randomly one of the available neighbors
   */
  this.pickNeighbor = function(cell) {
    var neighbors = this.getNeighbors(cell.Col, cell.Row);

    return (neighbors.length > 0)
      ? neighbors[floor(random(0, neighbors.length))]
      : undefined;
  }


  /**
   * Gather all the available neighbors,
   * avoiding both out of Grid positions
   * and already visited cells.
   */
  this.getNeighbors = function(col, row)
  {
    var neighbors = [];

    neighbors.push(this.getCell(col, row - 1));
    neighbors.push(this.getCell(col + 1, row));
    neighbors.push(this.getCell(col, row + 1));
    neighbors.push(this.getCell(col - 1, row));

    return neighbors.filter(
      cell => cell // is defined
      && !cell.IsObstacle
      && !cell.Visited)
  }


  /**
   * Get the cell of the grid at the
   * provided coordinantes (col, row)
   * @return {Cell} target cell
   */
  this.getCell = function(col, row)
  {
    return this.cells[this.to2DIndex(col, row)]
  }


  /**
   * Simulate 2D array postioning inside
   * of the 1D array.
   * @return {int} index
   */
  this.to2DIndex = function(col, row)
  {
    if ( col >= 0
      && row >= 0
      && col < this.nbCols
      && row < this.nbRows)
      return col + row * this.nbCols;
    return -1;
  }


  /**
   * Randomly set cells as obstacles based on odds
   * and such that no cell in the grid gets inaccessible.
   */
  this.initObstacles = function(odds)
  {
    for (var i = 0; i < this.cells.length; i++){
      // at least 1 way to access this cell
      var cell = this.cells[i];
      var neighbors = this.getNeighbors(cell.Col, cell.Row);
      if (neighbors.length > 0 && floor(random(0, odds)) === 0)
      {
          this.cells[i].IsObstacle = true;
      }
    }
  }


  /**
   * Sets the starting position in a suitable
   * place (not on an obstacle).
   */
  this.initStartingCell = function()
  {
    var index;
    while(true){
      console.log("olala");
      index = floor(random(0, this.cells.length));
      if (!this.cells[index].IsObstacle)
        break;
    }

    this.currentCell = this.cells[index];
    this.currentCell.IsStartingCell = true;
    this.currentCell.Visited = true;
  }
}