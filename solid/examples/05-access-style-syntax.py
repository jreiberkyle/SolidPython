# ======================================================
# = add relative path to the solid package to sys.path =
# ======================================================
import sys
from pathlib import Path
solidPath = Path(__file__).absolute().parent.parent.parent.as_posix()
sys.path.insert(0, solidPath)
#======================================================

from solid import *

# Since I don't like the OpenSCAD syntax I added the "access-style" syntax
# extension. This allows you to call all OpenSCAD builtin transformations, the
# convenience functions (up, down, left,...) and the modifiers (debug,
# background, ...) as if you would call a member function.
#
#       cube(10).up(5)
#
# is equivalent to
#
#       up(5)(cube(10))

c = cube(10, 20, 30).\
        down(5).\
            rotate(45, 45, 45)

s = ~sphere(10).forward(5)

(c-s).save_as_scad()

# generates the exactly the same code as 04-convenience.py:
#
#    // Generated by ExpSolidPython
#
#    difference() {
#            rotate(a = [45, 45, 45]) {
#                    translate(v = [0, 0, -5]) {
#                            cube(size = [10, 20, 30]);
#                    };
#            };
#            #translate(v = [0, 5, 0]) {
#                    sphere(r = 10);
#            };
#    };

