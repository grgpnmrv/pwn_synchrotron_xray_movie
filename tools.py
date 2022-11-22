from config import DATA_DIR, SNAPSHOTS_DIR, MOVIES_DIR
from functools import wraps
from managers import MapManager, PlotManager
from subprocess import call
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np


def cmd(command: str):
    """ Execute linux commands """
    call(command, shell = True)


def draw_xray_map(plot, data, time, cmap, limits = (0, 0.2)):
    """ 
    Produces synthetic x-ray emission map
    of the pulsar wind nebula model    
    """

    axes = plot.add_subplot(1, 1, 1)
    plt.title(f"t = {time} yr", fontsize=16, y=1.0) #, pad=+18)
    im = plt.imshow(data, cmap=cmap, vmin=limits[0], vmax=limits[1])
    cb = plt.colorbar(im, ax=axes, pad=0.02)
    cb.ax.tick_params(labelsize=16)
    cb.ax.yaxis.get_offset_text().set(size=16)
    axes.set(xticks=[], yticks=[])
    plt.plot([150], [150], 'ro', markersize=5, label = "pulsar")
    plt.legend()
    plt.savefig(f"{SNAPSHOTS_DIR}xray_map_dynamics_{time}.png")


def unzip_and_cleanup(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """
        This wrapper extracts data from zip archive,
        performs some actions with data and cleans up
        extracted datasets after the job is done
        """

        cmd(f"unzip -q {DATA_DIR}data.zip -d {DATA_DIR}")
        function(*args, **kwargs)
        cmd(f"rm {DATA_DIR}*.dat")
    return wrapper


@unzip_and_cleanup
def create_snapshots(first: int, last: int):
    """ Creates snapshots for each timestep """

    for i in range(first, last + 1):
        with MapManager(f"{DATA_DIR}syn_{i}.dat") as xray_map, PlotManager() as plot:
            timestep = i / 10
            draw_xray_map(plot, xray_map, timestep, cm.jet)


def create_movie(delay: int):
    """ Creates gif-animation of the pulsar
        wind nebula in dynamics
    """

    cmd(
        f"convert -delay {delay} -loop 0 {SNAPSHOTS_DIR}*.png {MOVIES_DIR}pwn_dynamics.gif"
    )
