
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class Coord:
    x: float
    y: float


class Point:
    def __init__(self, *args):
        # e.g. Point("A", 1, 2, -3.5)
        if len(args) == 4 and all(isinstance(arg, (float, int)) for arg in args[1:]):
            self.ab, self.af, self.ct = map(float, args[1:])

            P1 = Coord(self.ab, -self.af); P2 = Coord(self.ab, self.ct)

            # Marker at P1
            plt.plot(P1.x, P1.y, "o", ms=2, c='k')
            # Vertical projection line from the projection's height (y) to x axis (0)
            plt.plot(
                [P1.x, P1.x], [P1.y, 0],
                "-", c="0.5", lw=0.7,
            )
            plt.annotate(
                rf"${args[0]}_1$", (P1.x, P1.y), # Shows up as P_1 (subscript)
                fontsize=11,
                xytext=(3, -5), # More downward offset to match the upper one
                textcoords="offset points", # Offset from points, not global axis coordinates
            )

            # Same thing for the vertical projection
            plt.plot(P2.x, P2.y, "o", ms=2, c='k')
            plt.plot(
                [P2.x, P2.x], [P2.y, 0],
                "-", c="0.5", lw=0.7,
            )
            plt.annotate(
                rf"${args[0]}_2$",
                (P2.x, P2.y),
                fontsize=11,
                xytext=(3, 2), textcoords="offset points",
            )
