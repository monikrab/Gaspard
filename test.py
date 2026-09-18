
import gaspard as gd
from gaspard import Point


gd.State.new([
    Point("A", 12, 2, 3),
    Point("B", -6, 10, 4)
])

gd.show_solution()
