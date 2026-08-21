
import gaspard
from gaspard import Point


state = gaspard.State = {
    "A": Point(1, 2, 3),
    "B": Point(2, 3, 4)
}

target = gaspard.Target

solution = gaspard.Solve(state, target)
print(solution)
