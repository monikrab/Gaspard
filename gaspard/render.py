
import matplotlib
import matplotlib.pyplot as plt
from .defs import Monge


def Render(state):
    # Enable interactive mode
    plt.ion()

    matplotlib.use('QtAgg')

    monge = Monge()

    for name, obj in state.items():
        obj.render(monge, name)

    ax = plt.gca()

    plt.show(block=True)
