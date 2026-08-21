
import matplotlib.pyplot as plt


class Monge:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(8.27, 11.69))

        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.fig.subplots_adjust(
            left=0.04,
            right=0.96,
            bottom=0.04,
            top=0.96,
        )

        self.ax.set_xlim(-14, 14)
        self.ax.set_ylim(-20, 20)
        self.ax.set_aspect("equal")

        self.ax.axhline(0, linewidth=1)
        self.ax.text(
            1.01, 0,
            r"$X$",
            transform=self.ax.get_yaxis_transform(),
            ha="left",
            va="center"
        )


class Unknown:
    pass


class Point:
    def __init__(self, ab, af, ct):
        self.ab = float(ab)
        self.af = float(af)
        self.ct = float(ct)

    def render(self, monge, name=None):
        A1 = (self.ab, -self.af)
        A2 = (self.ab, self.ct)

        monge.ax.plot(*A1, "o")
        monge.ax.plot(*A2, "o")

        monge.ax.plot(
            [A1[0], A2[0]],
            [A1[1], A2[1]],
            linestyle="-",
            linewidth=0.9,
        )

        if name:
            monge.ax.annotate(
                rf"${name}_1$",
                A1,
                xytext=(4, 4),
                textcoords="offset points",
            )

            monge.ax.annotate(
                rf"${name}_2$",
                A2,
                xytext=(4, 4),
                textcoords="offset points",
            )


# class Line:
#     def __init__(self, A, B):
#         self.A = A
#         self.B = B

#     def render(self, monge, name=None):
#         A1 = (self.A.ab, -self.A.af)
#         A2 = (self.A.ab, self.A.ct)

#         B1 = (self.B.ab, -self.B.af)
#         B2 = (self.B.ab, self.B.ct)

#         monge.ax.axline(A1, B1)
#         monge.ax.axline(A2, B2)

#         H_ab = (
#             self.A.ab
#             - self.A.ct * (self.B.ab - self.A.ab)
#             / (self.B.ct - self.A.ct)
#         )

#         F_ab = (
#             self.A.ab
#             - self.A.af * (self.B.ab - self.A.ab)
#             / (self.B.af - self.A.af)
#         )

#         monge.ax.plot(H_ab, 0, "o")
#         monge.ax.plot(F_ab, 0, "o")

#         if name:
#             monge.ax.annotate(
#                 rf"${name}_1$",
#                 (
#                     (A1[0] + B1[0]) / 2,
#                     (A1[1] + B1[1] - 1.6) / 2,
#                 ),
#             )

#             monge.ax.annotate(
#                 rf"${name}_2$",
#                 (
#                     (A2[0] + B2[0]) / 2,
#                     (A2[1] + B2[1] + 1.6) / 2,
#                 ),
#             )

#         monge.ax.annotate(r"$H_1$", (H_ab, -0.5))
#         monge.ax.annotate(r"$F_1$", (F_ab, 0.5))
