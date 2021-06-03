# ======================================================
# = add relative path to the solid package to sys.path =
# ======================================================
import sys
from pathlib import Path
solidPath = Path(__file__).absolute().parent.parent.parent.as_posix()
sys.path.insert(0, solidPath)
#==================================================

from solid import *

# you can use OpenSCAD libraries in SolidPython. This examples needs the bosl
# library to be installed in the OpenSCAD library path
# (~.local/share/OpenSCAD/libraries)
#
# NOTE: you can import any *.scad file not only "libraries"

#import bosl.metric_screw and wrap it in a simple namespace
from types import SimpleNamespace
bosl = SimpleNamespace()
bosl.metric_screws = import_scad("BOSL/metric_screws.scad")

#use it to generate a metric screw
screw = bosl.metric_screws.metric_bolt(size=6, headtype='hex', l=20)

screw.save_as_scad()

#NOTE: BOSL2 see 07-libs-bosl2.py
