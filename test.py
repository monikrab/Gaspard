
import gaspard as gd
from gaspard import Point


gd.State.new([
    Point("A", 9, 2, 3),
    Point("B", 3, -4, 1),
    Point("C", 12, 2, -9),
    Point("D", -9, 5, 10),
    Point("E", -6, 10, -4)
])

gd.show_solution()
