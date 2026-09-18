
import matplotlib.pyplot as plt

# Define and initialize the global excersise state
class GaspardState(list):
    def __init__(self):
        super().__init__(); print("State initialized succesfully")

    def new(self, new_state):
        self.clear()
        self.extend(new_state)

    # Override many list methods to make them unusable
    def insert(self): pass
    def remove(self): pass
    def pop(self): pass
    def index(self): pass
    def count(self): pass
    def sort(self): pass
    def reverse(self): pass
    def copy(self): pass
    def __delitem__(self): pass

State = GaspardState()



def dihedral():
    # A3 dimensions (in)
    fig, ax = plt.subplots(figsize=(11.69, 16.54))
    # No ticks
    ax.set_xticks([]); ax.set_yticks([])
    # Padding = 3%
    fig.subplots_adjust(
        left=0.03, right=0.97, bottom=0.03, top=0.97,
    )

    # A3 sheet limits (cm) and aspect ratio
    ax.set_xlim(-14.85, 14.85); ax.set_ylim(-21, 21)
    ax.set_aspect("equal")

    # X axis
    ax.axhline(0, linewidth=1, c='k')
    ax.text(
        0.017, -0.35, # Appears on the left under the axis
        r"$x$", size=15,
        transform=ax.get_yaxis_transform(), # Position the x consistently
        ha="right", va="center"
    )

    # plt.sca(ax)
    
    return fig, ax

dihedral()
