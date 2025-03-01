from pathlib import Path
import numpy as np
import pysocialforce as psf


if __name__ == "__main__":
    # initial states, each entry is the position, velocity and goal of a pedestrian in the form of (px, py, vx, vy, gx, gy)
    initial_state = np.random.normal(loc=10, scale=10, size=(100, 6))
    # social groups informoation is represented as lists of indices of the state array
    groups = [[1, 0], [2], [55, 70], [81, 82, 89]]
    # list of linear obstacles given in the form of (x_min, x_max, y_min, y_max)
    # obs = [[-1, -1, -1, 11], [3, 3, -1, 11]]
    obs = [[1, 2, 7, 8],  [3, 4, 7, 8], [5, 6, 7, 8], [7, 8, 7, 8]]
    # obs = None
    # initiate the simulator,
    s = psf.Simulator(
        initial_state,
        groups=groups,
        obstacles=obs,
        config_file=Path(__file__).resolve().parent.joinpath("example.toml"),
    )
    # update 80 steps
    s.step(10)

    with psf.plot.SceneVisualizer(s, "images/onki_sim1") as sv:
        sv.animate()
        sv.plot()
