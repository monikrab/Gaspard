
from matplotlib import use; use('QtAgg')
import matplotlib.pyplot as plt
import shapely

plt.rcParams.update({
    "font.serif": ["Computer Modern Roman"], "mathtext.fontset": "cm"
})
plt.ion() # Enable interactive mode

# -----------------------------------------------------------------


from .objects import Point
from .constraints import State

def show_solution():
    plt.show(block=True)
