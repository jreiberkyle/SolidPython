#! /usr/bin/env python

from solid import *

# you can store any "openscad" object in a regular variable. No matter whether
# it's just a primitive or a complete assembly
c = cube([10, 20, 30])
s = sphere(10)

d = c - s
# Operators: This is from the operators extension.
# The following operators are defined:
#
#   operator    |   action
#   ------------|-------------
#      +, |     | union
#      -        | difference
#      *, &     | intersection
#       ~       | debug (see 03-debug-background.py)

d.save_as_scad()

# this is the same as 01-basics just using a more pythonic way to express it.
#
# If you execute this file it will create examples/02-vars-and-operators.py with
# the this content:
#
#    // Generated by ExpSolidPython
#
#    difference() {
#            cube(size = [10, 20, 30]);
#            sphere(r = 10);
#    };

