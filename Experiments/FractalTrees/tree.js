
"use strict";

/**
 * 
 * @param {int} nbLeaves
 * @param {int} minDistance
 * @param {int} maxDistance
 * @param {int} defaultRecord
 */
function Tree(nbLeaves, minDistance, maxDistance, defaultRecord) {
  this.leaves = [];
  this.branches = [];

  this.nbLeaves = nbLeaves;
  this.minDistance = minDistance;
  this.maxDistance = maxDistance;
  this.defaultRecord = defaultRecord;
  /**
   * Grow trunk and leaves once at the begining
   * (yes, leaves grow directely in the air,
   * they don't need branches)
   */
  this.sead = function()
  {
    growLeaves(this.nbLeaves);
    growTrunk();
  }


  /**
   * Draw trunk, branches and leaves
   */
  this.show = function() {
    for (var i = 0; i < this.leaves.length; i++) {
      this.leaves[i].show();
    }
    for (var i = 0; i < this.branches.length; i++) {
      this.branches[i].show();
    }
  }

  /**
   * Produce branches, linking each other recursively
   */
  this.grow = function()
  {
    for (var i = 0; i < this.leaves.length; i++) {
      var leaf = this.leaves[i];
      var closestBranch = null;
      var record = this.defaultRecord;
      for (var j = 0; j < this.branches.length; j++) {
        var branch = this.branches[j];
        var d = p5.Vector.dist(leaf.pos, branch.pos);
        if (d < this.minDistance) {
          leaf.reached = true;
          closestBranch = null;
          break;
        } else if (d > this.maxDistance) {
          continue;
        } else if (closestBranch === null || d < record) {
          closestBranch = branch;
          record = d;
        }
      }
      if (closestBranch !== null) {
        var newDir = p5.Vector.sub(leaf.pos, closestBranch.pos);
        newDir.normalize();
        closestBranch.dir.add(newDir);
        closestBranch.count++;
      }
    }

    // reverse loop leaves to be able to safely delete
    // those that were reached.
    for (var i = this.leaves.length; --i >= 0 ;) {
      if (this.leaves[i].reached) {
        this.leaves.splice(i, 1);
      }
    }

    // reverse loop branches to be able to safely add
    // new child branches recursively.
    for (var i = this.branches.length; --i >=0;) {
      var branch = this.branches[i];
      if (branch.count > 0) {
        branch.dir.div(branch.count + 1);
        branch = branch.next();
        this.branches.push(branch);
      }
      branch.reset();
    }
  }

  /**
   * So faking private methods is possible after all :-D
   */
  var growTrunk = (function()
  {
    var pos = createVector(window.width / 2, window.height);
    var dir = createVector(0, -1);
    var root = new Branch(null, pos, dir);

    this.branches.push(root);
    var currentBranch = root;

    // Search a leaf close enough to the current branch
    var found = false;
    while (!found)
    {
      for (var i = 0; i < this.leaves.length; i++) {
        var d = p5.Vector.dist(currentBranch.pos, this.leaves[i].pos);
        if (d < this.maxDistance) {
          found = true;
        }
      }
      if (!found) {
        currentBranch = currentBranch.next();
        this.branches.push(currentBranch);
      }
    }
  }).bind(this);


  /**
   * So faking private methods is possible after all :-D
   * Populates the tree with leaves
   * @param {int} nbLeaves
   */
  var growLeaves = (function (nbLeaves)
  {
    for (var i = 0; i < nbLeaves; i++) {
      this.leaves.push(new Leaf());
    }
  }).bind(this);
}