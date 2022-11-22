import numpy as np
import matplotlib.pyplot as plt


class MapManager:
    """ Handles data preparation"""

    def __init__(self, dataset):
        self.dataset = dataset

    def __enter__(self):
        return np.genfromtxt(self.dataset)

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass


class PlotManager:
    """ Handles plot opening/closing"""

    def __enter__(self):
        return plt.figure()

    def __exit__(self, exc_type, exc_value, exc_tb):
        plt.close()