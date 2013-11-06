Cubix_Rube
==========

2D Mapped Puzzle Cube Simulation

Released under MIT License, See LICENSE file for details.
Built on python2 and pygame

Program Descrption:
  Shows a 2D Projection of a 3D 3x3x3 Puzzle Cube
  Allows for most of the Standard Manipulations and Rotations
  common to Cubing.

Running:
  python2 Cubix_Rube.py
  ( Run the Cubix_Rube.py File with Python 2.6 or 2.7 )

Use:
  The Program Will Show Views of the Up, Front, Back,
  Left, Right and Down Faces as if they were mapped from the
  Surfaces of a 3D Cube.

  Keyboard Shortcuts are Based on Singmaster Notation: http://en.wikipedia.org/wiki/Rubik%27s_Cube#Move_notation

  You can Manipulate the Cube Using the Following Keyboard Shortcuts:
  ( If Any of these Don't Make Sense, Go to: http://en.wikipedia.org/wiki/Rubik%27s_Cube#Move_notation )
    u - Equivalent to U Move ( Turns the Up/Top Face 1/4 Turn Clockwise, as if Facing it )
    d - Equivalent to D Move ( Turns the Down/bottom Face 1/4 Turn Clockwise, as if Facing it )
    l - Equivalent to L Move ( Turns the Left Face 1/4 Turn Clockwise, as if Facing it )
    r - Equivalent to R Move ( Turns the Right Face 1/4 Turn Clockwise, as if Facing it )
    f - Equivalent to F Move ( Turns the Front Face 1/4 Turn Clockwise, as if Facing it )
    b - Equivalent to B Move ( Turns the Back Face 1/4 Turn Clockwise, as if Facing it )
    x - Equivalent to X Move ( Rotates the Entire Cube 1/4 Turn Clockwise, as if Facing the Right Face )
    y - Equivalent to Y Move ( Rotates the Entire Cube 1/4 Turn Clockwise, as if Facing the Up Face )
    z - Equivalent to Z Move ( Rotates the Entire Cube 1/4 Turn Clockwise, as if Facing the Front Face )
    m - Equivalent to M Move ( Rotates the Layer Between L and R 1/4 Turn Clockwise, as if Facing the Left Face )
    e - Equivalent to E Move ( Rotates the Layer Between U and D 1/4 Turn Clockwise, as if Facing the Down Face )
    s - Equivalent to S Move ( Rotates the Layer Between F and B 1/4 Turn Clockwise as if Facing the Front Face )


  To do the Opposite of a Move ( Counter-Clockwise Version, Hold [Shift] then do the Move )
  NOTE: You can also Hold [shift] to do Multiple Counter-Clockwise Turns in a Row
    Ex. [shift] + r - Equivalent to R' ( Turns Right Face Counter-Clockwise )

  To Turn 2 Layers ( i.e. the Given Layer and the Closest One Parallel to it )
  Hold [ctrl] then do the Move -- This Only Works for u, d, l, r, f and b
  NOTE: You can Hold [ctrl] to do Multiple 2 Layer Turns in a Row
    Ex. [ctrl] + r - Equivalent to r ( Turns Right Face and Closest Parallel Face Clockwise )

  To Turn 2 Layers Counter-Clockwise, Hold [ctrl] and [shift] then do the Move
  This only works for u, d, l, r, f and b

Enjoy,
jedi453
