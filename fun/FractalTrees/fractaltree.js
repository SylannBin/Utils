
"use strict";

/**
 * Defines a tree that has the ability to grow by a fractal pattern,
 * following the L-system.
 * 
 * Usage:
 * 1 - Declare a global tree in sketch.
 * 2 - Instanciate it with this constructor in the setup function.
 * 3 - Make it live in the draw function.
 */
function FractalTree()
{
  this.axiom = "F";
  this.sentence = this.axiom;
  this.baseLength = 20;
  this.growthPower = 0.75;
  this.minGrowth = 0.7;
  this.maxGrowth = 1.3;
  this.life = 0;
  this.lifespan = 4;
  this.tau = {
    "F": 0.8,
    "G": 1.1,
    "H": 1.4
  }
  this.patterns = [{
    a: "F",
    b: "FF+[+F-F-F+G]-[-F+F+F-G]"
  },{
    a: "G",
    b: "FF+[+F-G-F]-[-F+G+F]"
  },{
    a: "H",
    b: "FF+[+H]-[-H]"
  }];


  this.live = function()
  {
    if (this.life < this.lifespan){
      this.life++;
      this.grow();
    }
  }

  this.grow = function()
  {
    this.baseLength *= this.growthPower;
    var nextSentence = "";
    for (var char of this.sentence)
    {
      var found = false;
      for (var pattern of this.patterns)
        if (char == pattern.a)
        {
          found = true;
          nextSentence += pattern.b;
          break;
        }
      if (!found)
        nextSentence += char;
    }
    this.sentence = nextSentence;
    this.convertToDrawing();
  }

  this.convertToDrawing = function()
  {
    background(55);
    resetMatrix();
    translate(window.width / 2, window.height);
    stroke(255, 90);
    var angle = random(PI/6, PI/4);
    for (var char of this.sentence) {
        var coef = random(this.minGrowth, this.maxGrowth);
      switch (char) {
        case "F":
        case "G":
        case "H":
          line(0, 0, 0, -coef * this.tau[char] * this.baseLength);
          translate(0, -coef * this.tau[char] * this.baseLength);
          break;
        case "+":
          rotate(angle);
          break;
        case "-":
          rotate(-angle);
          break;
        case "[":
          push();
          break;
        case "]":
          pop();
          break;
        default:
          break;
      }
    }
  }

}