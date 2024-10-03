#visualizer for fractal generator
import warnings
import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

#function returns a complex matrix of the given dimensions. xmin, xmax horizontal range,
#  ymin, ymax vertical range, pixel_density number of pixels per unit
def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int ((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int ((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

#function returns a boolean matrix of the same dimensions as the input matrix c
def is_stable(c, num_iter):
    z = 0
    for i in range(num_iter):
        z = z**2 + c
    return abs(z) <= 2

#returns 1D array of complex numbers that are members of the Mandelbrot set
def get_members(c, num_iter):
    mask = is_stable(c, num_iter)
    return c[mask] 

#plotting the Mandelbrot set
c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)
members = get_members(c, num_iter=20)

plt.scatter(members.real, members.imag, color="black", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()