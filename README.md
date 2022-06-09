# ConwayOneD

In this project I am writing a version of John Conway's Game of Life that exists in one dimension. Writing it in python to practice tkinter, although I might port to javascript to use d3 instead. 

Because the 1D case is not super interesting, the program can handle an update to the ruleset. In order to do so, use updateRuleset(R_B__S__) where the R represents the radius, B represents the number of neighbors that will revive a dead square, and S represents the number of neighbors which will preserve an alive square.

The recursion relation runs until it reaches a 1 step equality, or until it has run 20 (can be changed) times.
